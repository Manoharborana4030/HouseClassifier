from django.db import models

class Pre_Image(models.Model):
    img_link=models.CharField(max_length=500)
    cat_img=models.CharField(max_length=100)

    def __str__(self):
        return self.cat_img
