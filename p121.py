import cv2
import numpy

vid = cv2.VideoCapture(0)
output_vid = cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*"XVID"),20,(640,480))

status = True
for i in range(60):
    r, e = vid.read()
e = numpy.flip(e,axis=-1)
while status:
    ref, ext = vid.read()
    ext = numpy.flip(ext,axis=-1)
    conv = cv2.cvtColor(ext, cv2.COLOR_BGR2HSV)
    lr = numpy.array([0, 120,50])
    ur = numpy.array([10,255,255])
    m1 = cv2.inRange(conv,lr,ur)
    lr1 = numpy.array([170,120,70])
    ur1 = numpy.array([180,255,255])
    m2 = cv2.inRange(conv, lr1, ur1)
    m1 = m1 + m2
    m1 = cv2.morphologyEx(m1,cv2.MORPH_OPEN,numpy.ones((3, 3), numpy.uint8))
    m1 = cv2.morphologyEx(m1,cv2.MORPH_DILATE,numpy.ones((3, 3), numpy.uint8))
    m2 = cv2.bitwise_not(m1)
    r1 = cv2.bitwise_and(conv, conv, mask=m2)
    r2 = cv2.bitwise_and(e, e, mask=m1)
    output = cv2.addWeighted(r1, 1, r2, 1, 0)
    cv2.imshow("out", output)
    cv2.imshow("m1", m1)
    cv2.imshow("m2", m2)
    output_vid.write(output)

    key = cv2.waitKey(25)
    if key == 32:
        status = False
