import glob,os

filelist = glob.glob('kk/*.jpg')
number = 294
for i in filelist:
	os.rename(i,f'DS/bedroom/bedroom_{number}.jpg')
	number+=1
print(number)