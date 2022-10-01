
from tkinter import *
from tkinter.ttk import *
from PIL import ImageGrab


class main:
    def __init__(self):
        self.res = ""
        self.pre = [None, None]
        self.bs = 6.0

        self.root = Tk()
        self.root.title("Bangla Handwriting Math Solver")
        self.root.resizable(False, False)

        # self.root size we want to create
        self.root_height = 600
        self.root_width = 1024

        # getting the full screen height and width
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # calculating the geometry padding
        x_cordinate = int((screen_width/2) - (self.root_width/2))
        y_cordinate = int((screen_height/2) - (self.root_height/2))

        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))

        self.c = Canvas(self.root, bd=3, relief="ridge", bg='white', height=self.root_height - 150, width=self.root_width - 52)
        self.c.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
 
        # Create label
        label = Label(self.root, text = "Draw your mathematical term here...👆👆", )
        label.config(font =("Courier", 14))
        label.grid(row=1, column=0, columnspan=3)

        # Create label blank for spacing
        space = Label(self.root, text = "", )
        space.config(font =("Courier", 14))
        space.grid(row=2, column=0, columnspan=3)

        style = Style()

        style.configure('E.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'red')
        style.configure('C.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'blue')
        style.configure('S.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'green')
        
        ''' Button 1: Exit'''
        exit_btn = Button(self.root, text = 'Quit !', style = 'E.TButton', command = self.close)
        exit_btn.grid(row = 3, column = 0)

        ''' Button 2: Clear'''
        calculate_btn = Button(self.root, text = 'Clear', style = 'C.TButton', command = self.clear)
        calculate_btn.grid(row = 3, column = 1)

        ''' Button 3: Solve'''
        exit_btn = Button(self.root, text = 'Solve', style = 'S.TButton', command = self.solve)
        exit_btn.grid(row = 3, column = 2)

        self.c.bind("<Button-1>", self.putPoint)
        # self.c.bind("<ButtonRelease-1>", self.getResult)
        self.c.bind("<B1-Motion>", self.paint)

        self.root.mainloop()
    
    # Function for closing window
    def close(self):
        self.root.destroy()

    # Function for clearing the canvas
    def clear(self):
        self.c.delete("all")

    # Function for putting a point on the canvas
    def putPoint(self, e):
        self.c.create_oval(e.x - self.bs, e.y - self.bs, e.x + self.bs, e.y + self.bs, outline='black', fill='black')
        self.pre = [e.x, e.y]

    # Function for drawing on the canvas
    def paint(self, e):
        self.c.create_line(self.pre[0], self.pre[1], e.x, e.y, width=self.bs * 2, fill='black', capstyle=ROUND, smooth=TRUE)
        self.pre = [e.x, e.y]

    # Function for solving the equation
    def solve(self):
        print('Solving the equation...')
        self.get_image()

    # Function for getting the image from the canvas
    def get_image(self):
        print('Processing image from the canvas...')
        x = self.root.winfo_rootx() + self.c.winfo_x()
        y = self.root.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        print("x: ", x, "y: ", y, "x1: ", x1, "y1: ", y1)
        print("Croped window width: ", x1 - x, "and Croped window height: ", y1 - y)
        img = ImageGrab.grab()
        img.save("full-screen.png")
        img = img.crop((x, y, x1, y1))
        img.save("drawn-image.png")
        print('Image saved!')

    # Function for solving the prediction
    def get_prediction(self):
        pass

    # def getResult(self, e):
    #     x = self.master.winfo_rootx() + self.c.winfo_x()
    #     y = self.master.winfo_rooty() + self.c.winfo_y()
    #     x1 = x + self.c.winfo_width()
    #     y1 = y + self.c.winfo_height()
    #     img = PIL.ImageGrab.grab()
    #     img = img.crop((x, y, x1, y1))
    #     img.save("icon.png")
    #     imgPath = "icon.png"
    #     model = load_model('bangla_digit_model.h5')
    #     img = cv2.imread(imgPath)
    #     img = np.asarray(img)
    #     img = cv2.resize(img, (32, 32))
    #     img = preprocessing(img)
    #     img = img.reshape(1, 32, 32, 1)
    #     prediction = model.predict(img)

    #     # predict_x = model.predict(img)
    #     # classes_x = np.argmax(predict_x, axis=1)

    #     predict_x = model.predict(img)
    #     classes_x = np.argmax(predict_x, axis=1)
    #     print("predict_x", predict_x)
    #     print("classes_x", classes_x)

    #     classIndex = model.predict_classes(img)
    #     self.res = str(get_className(classIndex))
    #     self.pr['text'] = "Prediction: " + self.res

# Running the main class
if __name__ == "__main__":
    main()

# import tkinter as tk

# win = tk.Tk()  # Creating instance of Tk class
# win.title("Centering self.roots")
# win.resizable(False, False)  # This code helps to disable self.roots from resizing



# screen_width = win.winfo_screenwidth()
# screen_height = win.winfo_screenheight()

# x_cordinate = int((screen_width/2) - (self.root_width/2))
# y_cordinate = int((screen_height/2) - (self.root_height/2))

# win.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, x_cordinate, y_cordinate))

# win.mainloop()

# class main:
#     def __init__(self, master):
#         self.master = master
#         self.res = ""
#         self.pre = [None, None]
#         self.bs = 8.5
#         self.c = Canvas(self.master, bd=3, relief="ridge",bg='white')
#         self.c.pack(side=LEFT)
#         f1 = Frame(self.master, padx=5, pady=5)
#         Label(f1, text="Bangla HandWriting Digit Classification",
#               fg="green", font=("", 15, "bold")).pack(pady=10)
#         Label(f1, text="Using Python and Keras, Tensorflow",
#               fg="green", font=("", 15)).pack()
#         Label(f1, text="Draw On The Canvas Alongside",
#               fg="green", font=("", 15)).pack()
#         self.pr = Label(f1, text="Prediction: None",
#                         fg="blue", font=("", 20, "bold"))
#         self.pr.pack(pady=20)

#         Button(f1, font=("", 15), fg="white", bg="red",
#                text="Clear Canvas", command=self.clear).pack(side=BOTTOM)

#         f1.pack(side=RIGHT, fill=Y)
#         # self.c.bind("<Button-1>", self.putPoint)
#         # self.c.bind("<ButtonRelease-1>", self.getResult)
#         # self.c.bind("<B1-Motion>", self.paint)

#     # def getResult(self, e):
#     #     x = self.master.winfo_rootx() + self.c.winfo_x()
#     #     y = self.master.winfo_rooty() + self.c.winfo_y()
#     #     x1 = x + self.c.winfo_width()
#     #     y1 = y + self.c.winfo_height()
#     #     img = PIL.ImageGrab.grab()
#     #     img = img.crop((x, y, x1, y1))
#     #     img.save("icon.png")
#     #     imgPath = "icon.png"
#     #     model = load_model('bangla_digit_model.h5')
#     #     img = cv2.imread(imgPath)
#     #     img = np.asarray(img)
#     #     img = cv2.resize(img, (32, 32))
#     #     img = preprocessing(img)
#     #     img = img.reshape(1, 32, 32, 1)
#     #     prediction = model.predict(img)

#     #     # predict_x = model.predict(img)
#     #     # classes_x = np.argmax(predict_x, axis=1)

#     #     predict_x = model.predict(img)
#     #     classes_x = np.argmax(predict_x, axis=1)
#     #     print("predict_x", predict_x)
#     #     print("classes_x", classes_x)

#     #     classIndex = model.predict_classes(img)
#     #     self.res = str(get_className(classIndex))
#     #     self.pr['text'] = "Prediction: " + self.res

#     def clear(self):
#         self.c.delete('all')

#     def putPoint(self, e):
#         self.c.create_oval(e.x - self.bs, e.y - self.bs, e.x +
#                            self.bs, e.y + self.bs, outline='black', fill='black')
#         self.pre = [e.x, e.y]

#     def paint(self, e):
#         self.c.create_line(self.pre[0], self.pre[1], e.x, e.y,
#                            width=self.bs * 2, fill='black', capstyle=ROUND, smooth=TRUE)

#         self.pre = [e.x, e.y]


# if __name__ == "__main__":
#     root = Tk()
#     main(root)
#     root.title('Digit Classifier')
#     root.resizable(0, 0)
#     root.mainloop()