from tkinter import filedialog
from keras.models import load_model
from tkinter import *
from tkinter.ttk import *
from PIL import ImageGrab, Image, ImageTk
import cv2
import imutils
from imutils.contours import sort_contours
import numpy as np
import matplotlib.pyplot as plt
import os

class main:
    def __init__(self):
        self.res = ""
        self.pre = [None, None]
        self.bs = 5.0
        self.pick_image_path = None

        self.root = Tk()
        self.root.title("Bangla Handwriting Math Solver")
        self.root.resizable(False, False)
        # self.root.overrideredirect(True) # turns off title bar

        # self.root size we want to create
        self.root_height = 600
        self.root_width = 1024

        # getting the full screen height and width
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # calculating the geometry padding
        self.x_cordinate = int((screen_width/2) - (self.root_width/2))
        self.y_cordinate = int((screen_height/2) - (self.root_height/2))

        # canvas size 
        self.canvas_width = self.root_width - 52
        self.canvas_height = self.root_height - 150


        self.show_image_or_canvas()

        # Create label
        self.label = Label(self.root, text = "Pick a image or Draw your mathematical term here...👆👇", )
        self.label.config(font =("Courier", 14), justify=CENTER)
        self.label.grid(row=1, column=0, columnspan=4)

        # Create label blank for spacing
        space = Label(self.root, text = "", )
        space.config(font =("Courier", 14))
        space.grid(row=2, column=0, columnspan=4)

        style = Style()
        
        ''' Button 1: Exit'''
        style.configure('E.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'red')
        exit_btn = Button(self.root, text = 'Quit !', style = 'E.TButton', command = self.close)
        exit_btn.grid(row = 3, column = 0)

        ''' Button 2: Clear'''
        style.configure('C.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'blue')
        calculate_btn = Button(self.root, text = 'Clear', style = 'C.TButton', command = self.clear)
        calculate_btn.grid(row = 3, column = 1)

        ''' Button 3: Solve'''
        style.configure('S.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'green')
        exit_btn = Button(self.root, text = 'Solve', style = 'S.TButton', command = self.solve)
        exit_btn.grid(row = 3, column = 2)

        ''' Button 4: Solve'''
        style.configure('B.TButton', font = ('calibri', 15, 'bold', 'underline'), foreground = 'green')
        exit_btn = Button(self.root, text = 'Browse Image', style = 'B.TButton', command = self.browse)
        exit_btn.grid(row = 3, column = 3)

        self.root.mainloop()

    # Funtion for showing image or canvas
    def show_image_or_canvas(self):
        if self.pick_image_path is None:
            print('Showing canvas...')
            self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, self.x_cordinate, self.y_cordinate))
            self.c = Canvas(self.root, bd=3, relief="ridge", bg='white', height=self.canvas_height, width=self.canvas_width)
            self.c.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

            self.c.bind("<Button-1>", self.putPoint)
            # self.c.bind("<ButtonRelease-1>", self.getResult)
            self.c.bind("<B1-Motion>", self.paint)
            pass

        else:
            print('Showing image...')
            img = Image.open(self.pick_image_path)
            img = img.resize((self.canvas_width, self.canvas_height))
            img = ImageTk.PhotoImage(img)
            self.canvas_img = Label(self.root)
            self.canvas_img.configure(image=img)
            self.canvas_img.image = img
            self.canvas_img.grid(row=0, column=0, columnspan=4, padx=20, pady=10)
            pass
    
    # Function for browsing image
    def browse(self):
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select Image", filetypes = (("jpg files","*.jpg"),("jpeg files","*.jpeg"),("png files","*.png"),("all files","*.*")))
        print('Browsed Image: ', fln)
        self.pick_image_path = fln
        self.show_image_or_canvas()
        self.get_equation_and_solve(self.pick_image_path)

    # Function for closing window
    def close(self):
        self.root.destroy()

    # Function for clearing the canvas
    def clear(self):
        self.label['text'] = "Pick a image or Draw your mathematical term here...👆👇"
        if self.pick_image_path is not None:
            self.pick_image_path = None
            self.show_image_or_canvas()
        else:
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
        self.label['text'] = 'Solving the equation...' 

        success = self.get_image()
        if success:
            self.get_equation_and_solve("output/2_drawn-image.png")

    # Function for getting the image from the canvas
    def get_image(self):
        print('Processing image from the canvas...')
        self.label['text'] = 'Processing image from the canvas...'
        #
        x, y = (self.c.winfo_rootx(), self.c.winfo_rooty())
        width, height = (self.c.winfo_width(), self.c.winfo_height())
        a, b, c, d = (x, y, x+width, y+height)
        #
        img = ImageGrab.grab()
        img.save("output/1_full-screen.png")
        img = img.crop((a + 76, b + 48, c + 313, d + 154))
        img.save("output/2_drawn-image.png")
        print('Image saved!')
        self.label['text'] = 'Image saved!'
        return True

    # Function for solving the prediction
    def get_equation_and_solve(self, path):
        print('Solving the equation...')
        self.label['text'] = 'Solving the equation...'
        model = load_model('math_symbol_and_digit_recognition.h5')
        chars = []
        
        img = cv2.imread(path)

        ##### removing noise #####
        # convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # blur
        blur = cv2.GaussianBlur(gray, (0,0), sigmaX=33, sigmaY=33)
        # divide
        divide = cv2.divide(gray, blur, scale=255)
        # otsu threshold
        thresh = cv2.threshold(divide, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
        # apply morphology
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
        # write result to disk
        cv2.imwrite("output/3_gray_noise_remove.jpg", gray)
        cv2.imwrite("output/4_blur_noise_remove.jpg", blur)
        cv2.imwrite("output/5_divide_noise_remove.jpg", divide)
        cv2.imwrite("output/6_thresh_noise_remove.jpg", thresh)
        cv2.imwrite("output/7_morph_noise_remove.jpg", morph)

        
        img = cv2.imread("output/6_thresh_noise_remove.jpg")
        # img = cv2.imread("output/7_morph_noise_remove.jpg")

        img = cv2.resize(img, (self.canvas_width, self.canvas_height))
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edged = cv2.Canny(img_gray, 30, 150)
        cv2.imwrite("output/8_all_canny_detect.jpg", edged)
        contours = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        print('Number of contours found: ', len(contours))
        contours = sort_contours(contours, method="left-to-right")[0]
        labels = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'add', 'div', 'mul', 'sub']

        for i, c in enumerate(contours):
            print('Processing the image...: ', str(i+1))
            (x, y, w, h) = cv2.boundingRect(c)
            print('x: ', x, 'y: ', y, 'w: ', w, 'h: ', h)
            if x > 0 and y > 0 and w > 20:  # cheaking weather any garbage value detecting
                roi = img_gray[y:y+h, x:x+w]
                thresh = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                (th, tw) = thresh.shape
                if tw > th:
                    thresh = imutils.resize(thresh, width=32)
                if th > tw:
                    thresh = imutils.resize(thresh, height=32)
                (th, tw) = thresh.shape
                dx = int(max(0, 32 - tw)/2.0)
                dy = int(max(0, 32 - th) / 2.0)
                padded = cv2.copyMakeBorder(thresh, top=dy, bottom=dy, left=dx, right=dx, borderType=cv2.BORDER_CONSTANT, value=(0, 0, 0))
                padded = cv2.resize(padded, (32, 32))
                padded = np.array(padded)
                padded = padded/255.
                padded = np.expand_dims(padded, axis=0)
                padded = np.expand_dims(padded, axis=-1)
                pred = model.predict(padded)
                pred = np.argmax(pred, axis=1)
                label = labels[pred[0]]
                print('>>>>The {} no word is : {}'.format(i, label))
                chars.append(label)
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                cv2.putText(img, label, (x-5, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))

        plt.figure(figsize=(10, 10))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite("output/9_system_prediction.jpg", img)
        plt.imshow(img)
        plt.savefig('output/10_with_axis.png')
        plt.axis('off')
        plt.savefig('output/11_without_axis.png')
        
        try:
            e = ''
            print('Equation: {}', chars)
            for i in chars:
                if i=='add':
                    e += '+'
                elif i=='sub':
                    e += '-'
                elif i=='mul':
                    e += '*'
                elif i=='div':
                    e += '/'
                else:
                    e += i
            v = eval(e)
            print('V Result: {}', v)
            print('E Result: {}', e)

            self.label['text'] = 'The result is: {} : {}'.format(e, v) 
            print('Value of the expression {} : {}'.format(e, v))

        except Exception as e:
            self.label['text'] = 'Sorry! I got hanged 🤐.\nError: {}'.format(e)
            print('Error: {}'.format(e))

        pass

# Running the main class
if __name__ == "__main__":
    main()