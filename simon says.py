from tkinter import Tk, Label, Button
import time
import random

class myFirstGUI:
    def __init__(self, master):
        random.seed()
        self.turn_number = 1
        self.playing_round = False

        self.master = master
        master.title("Simon Says")

        self.label = Label(master, text="Let's Play Simon Says!")
        self.label.grid(row=0, column=0, columnspan=2)

        #creat and place buttons in GUI

        self.red_button = Button(master, text="Red", bg='white', command=self.red)
        self.red_button.grid(row=1, column=0)

        self.green_button = Button(master, text="Green", bg='white', command=self.green)
        self.green_button.grid(row=1, column=1)

        self.blue_button = Button(master, text="Blue", bg='white', command=self.blue)
        self.blue_button.grid(row=2, column=0)

        self.yellow_button = Button(master, text="Yellow", bg='white', command=self.yellow)
        self.yellow_button.grid(row=2, column=1)

        self.play_button = Button(master, text="Play!", command=self.play)
        self.play_button.grid(row=3, column=0, columnspan=2)

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.grid(row=4, column=0, columnspan=2)

    def press_color_button(self, button_color):
        #self.flash_button(button_color)
        if self.playing_round == True:
            if self.button_sequence and self.button_sequence[0] == button_color:
                print("Correct!")
                self.button_sequence.pop(0)
            else:
                print("Oops! The correct button was %s!" % self.button_sequence[0])
                print("You lose!")
                self.playing_round = False
                self.turn_number = 1
        else:
            print(button_color + "!")

    def red(self):
        self.press_color_button("red")

    def green(self):
        self.press_color_button("green")

    def blue(self):
        self.press_color_button("blue")

    def yellow(self):
        self.press_color_button("yellow")

    def poll_user_input(self):
        if len(self.button_sequence) > 0:
            self.master.after(100, self.poll_user_input) #runs every 100 milliseconds
        else:
            print("You win!")
            self.turn_number += 1

    def reset_to_white(self, which_button):
        which_button.configure(bg='white')

    def flash_button(self, which_button):
        print("HERE I AM and button is " + which_button)
        if which_button == "red":
            self.red_button.configure(bg="red")
            self.master.after(500, self.reset_to_white, self.red_button)

        if which_button == "blue":
            self.blue_button.configure(bg="blue")
            self.master.after(500, self.reset_to_white, self.blue_button)

        if which_button == "green":
            self.green_button.configure(bg="green")
            self.master.after(500, self.reset_to_white, self.green_button)

        if which_button == "yellow":
            self.yellow_button.configure(bg="yellow")
            self.master.after(500, self.reset_to_white, self.yellow_button)

    def play(self):
        self.playing_round = True
        print("Let's play! Remember the color patterns, then press them in order!")
        print("Ready... remember this!")
        
        self.button_sequence = []
        #
        for num in range(self.turn_number):
            which_button = random.choice(["red", "yellow", "blue", "green"])
            self.button_sequence.append(which_button)
            self.flash_button(which_button)
            
            self.master.after((num*1100), self.flash_button, which_button)

        print("Now it's your turn! Press the buttons in the right order!")
        self.poll_user_input()

root = Tk()

my_gui = myFirstGUI(root)

root.mainloop()
