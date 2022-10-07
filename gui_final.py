
from tkinter import *
from tkinter.ttk import *
from PIL import ImageGrab


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
        success = self.get_image()
        if success:
            self.get_solve()

    # Function for getting the image from the canvas
    def get_image(self):
        print('Processing image from the canvas...')
        #
        x, y = (self.c.winfo_rootx(), self.c.winfo_rooty())
        width, height = (self.c.winfo_width(), self.c.winfo_height())
        a, b, c, d = (x, y, x+width, y+height)
        #
        img = ImageGrab.grab()
        img.save("full-screen.png")
        img = img.crop((a + 76, b + 48, c + 313, d + 154))
        img.save("drawn-image.png")
        print('Image saved!')
        return True

    # Function for solving the prediction
    def get_solve(self):
        print('Solving the equation...')
        pass

# Running the main class
if __name__ == "__main__":
    main()