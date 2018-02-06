"""
This file contains the function to calculate the center of the detected objects
by the YOLO net that enable us to predict the path of collision of the person with 
the incoming object.
"""

import os

def get_coordinates(file):
  with file  as file:
    lines = file.readlines()
  coordinate_map = {}
  for i in range(len(lines)):
    if 'Bounding Box:' in lines[i]:
      item = lines[i-1].split(' ')[0].strip(':')
      coordinate = lines[i].split(' ')
      left = int(coordinate[2].split('=')[1].split(',')[0])
      top = int(coordinate[3].split('=')[1].split(',')[0])
      right = int(coordinate[4].split('=')[1].split(',')[0])
      bottom = int(coordinate[5].split('=')[1].split('\n')[0])

      # Returns center X and Y co-ordinate
      coordinate_map[item]  = [(left+right)/2, (top+bottom)/2]
  return coordinate_map

def objects_path():
	curr_coordinate = {} # dict to hold the center of the objects detected in the present image
	prev_coordinate = {} # dict to hold the center of the objects detected in the previous image
	file1 =  open('./yolo_output.txt','r')
	curr_coordinate = get_coordinates(file1)
	file2 = open('./yolo_output_prev.txt','w+')
	if os.stat('./yolo_output_prev.txt').st_size == 0:
		os.system('cat ./yolo_output.txt>./yolo_output_prev.txt')
	prev_coordinate = get_coordinates(file2)
	os.system('cat ./yolo_output.txt>yolo_output_prev.txt')
	return [curr_coordinate, prev_coordinate]

