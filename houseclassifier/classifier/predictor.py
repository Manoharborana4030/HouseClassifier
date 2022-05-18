import numpy as np
import glob
import cv2
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers, models
from PIL import Image


class ImagePredictor:
    def __init__(self):       
        filelist = glob.glob('media/dataset/*.jpg')

        x = np.array([np.array(Image.open(fname)) for fname in filelist])

        y = np.array([int(i.split('_')[0].split('\\')[1]) for i in filelist])

        resized_x = np.array([cv2.resize(i,(64,64)) for i in x])

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
        self.cnn.fit(scaled_x_train, y_train, epochs=2)
        # cnn.evaluate(scaled_x_test,y_test)

    def predict_image(self,fname):
        img = glob.glob(f'{fname[1:]}')[0]
        img_array = np.array(Image.open(img))

        resized_img = cv2.resize(img_array,(64, 64))
        rescaled_img = resized_img/255.0
        rescaled_img = rescaled_img.reshape(1,64,64,3)
        
        predicted = self.cnn.predict(rescaled_img)
        result=np.argmax(predicted)
        return result
            
