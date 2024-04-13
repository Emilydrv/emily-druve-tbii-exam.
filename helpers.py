from PIL import Image,ImageTk
import tkinter as tk

screen_height = 750
screen_width = 420

def set_background(root, image_file_path):
    """
    This function was inspired by Robin Paul and sets the background image.

    You need to specify the variable that creates the gui frame and the file path of the image.
    """


    img = Image.open(image_file_path)
    img = img.resize((screen_width, screen_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0,)


def clear_widgets(root):
    # This function is used everytime a new page is launched to clear everything from the previous page.

    for i in root.winfo_children():
        i.destroy()


def resizing_images(root,
           background_image_path,
           second_image_path,
           screen_width,
           screen_height,
           resized_width,
           resized_height,
           x_pos,
           y_pos
           ):
    """
    The Function we put together in class to resize images on top of other images to use brackground images in combination with other images.
    """
    global pic, f1

    f1 = tk.Frame(root)

    img1 = Image.open(background_image_path)
    img1 = img1.resize((screen_width, screen_height), Image.LANCZOS)

    img2 = Image.open(second_image_path)
    img2 = img2.resize((resized_width, resized_height), Image.LANCZOS)

    img1.paste(img2, (x_pos, y_pos))

    pic = ImageTk.PhotoImage(img1)
    Lab = tk.Label(f1, image=pic)
    Lab.pack()
    f1.pack()

