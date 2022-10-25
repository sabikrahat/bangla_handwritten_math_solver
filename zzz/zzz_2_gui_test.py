
from tkinter import *
from tkinter.ttk import *
from PIL import ImageGrab
import win32gui


class main:
    def __init__(self):
        self.res = ""
        self.pre = [None, None]
        self.bs = 5.5

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

        self.root.geometry("{}x{}+{}+{}".format(self.root_width, self.root_height, self.x_cordinate, self.y_cordinate))

        self.c = Canvas(self.root, bd=3, relief="ridge", bg='white', height=self.root_height - 150, width=self.root_width - 52)
        # self.c.grid(row=0, column=0, columnspan=3, padx=20, pady=10)
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
        self.crop_test()
        # self.get_image()

    def crop_test(self):

        x, y = (self.c.winfo_rootx(), self.c.winfo_rooty())
        width, height = (self.c.winfo_width(), self.c.winfo_height())

        a, b, c, d = (x, y, x+width, y+height)
        print('canvas cordinates')
        print(a, b, c, d)
        print('System defined canvas width x height')
        print(c-a, d-b)
        print('My defined canvas width x height')
        print(self.root_width - 52, self.root_height - 150)
        # cor = self.c.coords()
        # print(cor)


        # ww = self.root.winfo_width()
        # wh = self.root.winfo_height()
        # cw = self.c.winfo_width()
        # ch = self.c.winfo_height()
        # wx = self.root.winfo_rootx()
        # wy = self.root.winfo_rooty()
        # cx = self.c.winfo_rootx()
        # cy = self.c.winfo_rooty()
        # print("Window width: {}, Window height: {}".format(ww, wh))
        # print("Canvas width: {}, Canvas height: {}".format(cw, ch))
        # print("Window x: {}, Window y: {}".format(wx, wy))
        # print("Canvas x: {}, Canvas y: {}".format(cx, cy))
        # x = self.root.winfo_rootx() + self.c.winfo_x()
        # y = self.root.winfo_rooty() + self.c.winfo_y()
        # x1 = x + self.c.winfo_width()
        # y1 = y + self.c.winfo_height()
        # # Crop the image
        img = ImageGrab.grab()
        img.save("zzz_screenshoot.png")
        # for i in range(0, 50):
        #     img2 = img.crop((a + (i*10), b+(i*10), c+(i*10), d+(i*10)))
        #     fileName = "zzz_screenshoot" + str(i) + ".png"
        #     img2.save(fileName)
        #     print('Saving image: ' + fileName)

        print('Done')
        img = img.crop((a + 76, b + 48, c + 313, d + 154))
        img.save("zzz_screenshoot.png")
        
        print('Image cropped successfully...')
        

    # Function for getting the image from the canvas
    def get_image(self):
        print('Processing image from the canvas...')
        ##
        ## Process: 01
        print('Processing: 01')
        ww = self.root.winfo_width()
        wh = self.root.winfo_height()
        cw = self.c.winfo_width()
        ch = self.c.winfo_height()
        wx = self.root.winfo_rootx()
        wy = self.root.winfo_rooty()
        cx = self.c.winfo_rootx()
        cy = self.c.winfo_rooty()
        print("Window width: {}, Window height: {}".format(ww, wh))
        print("Canvas width: {}, Canvas height: {}".format(cw, ch))
        print("Window x: {}, Window y: {}".format(wx, wy))
        print("Canvas x: {}, Canvas y: {}".format(cx, cy))
        img = ImageGrab.grab()
        img.save("full-screen-P1.png")
        img = img.crop((cx, cy, cx + self.root_width - 52, cy + self.root_height - 150))
        img.save("drawn-image-P1.png")
        print('Process-1 completed...')
        ##
        ## Process: 02
        print('Processing: 02')
        x = self.root.winfo_rootx() + self.c.winfo_x()
        y = self.root.winfo_rooty() + self.c.winfo_y()
        x1 = x + self.c.winfo_width()
        y1 = y + self.c.winfo_height()
        print("x: ", x, "y: ", y, "x1: ", x1, "y1: ", y1)
        img = ImageGrab.grab()
        img.save("full-screen-P2.png")
        img = img.crop((x, y, x1, y1))
        img.save("drawn-image-P2.png")
        print('Process-2 completed...')
        ##
        ## Process: 03
        print('Processing: 03')
        HWND = self.c.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        im = ImageGrab.grab(rect)
        im.save("drawn-image-P3.png")
        print('Process-3 completed...')
        ##
        ## Process: 04
        print('Processing: 04')
        ImageGrab.grab(bbox=(
            self.c.winfo_rootx(),
            self.c.winfo_rooty(),
            self.c.winfo_rootx() + self.c.winfo_width(),
            self.c.winfo_rooty() + self.c.winfo_height()
        )).save('drawn-image-P4.png')
        print('Process-4 completed...')
        ##
        ## Process: 05
        ##
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