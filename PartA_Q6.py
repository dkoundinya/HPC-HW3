# Part A Question 6
import cv2 
# Read the image. 
img = cv2.imread('image.jpg') 
winname='unfiltered image'
cv2.imshow(winname,img)
cv2.waitKey(0)
# Apply bilateral filter
bilateral = cv2.bilateralFilter(img,15,80,80)
winname='filtered image'
cv2.imshow(winname,bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()
# Save the output. 
cv2.imwrite('bilateral.jpg', bilateral) 