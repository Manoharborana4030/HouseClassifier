from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .predictor import ImagePredictor
from .models import *
from PIL import Image
import glob


img_predictor = ImagePredictor()
category_list = ['kitchen','exterior','living room','bedroom','washroom']


def index(request):
    return render(request,'index.html')

def category(request):
    return render(request,'category.html')

def predict(request):
    if request.method=='POST':
        file_name=request.FILES['file']
        img_obj = PredictedImage(img=file_name)
        img_obj.save()
        
        model_response=img_predictor.predict_image(img_obj.img.url)
        category_name = category_list[model_response]
        category_id = model_response

        img_obj_up = PredictedImage.objects.filter(id=img_obj.id)\
        .update(category_name=category_name,category_id=category_id)

        return render(request,'result.html',{'result':category_name})
    return render(request,'predict.html')