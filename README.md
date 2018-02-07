# Save the Clash

[Documentation Link](https://github.com/yashagrawal3/save-the-clash/blob/master/DOCUMENTATION.pdf)

This app was created as a part of the online round of Microsoft Code.Fun.Do 2018

Sight is the by far the most essential of all the sensory abilities. But some less fortunate are not able perviece the joy of sight which leads them to a disarray of uncertainity and unpredictability. Our app **Save the Clash** aims to reduce this gap between the blind via the use of current technology.

We use 2 State of the art Convoluation Nueral Networks ( YOLO and MONODEPTH ) and tackle this problem with a new approach. The app works by sending the images captured from the smartphone of the user to a MiddleMan pc which then transfers the image to the a server with GPU support.
The Speed of processing can vary from machine to machine speeding from 2frames/s to even 1frame/10s for slow CPU computations. The appraoch gave a proficient result of 1frame/2sec on our sytem using GM107GL [Quadro K620] GPU.
The two networks work in harmony and notify the user about an object when it enters in its personal space and also the direction of most probable collision.

## How to setups
1. Install an app that transfer image or video file from your smartphone to your pc(or any hardware able to run a script and providing SCP support).(we used IPWEBCAM for this purpose[https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en]

2. Download the 2 CNN's:-
        1. YOLO object detection net: https://github.com/pjreddie/darknet (download weights for tiny-yolo)
        2. Monodepth image depth detection : https://github.com/mrharicot/monodepth
   follow the instructions in the page to set up the network and store them in the defaults folder.
3. run the command " chmod +x saveTheClash.py
                      while inotifywait -e create ~/path_to_Input_folder; (Input folder is in data folder and stores the incoming data)
                       do ./saveTheClash.py;
                       done;
    this command sets up an watch and process the input image whenit it is recieved.
4. run the file middleMan.py on the device that recieve images from the smartphone
 
Follow the steps and you are good to go.


The app is still far from complete, but we believe that our small step in the direction for the cause can cause major advancement in the future. Please feel free to contribute. 
