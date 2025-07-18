try:
    import cv2
    import mediapipe as mp
    import pyautogui as pag
    import math
except:
    print(0)

x1 = y1 = x2 = y2 =0
hc = mp.solutions.hands.Hands()
du = mp.solutions.drawing_utils
webcam = cv2.VideoCapture(0)

while True:
    _ , rec = webcam.read()
    fw,fh,_ = rec.shape
    rgv_cv = cv2.cvtColor(rec , cv2.COLOR_BGR2RGB)
    op = hc.process(rgv_cv)
    hands = op.multi_hand_landmarks
    if hands:
        for hand in hands:
            du.draw_landmarks(rec , hand)
            lm = hand.landmark
            for id,lnd in enumerate(lm):
                x,y = int (lnd.x*fh) , int (lnd.y*fw)
                if id == 8:
                    cv2.circle(img = rec,center = (x,y),radius = 8, color = (0,255,255),thickness=3)
                    x1 = x
                    y1 = y
                if id == 4:
                    cv2.circle(img = rec,center = (x,y),radius = 8, color = (0,0,255),thickness = 3)
                    x2 = x
                    y2 = y
                dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
                cv2.line(rec , (x1,y1),(x2,y2),(0,255,0),5 )

                if dist >50:
                    pag.press('volumeup')
                else:
                    pag.press('volumedown')

    cv2.imshow("Gesture Based volume control system",rec)
    wkey = cv2.waitKey(10)
    if wkey ==27:
        break
webcam.release()
cv2.destroyAllWindows()
