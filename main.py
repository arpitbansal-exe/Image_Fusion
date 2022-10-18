from functions import *

# taking image input from the user
img1_name = input("Enter the name of image 1: ")
img1 = cv2.imread(img1_name)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

img2_name = input("Enter the name of image 2: ")
img2 = cv2.imread(img2_name)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Resizing the images to the same size
rows, columns = np.shape(img1[:, :, 1])

if (np.shape(img1) != np.shape(img2)):
    img2 = cv2.resize(img2, (rows, columns))



# Fused = fuse_images(img1, img2)



# create figure
fig = plt.figure(figsize=(20,20))

# Adds a subplot at the 1st position
fig.add_subplot(3,3, 1)

# showing image
plt.imshow(img1)
plt.axis('off')
plt.title("First")

# Adds a subplot at the 2nd position
fig.add_subplot(3,3, 3)

# showing image
plt.imshow(img2)
plt.axis('off')
plt.title("Second")

fig.add_subplot(3,3,5 )

# showing image
plt.imshow(img2)   # will be replaced with fused image
plt.axis('off')
plt.title("Fused Image")

# final show command
plt.show()
