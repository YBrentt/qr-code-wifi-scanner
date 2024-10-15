import cv2
import numpy as np
from pyzbar.pyzbar import decode
import webbrowser

cap = cv2.VideoCapture(0)

while True:
 ret, frame = cap.read()
 if not ret:
  break
 
 decoded_object = decode(frame)
 for obj in decoded_object:
  data = obj.data.decode('utf-8')
  print(f'detected qr code: {data}')
  
  if "WIFI:" in data:
   webbrowser.open(data)
   
  points = obj.polygon
  if len(points) == 4:
   cv2.polylines(frame, [np.array(points)], isClosed=True, color=(0, 255, 0), thickness=2)
  
 cv2.imshow('qr code scanner', frame)
 if cv2.waitKey(1) & 0xFF == ord('q'):
  break
 
cap.release()
cv2.destroyAllWindows()