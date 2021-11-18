import cv2
import matplotlib.pyplot as plt

image1 = cv2.imread('.\images\cat-01.jpg')
image2 = image1.astype(np.uint16)
b, g, r = cv2.split(image2)
gray1 = ((b+g+r)/3).astype(np.uint8)


gray2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

image1 = image1[:,:,::-1]

image2 = np.zeros((gray1.shape[0], gray1.shape[1], 3), dtype=np.uint8)
image2[:,:,0] = gray1
image2[:,:,1] = gray1
image2[:,:,2] = gray1

image2 = np.zeros((gray1.shape[0], gray1.shape[1], 3), dtype=np.uint8)
image2[:,:,0] = gray1
image2[:,:,1] = gray1
image2[:,:,2] = gray1

image3 = np.expand_dims(gray2, axis=-1) * np.ones((1,1,3))
image3 = image3.astype(np.uint8)

fig, axes = plt.subplots(1, 3, dpi=150)

for i, image in enumerate([image1, image2, image3]):
    axes[i].imshow(image)
    axes[i].axis('off')

fig.tight_layout()
plt.show()