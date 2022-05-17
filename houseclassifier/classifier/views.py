from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .Predicator import ImagePredict
from .models import *

obj=ImagePredict()

def home(request):

    return render(request,'index.html')
def find(request):

    return render(request,'find.html')
def predicate(request):
    if request.method=='POST':
        file_name=request.FILES['file']
        print('@@@',file_name)
        filename_new=file_name.name
        filename_new=filename_new.replace(" ","_")
        fs=FileSystemStorage()
        fs.save(filename_new,file_name)
        data=obj.predictor(filename_new)
        temp=None
        if data == 1:
            temp='House Exterior'
        if data == 2:
            temp='Living Room'
        if data == 3:
            temp='Bed Room'
        if data == 4:
            temp='Washroom'
        if data == 0:
            temp='Kitchen'
        s_obj=Pre_Image(img_link=f'media/{filename_new}',cat_img=temp)
        s_obj.save()
        return render(request,'result.html',{'data':temp})
    return render(request,'predicate.html')