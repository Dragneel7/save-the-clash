#!/usr/bin/env python3

import speech_recognition as sr  
import subprocess
import multiprocessing
import time
import urllib
from os import system


# install SpeechRecognisation
# install portaudio
# install pyaudio
# link: https://people.csail.mit.edu/hubert/pyaudio/

# get audio from the microphone
r= sr.Recognizer()

def time_delay():
  for i in range(100):
    print "...."
    time.sleep(1)

def audio_output(output):
   # Do any processing of the output here 
   system('say '+output)
   return

def listen(counter):
  # counter+=1
  with sr.Microphone() as source:
     print("Speak:") 
     r.dynamic_energy_threshold = False
     r.energy_threshold = 300
     audio = r.listen(source,  timeout=5)
  try:
        spoken_string = r.recognize_google(audio)
        print(spoken_string)

        # check for key words
        if 'search' in spoken_string or 'view' in spoken_string:
          # get image from ipweb:
          image = urllib.URLopener()
          image.retrieve("http://172.30.28.124:8080/shot.jpg","./send/shot.jpg")
          print("Saving File .....")
          with open("./send/output_local.txt", "w") as text_file:
              text_file.write(spoken_string)

          print("Sending output file to the server .......")
          subprocess.call(["scp", "-r", "./send", "rajkumar@192.168.173.27:Templates/we-dont-know-da-wae/data/Input"])
          # print("Wait for 3 seconds")
          p = multiprocessing.Process(target=time_delay)
          p.start()
          p.join(5)  # Wait 5 seconds
          # if thread is alive
          if p.is_alive():
             p.terminate()

             print(counter)
             if(counter > -1):
                print("Getting file from the server ........")
                subprocess.call(["scp", "rajkumar@192.168.173.27:~/Templates/we-dont-know-da-wae/data/output.txt",
                                 "./"])
                # read output file
                output = open("output.txt", "r").read()
                print(output)
                if(output != ''):
                   audio_output(output)
             counter+=1
             listen(counter)
        else:
             listen(counter)

  except sr.UnknownValueError:
        print("Could not understand audio")
        # Ask user to speak again
        listen(0)

  except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        # Ask user to speak again
        listen(0)

listen(0)
