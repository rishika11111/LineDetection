import numpy as np
import cv2

gray = cv2.imread(r"img1.jpeg")
edges = cv2.Canny(gray,180,200,apertureSize = 3)
minLineLength=50
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=215, minLineLength=minLineLength)
for line in lines:
   x1, y1, x2, y2 = line[0]
   cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 3)
   #cv2.imshow("linesEdges", edges)
   cv2.imshow("linesDetected", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
