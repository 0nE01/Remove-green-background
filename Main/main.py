# Moduls
import cv2 as cv
import numpy as np

def remove_green_background_image(image_path: str, save_name: str) :
    image = cv.imread(f'{image_path}')
    # Converting image to hsv image
    hsv_image = cv.cvtColor(image,cv.COLOR_BGR2HSV)
    # Creating green mask.
    lowerb_green = np.array([25, 52, 72], np.uint8) 
    upperb_green = np.array([102, 255, 255], np.uint8)
    green_mask = cv.inRange(hsv_image, lowerb_green, upperb_green) 
    # Using green mask to detect green background in images.
    green_only_image = cv.bitwise_and(image,image,mask=green_mask)
    # Removing green background.
    final_image = image - green_only_image
    # saving the final image.
    cv.imwrite(save_name,final_image)
   
def remove_green_background_video(video_path: str, save_name: str) :
    cap = cv.VideoCapture(f'{video_path}')
    # Creating green mask.
    lowerb_green = np.array([25, 52, 72], np.uint8) 
    upperb_green = np.array([102, 255, 255], np.uint8)
    # Geting size of video for saving vidoe.
    frame_width = int(cap.get(3)) 
    frame_height = int(cap.get(4)) 
    size = (frame_width, frame_height) 
    # Creating a VideoWriter object for saving vidoe.
    result = cv.VideoWriter(save_name,  
                            cv.VideoWriter_fourcc(*'MJPG'), 
                            10, size) 
    while True:
        ret,frame = cap.read()
        if ret == False: 
            break 
        # Converting frame to hsv frames.
        hsv_farme = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        # Creating green mask.
        green_mask = cv.inRange(hsv_farme, lowerb_green, upperb_green) 
        # Using green mask to detect green background in frames.
        green_only_farme = cv.bitwise_and(frame,frame,mask=green_mask)   
         # Removing green background.
        final_frame = frame - green_only_farme 
        # saving the final every frame for final vidoe.
        result.write(final_frame)
        # Press q for quit the app.
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()