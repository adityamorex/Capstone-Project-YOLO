# Capstone Project to demonstrate the usage of DevOps  

# Real-Time Vehicle Counter with Computer Vision  

![car counter](https://github.com/ansh-sharmaa/Car-Counter/assets/126788870/8ed6b35c-2802-4854-8f7b-6747f156d95e)

**Overview**

This project is a real-time vehicle counter that uses computer vision to detect and count vehicles in a video stream. It leverages the YOLO (You Only Look Once) object detection model for vehicle detection and the SORT (Simple Online and Realtime Tracking) algorithm for tracking. The project is designed to count various types of vehicles, including cars, trucks, buses, and motorbikes, and it displays the count in real-time on the video feed.  

## Features  

- **Object Detection:** Utilizes the YOLO model to identify and classify vehicles in a video stream.   
- **Real-Time Tracking:** Employs the SORT algorithm for tracking and maintaining vehicle identity.    
- **Counting Logic:** Accurately counts vehicles that cross a defined point in the video.   
- **Visualization:** Displays the vehicle count in real-time on the video feed.    
- **Customization:** Provides flexibility to adjust detection and tracking parameters.    
- **Performance:** Optimized for real-time processing and accuracy.   

## Prerequisites   

To run this project, you will need the following dependencies:  

- Python 3.x  
- OpenCV  
- NumPy  
- Ultralytics YOLO  
- SORT  
- A pre-trained YOLO model (e.g., YOLOv3) and corresponding configuration files.  
- A video input source (e.g., a video file).  

## Setup  

1. Clone or download this project repository.  
2. Install the required Python libraries and dependencies using pip.  
3. Download the pre-trained YOLO model and configuration files.  
4. Specify the path to the YOLO model, configuration, video source, and other resources in the code.  

## Usage   

1. Run the Python script to start the real-time vehicle counting application.  
2. The application will process the video source, detect and track vehicles, and display the vehicle count in real-time.  
3. You can adjust the parameters, such as confidence thresholds and tracking settings, as needed.  

## Configuration  

- **model:** Specify the path to the pre-trained YOLO model and configuration files.  
- **classNames:** Define the class names for object detection (e.g., "car," "truck," "bus," "motorbike").  
- **mask:** Load a mask image to limit the region of interest (ROI) for vehicle counting.  
- **tracker:** Configure SORT tracking parameters such as maximum age and minimum hits.  
- **limits:** Set the line coordinates for counting vehicles that cross a specific point in the video.  

## Results

- The application will display the video stream with bounding boxes around detected vehicles.  
- The vehicle count will be updated in real-time on the video feed.  
- Vehicle identities will be tracked and displayed.  

## Acknowledgments

- Ultralytics for the YOLO framework.  
- Alex Bewley for the SORT tracking algorithm.  

## License

This project is open-source and available under the MIT License.
