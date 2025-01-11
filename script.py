import cv2

# loading my image copy
image = cv2.imread('assignment-001-given.png')

# draw a green rectangle
cv2.rectangle(image,(130,96),(489,459),(0,255,0),3)
"""
adding semi transparent black background
for that we have to make an overlay picture with that background triangle
and try to blend the overlay with the resied picture
"""
overlay = image.copy()
opacity = 0.5
cv2.rectangle(overlay,(388,45),(603,87),(0,0,0),-1)
cv2.addWeighted(overlay,opacity,image,1-opacity,0,image)
#writing plate number on image
cv2.putText(image,'RAH972U',(390,85),cv2.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0),2)

# displaying image
cv2.imshow('picture',image)
# Wait indefinitely until a key is pressed
cv2.waitKey(0)
#saving image
cv2.imwrite('assignment-001-result.png',image)
# we are closing opened windows
cv2.destroyAllWindows()