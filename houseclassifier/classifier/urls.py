"""houseclassifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from classifier import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('category/<str:category>',views.category,name='category'),
    path('predict',views.predict,name='predict'),
    path('result',views.result,name='result'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('move/<str:cat_id>',views.move,name='move'),
    path('delete_result/<str:id_idslug>',views.delete_result,name='delete_result'),
    path('move_result/<str:cat_id_idslug>',views.move_result,name='move_result'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
