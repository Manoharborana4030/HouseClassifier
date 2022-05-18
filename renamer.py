import glob,os

filelist = glob.glob('dataset/washroom/*.jpg')
number = 785
for i in filelist:
	os.rename(i,f'washroom/4_img_{number}.jpg')
	number+=1
print(number)