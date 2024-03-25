from math import sqrt,pow
import cv2
import mediapipe as mp
import pyautogui as control

#Camera choice
cam = cv2.VideoCapture(0)

#Main Screen(laptop, desktop, etc) Dimensions:
screen_width, screen_height = control.size()

#Result Screen Dims
#Default = (480, 640, 3) = (height, width, dims)
# cam.set(3, 720)
# cam.set(4, 720)
# Lets set the result screen to 1/2 of the main screen:

# cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1000)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 563)

#MediaPipe Tools: 
mp_drawings = mp.solutions.drawing_utils #THis is used to draw the markings on the screen
mp_holistic = mp.solutions.holistic #this are the main for the coordinate detection
mp_hands = mp.solutions.hands.Hands()
#Detections:
#mp_holistic.Hoslistic()

#Main Loop
X,Y ,X2,Y2 = 0,0,0,0 #this is to resolve the error of X not defined, while calculating distance
while True:
    _,frame = cam.read()
    frame = cv2.resize(frame, (1000,563))
    frame = cv2.flip(frame,1) #1 = Y-axis , 0 = X
    frame_height, frame_width, _ = frame.shape #This is to get the main dim of the frame
    rgb_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = mp_hands.process(rgb_frame)
    hand_marks = output.multi_hand_landmarks
    ''' Now inside this hand_marks, you will have each point,21 in total,
    from which our main fingers are:
    Thumb : 4
    Index : 8
    Middle: 12
    Ring  : 16
    Pinky : 20
    
    NOTE: These are the markings of the pin point ends of your fingers.
    for mouse cursor, we are going to use index point = 8
    to get there you have to iterate through you hand_marks
    
    And to mark to them, use the mp_drawing'''
    
    if hand_marks:
        for hand in hand_marks:
            mp_drawings.draw_landmarks(frame,hand)
            
            landmarks = hand.landmark
            for id1,lm in enumerate(landmarks):
                try:
                    if id1 == 8:
                        x = int(lm.x * frame_width)
                        y = int(lm.y * frame_height)
                        # print(id1,x,y)
                        #To draw the coordinates for Index finger id ==8
                        #here we are just highliting the finger with a circle
                        cv2.circle(img=frame, center=(x,y), radius=10, color=(0,255,0))
                        X = (screen_width/frame_width) * x
                        Y = (screen_height/frame_height) * y
                    
                        try:
                            # print(int(X) , int(Y))
                            
                            control.moveTo(int(X),int(Y))

                        except control.FailSafeException as e:
                            print(e)
                            control.PAUSE
                        
                    if id1 == 4:
                        x2 = int(lm.x * frame_width)
                        y2 = int(lm.y * frame_height)
                        # print(id1,x,y)
                        #To draw the coordinates for Index finger id ==8
                        #here we are just highliting the finger with a circle
                        cv2.circle(img=frame, center=(x2,y2), radius=10, color=(0,255,0))
                        X2 = (screen_width/frame_width) * x2
                        Y2 = (screen_height/frame_height) * y2
                    
                        try:
                            distance_btw_thumb_index = int(sqrt(pow((X-X2),2) + pow((Y-Y2),2)))
                            print(distance_btw_thumb_index)
                            if ((distance_btw_thumb_index < 35) and (distance_btw_thumb_index>0)):
                                control.click()
                                control.sleep(1)
                        except Exception as e:
                            print(str(e))
                            print("NOT ABLE TO")
                            control.sleep(1)
                except Exception as e:
                    print(e)
                    exit()

    cv2.imshow('Virtua1 Mouse',frame)
    
    k = cv2.waitKey(1)
    if k == ord('q'):
        cv2.destroyAllWindows()
        break
print(screen_width,screen_height)
print(frame.shape)

