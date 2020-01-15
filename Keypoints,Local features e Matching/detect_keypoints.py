import numpy as np
import cv2
nomeJanela="Localizando caderno"
cv2.namedWindow(nomeJanela , cv2.WINDOW_NORMAL)
cv2.resizeWindow(nomeJanela , 1536 , 864)
cap = cv2.VideoCapture('video.mp4')
img2 = cv2.imread('foto.png', cv2.IMREAD_GRAYSCALE) # imagem para aprender
while (1):

    ret, img1 = cap.read()#pega cada frame do video
    img1 = cv2.cvtColor(img1, cv2.cv2.COLOR_BGR2GRAY) 
    
    orb = cv2.ORB_create(1000)

    # encontra as keypoints e descriptors com o orb
    kp1, des1 = orb.detectAndCompute(img1,None) #definição de keypoints e descriptors
    kp2, des2 = orb.detectAndCompute(img2,None)

    # BFMatcher 
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)  #norma de hamming = calculo de distancia, melhor para ORB // # crossCheck = apenas o melhor match.
    matches = bf.match(des1,des2)

    matches = sorted(matches, key = lambda x:x.distance) #ordena matches pela distancia

    # desenha os 10 melhores matches(ordenados).
    img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:30],None,flags=2) 

    cv2.imshow(nomeJanela, img3)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break