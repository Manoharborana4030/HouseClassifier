import threading
from .models import *
from .predictor import ImagePredictor

class TrainModelThread(threading.Thread):
	def run(self):
		try:
			print('Thread execution started')
			#create instance of ML model
			img_predictor = ImagePredictor()
			img_predictor.train_model()
			print('Thread execution finished')

		except Exception as e:
			print(e,'error')


