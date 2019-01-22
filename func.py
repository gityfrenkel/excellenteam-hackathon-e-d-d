from time import sleep

import cv2

from light_detection import lightDetection

def handle():
   cap = cv2.VideoCapture(0)
   count = 0
   num_after = 0


   while True:
       ret, frame = cap.read()
       num_before = num_after
       num_after = lightDetection(frame)
       count += 1
       
       if num_after - num_before > 4 and count > 5:
           cap.release()
           cv2.destroyAllWindows()
           return ("STRONG LIGHT DETECTED!!!!")

       if cv2.waitKey(1) & 0xFF == ord('q'):
           break

   cap.release()
   cv2.destroyAllWindows()

output = handle()
print(output)