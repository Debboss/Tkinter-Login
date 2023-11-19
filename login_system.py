from tkinter import *
from PIL import Image, ImageTk

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")

        # Load the image using PIL
        self.bg = Image.open("image.jpg")
        self.bg = ImageTk.PhotoImage(self.bg)

        # Create a Label with the image
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

root = Tk()
obj = Login(root)
root.mainloop()
