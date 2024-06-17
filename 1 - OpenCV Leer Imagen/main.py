import cv2

img = cv2.imread('campus-smp.webp')

# blanco y negro:
img_bn = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('UPCH', img)
# mostrar la imagen:
cv2.imshow('UPCH en BN',img_bn)
cv2.waitKey(0)
