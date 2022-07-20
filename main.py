import cv2
#load images
image= cv2.imread("elfs.jpeg")
watermark= cv2.imread("watermark.png")

print(watermark.shape)

x= image.shape[1] - watermark.shape[1]
y= image.shape[0] - watermark.shape[0]

watermark_place= image[y:, x:]

blend= cv2.addWeighted(watermark_place, 0.5, watermark, 0.5, 0)
#cv2.imwrite("blend.jpeg", blend)

image[y:, x:] = blend
cv2.imwrite("elfs-watermark.jpeg", image)