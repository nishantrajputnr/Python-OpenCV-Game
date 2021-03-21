import cv2
import numpy as np
import random

life = 5
cont = 0
ex = 0
score = 0
speed = 5
f_score = open('highscore.txt')
highscore = int(f_score.readlines()[0])
f_score.close()
print(highscore)
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        global i
        global j
        global cont
        if (x >= j-15 and x <= j+15) or (y >= j - 10 and y <= j + 10):
            global score
            if cont == 0:
                score += 5
            cont = 1
            i = 550
def motion():
    global i
    global j
    global score
    global life
    global cont
    global ex
    global speed
    global highscore
    while life >= 1 and ex == 0:
        cont = 0
        prev = score
        key = cv2.waitKey(1)
        if key == 27:
            ex = 1
        decide = random.randint(0, 1)
        random_x = random.randint(150, 500)
        i = 550
        j = random_x
        flag = 0
        if decide == 0:
            while i >= -20 and ex == 0 and cont==0:
                cv2.setMouseCallback('game', click_event)
                img=cv2.imread('bkbk.jpg',1)
                font = cv2. FONT_HERSHEY_COMPLEX_SMALL
                text2 = 'YOUR LIFE-' + str(life)
                text1 = 'PRESS ESC TO EXIT'
                high = 'HIGHEST SCORE-'+str(highscore)
                text = 'YOUR SCORE-' + str(score)
                if cont == 0:
                    circle = cv2.circle(img, (j, i), 20, (0, 69, 255), -1)
                cv2.putText(img, text, (10, 20), font, 1, (0, 255, 255), 2)
                cv2.putText(img,text2,(315,20),font,1,(255,255,255),2)
                cv2.putText(img, high, (550, 20), font, 1, (0, 255, 255), 2)
                cv2.putText(img, text1, (170, 600), font, 2, (255, 255, 255), 2)

                if flag == 0:
                    i = i - speed
                    j += 1
                    flag = 1
                else:
                    flag = 0

                cv2.imshow('game', img)
                com = cv2.waitKey(1)
                if com == 27:
                    ex = 1
        else:
            while i >= -20 and ex == 0 and cont==0:
                cv2.setMouseCallback('game', click_event)
                font = cv2.FONT_HERSHEY_COMPLEX_SMALL
                text = 'YOUR SCORE-' + str(score)
                text2 = 'YOUR LIFE-' + str(life)
                text1 = 'PRESS ESC TO EXIT'
                high = 'HIGHEST SCORE-' + str(highscore)
                img = cv2.imread('bkbk.jpg', 1)
                cv2.putText(img, text, (10, 20), font, 1, (0, 255, 255), 2)
                cv2.putText(img, text2, (315, 20), font, 1, (255, 255, 255), 2)
                cv2.putText(img, high, (550, 20), font, 1, (0, 255, 255), 2)
                cv2.putText(img, text1, (170, 600), font, 2, (255, 255, 255), 2)
                if cont == 0:
                    circle = cv2.circle(img, (j, i), 20, (0, 69, 255), -1)
                if flag == 0:
                    i = i - speed
                    j -= 1
                    flag = 1
                else:
                    flag = 0
                cv2.imshow('game', img)

                com = cv2.waitKey(1)
                if com == 27:
                    ex = 1
        if prev == score:
            life -= 1
        if score > prev and score % 100 == 0:
            speed += 2
        if score > highscore:
            highscore = score

motion()
if score >= highscore:
    f = open('highscore.txt', 'w')
    f.write(str(highscore))
    f.close()
img = cv2.imread('bkbk.jpg', 1)
text = 'GAME OVER'
text1 = 'PRESS ESC TO EXIT'
text2 = 'YOUR SCORE-' + str(score)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img, text, (250, 200), font, 2, (0, 255, 255), 1)
cv2.putText(img, text1, (150, 300), font, 2, (0, 255, 255), 1)
cv2.putText(img, text2, (200, 400), font, 2, (255, 255, 255), 1)
cv2.imshow('game',img)
cv2.waitKey(0)

cv2.destroyAllWindows()