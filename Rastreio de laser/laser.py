import cv2   # Biblioteca OpenCV
import numpy as np

#Video = cv2.VideoCapture('VID_20181019_102041.3gp') # Abre o vídeo
#Video = cv2.VideoCapture('VID_20181019_102131.3gp') # Abre o vídeo
#Video = cv2.VideoCapture('VID_20181019_102214.3gp') # Abre o vídeo
#Video = cv2.VideoCapture('laser2.mp4') # Abre o vídeo
Video = cv2.VideoCapture('laser.mp4') # Abre o vídeo

while (True):

    ret, Frame = Video.read() # Pega cada um Frame e verifica. ret -> Valor do frame (True ou False); Frame -> Recebe o próximo frame 

    Frame_HSV = cv2.cvtColor(Frame, cv2.COLOR_BGR2HSV) # Conversão de cor, converte de RGB/BGR para HSV (hue, saturation, value)

    lower_red = np.array([0,0,255]) # Valor de vermelho mais baixo
    upper_red = np.array([10,255,255]) # Valor de vermelho mais alto

    mask = cv2.inRange(Frame_HSV, lower_red, upper_red) # Utilizando masks, Recebe um vetor de dados booleano, (lower_red ou upper_red)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask) # Retorna valores de intensidade máxima e mínima. Gera array de 4 elementos em mask

    cv2.circle(Frame, maxLoc, 20, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('Ponteiro Laser', Frame) # Mostra o vídeo na tela
    Frame = cv2.resize(Frame_HSV, (0,0), fx=0.5, fy=0.5) 

    moments = cv2.moments(mask) # Encontra o centróide do círculo vermelho

    if(int(moments['m00']) > 0):
        x = int(moments['m10'] / moments['m00']) # Calcula as coordenadas do centro em X
        y = int(moments['m01'] / moments['m00']) # Calcula as coordenadas do centro em Y
        print("Posição em X ("+str(x)+") e Posição em Y ("+str(y)+")") # Printa as coordenadas


    if cv2.waitKey(1) & 0xFF == ord('q'): # Mostra o frame por 1ms
       break


FrameVideo.release()
cv2.destroyAllWindows()