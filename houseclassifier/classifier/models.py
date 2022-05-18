from django.db import models


class PredictedImage(models.Model):
    img = models.ImageField(upload_to='predicted_image')
    category_name = models.CharField(max_length=50,null=True)
    category_id = models.IntegerField(null=True)

    def __str__(self):
        return self.category_name