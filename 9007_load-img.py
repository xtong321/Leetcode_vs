import cv2

inst_labels = [1, 2, 3, 4]
inst_label2 = []
cls_flag = 1
ppp = max(inst_labels) + 1 if len(inst_labels) > 0 else 1
qqq = max(inst_labels) + 1 if len(inst_label2) > 0 else 1
print("ppp = %d" % ppp)
print("qqq = %d" % qqq)


img = cv2.imread(".\lena.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destoryAllWindows()

