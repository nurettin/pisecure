from os import popen
from os import path

index= 1

while 1:
	popen("fswebcam -r 1024x768 --no-banner cam%d.jpeg" % index)
	if index== 1:
		index= 2
	else:
		index= 1
	if not path.isfile("cam2.jpeg"):
		continue
	str= popen("convert cam1.jpeg cam2.jpeg -compose Difference -composite -colorspace gray -format '%[fx:mean*100]' info:").read()
	diff= float(str)
	print "diff: ", diff
	if diff> 1:
		popen("aplay police_s.wav")

