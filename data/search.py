"""
Future implementation of the app that will exponentially decrease the search time 
of the system enabling more handiness to the person.
"""

import subprocess
import os

def initialize:
        search_net = subprocess.Popen('./darknet detector test cfg/voc.data cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights',shell=True, stdin = subprocess.PIPE)
        return search_net

def search:
	search_net = initialize()
	keyword = open('../data/Input/keywords.txt','r').read()
	
	while('search' in keyword):
		search_net.communicate(input = '../data/Input/shot.jpg')
		
