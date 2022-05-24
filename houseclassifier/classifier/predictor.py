import numpy as np
import glob
import cv2
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers, models
from PIL import Image
from .models import PredictedImage


class ImagePredictor:
    def train_model(self):
        object_list = PredictedImage.objects.values('img','category_id')
    
        # filelist = glob.glob('media/dataset/*.jpg')

        x = np.array([np.array(Image.open('media/'+i['img'])) for i in object_list])
        y = np.array([i['category_id'] for i in object_list])


        # resized_x = np.array([cv2.resize(i,(64,64)) for i in x])
        resized_x=[]
        for i in x:
          if len(i.shape) > 2 and i.shape[2] == 4:
            img_array = cv2.cvtColor(i, cv2.COLOR_BGRA2BGR)
            resized_x.append(cv2.resize(img_array,(64,64)))
          else:
            resized_x.append(cv2.resize(i,(64,64)))
        resized_x=np.array(resized_x)


        x_train, x_test, y_train, y_test = train_test_split(resized_x, y, test_size=0.1, random_state=2)

        scaled_x_train = x_train / 255.0 #rescaling
        scaled_x_test = x_test / 255.0

        # data_augmentation = keras.Sequential([
        #         layers.RandomFlip("horizontal",input_shape=(64,64,3)),
        #         layers.RandomRotation(0.1),
        #         layers.RandomZoom(0.1),
        #         ])

        self.cnn = models.Sequential([
                layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'),
                layers.MaxPooling2D((2, 2)),
                
                layers.Conv2D(filters=32, kernel_size=(3, 3), activation='relu'),
                layers.MaxPooling2D((2, 2)),
            
                layers.Dropout(0.2),
                layers.Flatten(),
                layers.Dense(64, activation='relu'),
                layers.Dense(5, activation='softmax')
            ])

        self.cnn.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
        self.cnn.fit(scaled_x_train, y_train, epochs=3)
        # cnn.evaluate(scaled_x_test,y_test)

    def predict_image(self,fname):
        img = glob.glob(f'{fname[1:]}')[0]
        img_array = np.array(Image.open(img))

        if len(img_array.shape) > 2 and img_array.shape[2] == 4:
            #convert the image from RGBA2RGB
            img_array = cv2.cvtColor(img_array, cv2.COLOR_BGRA2BGR)

        resized_img = cv2.resize(img_array,(64,64))
        rescaled_img = resized_img/255.0
        try:
            rescaled_img = rescaled_img.reshape(1,64,64,3)
        except Exception as e:
            print(e,'error on line no 63 in predictor.py')
        predicted = self.cnn.predict(rescaled_img)
        result=np.argmax(predicted)
        return result
            
