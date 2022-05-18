from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .predictor import ImagePredictor
from .models import *
from PIL import Image
import threading

#clear unnecessory images
noise = PredictedImage.objects.filter(category_name=None)
noise.delete()

#create instance of ML model
img_predictor = ImagePredictor()
img_predictor.train_model()

category_list = ['kitchen','exterior','living room','bedroom','washroom']


def index(request):
    return render(request,'index.html')

def category(request,category=None):
    if category is not None:
        image_list = PredictedImage.objects.filter(category_name=category).order_by('-id')
        return render(request, 'category.html', {'image_list':image_list,'category':category})
    return render(request,'category.html',{'category':category})

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

        # t = threading.Thread(target=img_predictor.train_model())
        # t.start()
        result_list = PredictedImage.objects.filter(id__in=img_id_list)
        return render(request,'result.html',{'result_list':result_list})    

    return render(request,'predict.html')