import cv2
#import time
import pytesseract  
from gtts import gTTS  
from pygame import mixer 
import os 

pytesseract.pytesseract.tessarct_cmd=r"C:\Sumit Purandare\Software\General\Tesseract\tesseract.exe"
mixer.init()
def play(text):
  tts = gTTS(text)
  tts.save("output.mp3")
  mixer.music.load('output.mp3')
  mixer.music.play()
  while mixer.music.get_busy():
      pass
  mixer.music.load('test.mp3')
  os.remove('output.mp3')

cap = cv2.VideoCapture(0)
while 1:
  ret, img = cap.read()
  img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  cv2.imshow("Video",img1)
  text=pytesseract.image_to_string(img1)  
  print(text)
  try:
    play(text)
  except AssertionError:
    pass

  #time.sleep(1)
  if cv2.waitKey(1) == ord("q"):
    break
cap.release()
cv2.destroyAllWindows()



