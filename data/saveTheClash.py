#!/usr/bin/env python
from get_coordinates import * # use to get center coordinates of detected image
import os
import subprocess
import numpy
import logging
#import matplotlib.pyplot as plt
from PIL import Image 

"""
file contains the function for the search and view mode.
"""

def saveTheClash():
	#load the keyword
	keyword = open('./Input/send/output_local.txt', 'r').read() # decides the function to be executed
	print(keyword)
	if 'search' in keyword:
		# (bash script to run the YOLO >> objects_detected.txt)
                os.chdir('../defaults/darknet')
		# process the file here and generate the string
                os.system("./darknet detector test cfg/voc.data cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights ~/Templates/we-dont-know-da-wae/data/Input/send/shot.jpg >../../data/yolo_output.txt")
                os.chdir('../../data/')
		output = "is in front of you! "
		yolo_output = open('./yolo_output.txt','r').read()
                print(yolo_output)
		keywords = set(keyword.split())
		for i in keywords:
	          if i in yolo_output:
			output = i + " " + output
			file1 = open("./output.txt", "w")
			file1.write(output) 
		os.system('rm -r ./Input/send')
		# use scp to send a txt file to the intermediate and convert it to speech

	elif 'view' in keyword:
		# (bash script to run stereoCNN)
		detected_objects = []
		hue = [[255, 234, 49], [112, 55, 168]] # will be an array of pixels
		os.chdir('../defaults/darknet')

                os.system("./darknet detector test cfg/voc.data cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights ~/Templates/we-dont-know-da-wae/data/Input/send/shot.jpg >../../data/yolo_output.txt")

		os.chdir('../../data')
		os.chdir('../defaults/monodepth')

		subprocess.call('python monodepth_simple.py --image_path ~/Templates/we-dont-know-da-wae/data/Input/send/shot.jpg --checkpoint_path ~/Templates/we-dont-know-da-wae/defaults/monodepth/models/model_cityscapes',shell=True)
		os.chdir('../../data')

		stereo_image = Image.open('./Input/send/shot_disp.png')
		stereo_image = stereo_image.load()
		curr_coordinates, prev_coordinates = objects_path()

		output = ""
		for key in curr_coordinates.keys():
			print(curr_coordinates[key][0])
                        stereo_coordinates = stereo_image[curr_coordinates[key][0], curr_coordinates[key][1]][:3]
			print(stereo_coordinates)
			if stereo_coordinates[0] <= hue[0][0] and stereo_coordinates[0] >= hue[1][0] and  \
                           stereo_coordinates[1] >= hue[1][1] and stereo_coordinates[1] <= hue[0][1] and  \
                           stereo_coordinates[2] <= hue[1][2] and stereo_coordinates[2] >= hue[0][2]:     
				if key in prev_coordinates.keys():
					if(curr_coordinates[key][0]-prev_coordinates[key][0] > 0):
						output = output + " " + key + " approaching you from left"
					elif(curr_coordinates[key][0]-prev_coordinates[key][0] < 0):
						output = output + " " + key + " approaching you from right"
					else:
						output = output + " " + key + " approaching you head on"
                                else:
                                        output = output + " " + key + " is approaching you."
		file1 = open("./output.txt","w")
                print(output)
		file1.write(output)
 		os.system('rm -r ./Input/send')

	elif keyword == 'view_disabled' :
		pass 


saveTheClash()
