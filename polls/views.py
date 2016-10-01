from django.http import HttpResponse
from polls.models import Classes
from django.shortcuts import render
import os
import io
import zipfile

def index(request):
    return render(request,'polls/index.html')
def getuser(request,user_id):
    return HttpResponse("Estas solicitando datos del alumno con id %s" %user_id)
def getname(request,user_id):
    usern = Classes.objects.get(id = user_id)
    print(usern)
    print(type(usern))
    return HttpResponse("Estas solicitando el nombre del alumno con name %s" %usern)
def getfiles(request):
    paths = []
    data = ""
        #gives list of id of inputs
    lists=request.POST.getlist('comps')
    for i in lists:
        data+=i
    print (data)
    if data.find('0')!=-1:
        paths.append("/BIN/a.exe")
    if data.find('1')!=-1:
        paths.append("/BIN/bc.exe")
    if data.find('2')!=-1:
        paths.append("/BIN/sol.exe")
    if data.find('3')!=-1:
        paths.append("/BIN")
        paths.append("/BIN/a.exe")
        paths.append("/BIN/bc.exe")
        paths.append("/BIN/sol.exe")

    s = io.BytesIO()
    zip_subdir = "/"
    zip_filename = "data.zip"
    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    for fpath in paths:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type = "application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=%s' % zip_filename
    resp['Content-length'] = s.tell()

    return resp
