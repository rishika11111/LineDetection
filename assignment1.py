import numpy as np
import cv2

gray = cv2.imread(r"img1.jpeg")
edges = cv2.Canny(gray,180,200,apertureSize = 3)
minLineLength=50
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=215, minLineLength=minLineLength)
c=0
x11,y11=0,0
print(lines.shape, len(lines))
print(lines)
for i in range(len(lines)-1):
    x1, y1, x2, y2 = lines[i][0]
    print(x1,y1)
    #Checking for horizontal line. Here, we focus on vertical lines.
    if(x1!=x2):
        cv2.line(gray, (x1, y1), (x2, y2), (0, 255, 0), 2)
        continue
    #Removing two edges of vertical line.
    else:
        diff=abs(y1-y2)
        for j in range(i+1,len(lines)):
            print(j)
            x, y, _, _ = lines[j][0]
            print(x,y)
            if(abs(x1-x)<diff):
                diff = abs(x1-x)
                ind = j
                x11= x
                y11= y
        x1=(x1+x11)//2
        lines[ind][0] = -1
        lines[i][0] = -1
        if(x1>0 and y1>0 and y2>0):
            c+=1
        cv2.line(gray, (x1, y1), (x1, y2), (0, 255, 0), 2)
cv2.imshow("linesDetected", gray)
print(lines)
print(c)
cv2.waitKey(0)
cv2.destroyAllWindows()
