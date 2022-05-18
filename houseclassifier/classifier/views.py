from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .predictor import ImagePredictor
from .models import *
from PIL import Image
import glob

#clear unnecessory images
noise = PredictedImage.objects.filter(category_name=None)
noise.delete()

#create instance of ML model
img_predictor = ImagePredictor()

category_list = ['kitchen','exterior','living room','bedroom','washroom']


def index(request):
    return render(request,'index.html')

def category(request):
    return render(request,'category.html')

def result(request):
    return render(request,'result.html')

def predict(request):
    if request.method=='POST':
        file_list=request.FILES.getlist('images')
        
        img_id_list = list()
        for file in file_list:
            img_obj = PredictedImage(img=file)
            img_obj.save()

            model_response=img_predictor.predict_image(img_obj.img.url)
            category_name = category_list[model_response]
            category_id = model_response

            PredictedImage.objects.filter(id=img_obj.id)\
            .update(category_name=category_name,category_id=category_id)

            img_id_list.append(img_obj.id)

        result_list = PredictedImage.objects.filter(id__in=img_id_list)

        return render(request,'result.html',{'result_list':result_list})
    return render(request,'predict.html')