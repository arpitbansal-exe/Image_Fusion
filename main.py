from functions import *
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog

main_window=Tk()
main_window.title("Image Fusion")
main_window.geometry("400x250")

def submit1():
    main_window.filename1 = filedialog.askopenfilename(initialdir="H:\ImageFusion\Images",title="Select the first Image")
    print("****First Image Selected*****")

def submit2():
    main_window.filename2 = filedialog.askopenfilename(initialdir="H:\ImageFusion\Images",title="Select the Second Image")
    print( "*****Second Image Selected****" )

def fusion():
    print("\n\n****Fusing Images!!!****")
    print("Please wait for some time")
    img1_name = main_window.filename1
    img2_name = main_window.filename2

    img1 = cv2.imread(img1_name)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

    img2 = cv2.imread(img2_name)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    # Resizing the images to the same size
    rows, columns = np.shape(img1[:, :, 1])
    if (np.shape(img1) != np.shape(img2)):
        img2 = cv2.resize(img2, (rows, columns))

    Fused = fuse_images(img1, img2)

    fig = plt.figure(figsize=(10,7))

    fig.add_subplot(3,3, 1)
    plt.imshow(img1)
    plt.axis('off')
    plt.title("First Image")

    fig.add_subplot(3,3, 3)
    plt.imshow(img2)
    plt.axis('off')
    plt.title("Second Image")

    fig.add_subplot(3,3,5 )
    plt.imshow(Fused)
    plt.axis('off')
    plt.title("Fused Image")

    plt.show()

    print("*****Images Fused!!!******")
    print("*****Result Displayed****")

l = Label(main_window, text = "Image Fusion\n")
l.config(font =("Italic", 18))
l.pack()
button1 =Button(main_window,text="Select first Image",command=submit1)
button1.config(width=20,height=2)
button1.pack()

button2 =Button(main_window,text="Select Second Image",command=submit2)
button2.config(width=20,height=2)
button2.pack()

button3 =Button(main_window,text="Fuse and Display Images",command=fusion)
button3.config(width=20,height=2)
button3.pack()

exit_button = Button(main_window, text = "Exit",command = main_window.destroy)
exit_button.config(width=20,height=2)
exit_button.pack()

main_window.mainloop()





