# Save the Clash

Here is the [Documentation Link](https://github.com/yashagrawal3/save-the-clash/blob/master/DOCUMENTATION.pdf) of our app.

This app was created as a part of the online round of Microsoft Code.Fun.Do 2018.

Sight is the by far the most essential of all the sensory abilities. But some less fortunate are not able perviece the joy of sight which leads them to a disarray of uncertainity and unpredictability. Our app **Save the Clash** aims to reduce this gap between the blind via the use of current technology.

We use 2 State of the art Convoluation Nueral Networks (YOLO and MONODEPTH) and tackle this problem with a new approach. The app works by sending the images captured from the smartphone of the user to a MiddleMan pc which then transfers the image to the a server with GPU support.
The Speed of processing can vary from machine to machine speeding from `2frames/sec` to even `1frame/10sec` for slow CPU computations. The approach gave a proficient result of `1frame/2sec` on our sytem using GM107GL [Quadro K620] GPU.
The two networks work in harmony and notify the user about an object when it enters in its personal space and also the direction of most probable collision.

## Setup:
1. Install an app that transfer image or video file from your smartphone to your pc or any hardware able to run a script and providing SCP support. We have used [IPWEBCAM](https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en) for this purpose.

2. Download the two CNNs:
  - [YOLO](https://github.com/pjreddie/darknet) object detection net: Download weights for tiny-yolo.
  - [Monodepth](https://github.com/mrharicot/monodepth) image dept detection.
   follow the instructions in the page to set up the network and store them in the defaults folder.

3. Run the command `chmod +x saveTheClash.py
                      while inotifywait -e create ~/<input_folder_path>;
                       do ./saveTheClash.py;
                       done;`
    this command sets up an watch and process the input image when it it is recieved. Here, The `<input_folder_path>` is in data folder and stores the incoming data from the user.

4. Run the file `middleMan.py` on the device that recieve images from the smartphone
 
Follow the steps and you are good to go.


The app is still far from complete, but we believe that our small step in the direction for the cause can cause major advancement in the future. Please feel free to contribute. 
