from playsound import playsound
import numpy as np
import threading
import requests
import imutils
import time
import cv2


url = "http://192.168.0.3:8080/shot.jpg"

'''
color_dict_HSV = {'black': [[180, 255, 30], [0, 0, 0]],
              'white': [[180, 18, 255], [0, 0, 231]],
              'red1': [[180, 255, 255], [159, 50, 70]],
              'red2': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'blue': [[128, 255, 255], [90, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]],
              'purple': [[158, 255, 255], [129, 50, 70]],
              'orange': [[24, 255, 255], [10, 50, 70]],
              'gray': [[180, 18, 230], [0, 0, 40]]}
'''


lb_blue = np.array([90, 50, 70])
lb_gray = np.array([0, 0, 40])
ub_blue = np.array([128, 255, 255])
ub_gray = np.array([180, 18, 230])


dec = ""
run = True



def bg_worker(url,state):
    global lb_blue
    global lb_gray
    global ub_blue
    global ub_gray
    global run 
    
    while run:
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, -1)
        img = imutils.resize(img, width=320, height=240)
        cv2.imshow("Android Video", img)
        if(state == "storm"):
            chk_storm(img,lb_gray,ub_gray)
        else:
            chk_clear(img, lb_blue,ub_blue)
        
        if cv2.waitKey(1) == 27:
            break
 
def chk_storm(img,lb,ub): 
    global dec  
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lb, ub)
    
    if(np.sum(mask == 0) < np.sum(mask == 255) ):
        dec = "STORMY"
   
    elif(np.sum(mask == 255) > 100):
        dec = "CLOUDY BUT OKAY"
        
    cv2.imshow("Android Cam mask", mask)
    
def chk_clear(img,lb,ub):
    global dec   
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lb, ub)
    
    if(np.sum(mask == 0) > np.sum(mask == 255) ):
        dec = "CLOUDY BUT SUNNY"
    else:
        dec = "CLEAR"
   
    cv2.imshow("Android Cam2 mask", mask)
    

def worker():
    global dec
    global run
    
    while run:
        time.sleep(10)
        
        if(dec == "CLEAR"):
            print("CLEAR")
        elif(dec == "CLOUDY BUT SUNNY"):
            print("CLOUDY BUT SUNNY")
        elif(dec == "CLOUDY BUT OKAY"):
            print("CLOUDY AND POSSIBLE RAIN")
        else:
            print("STORMY")
        
        
    

t1 = threading.Thread(target=bg_worker, args=(url,"clear",))
t2 = threading.Thread(target=bg_worker, args=(url,"storm",))
t3 = threading.Thread(target=worker, args=())

t1.start()
t2.start()
t3.start()

cv2.destroyAllWindows()
