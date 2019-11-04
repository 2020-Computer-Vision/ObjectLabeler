import time
import cv2
import mss
import numpy


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 40, 'left': 0, 'width': 800, 'height': 640}

    while 'Screen capturing':
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(sct.monitors[0]))
        # Displaying window too large on my computer - jacob
        
        # feed image into model

        # retrieve model output (bounding boxes)

        # Draw rectangles over mobs
        cv2.rectangle(img, (100,100),(200,200),(255,0,0),2)

        # Display the picture
        cv2.imshow('Minecraft YOLO', img)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        # cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        #print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
