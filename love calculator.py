import tkinter as tk
import random

class LoveCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("love calculator")
        self.create_widget()

    def create_widget(self):
        tk.Label(self.root, text="enter XY name").pack(pady=5)
        self.boy_entry=tk.Entry(self.root)
        self.boy_entry.pack(pady=5)
        tk.Label(self.root, text="enter XX name").pack(pady=5)
        self.girl_entry=tk.Entry(self.root)
        self.girl_entry.pack(pady=5)

        self.calculate_button = tk.Button(self.root , text="calculate_love" , command=self.test_love)
        self.calculate_button.pack(pady=5)
        self.result_label = tk.Label(self.root , text="")
        self.result_label.pack(pady=5)

    def test_love(self):
        boy_name = self.boy_entry.get()
        girl_name= self.girl_entry.get()
        if boy_name == "" or girl_name == "":
            self.result_label.config(text="pls enter your both name")
            return
        love_line =random.randint(0,100)
        self.result_label.config(text=f"{boy_name} and {girl_name} loved percent is {love_line}%")

if __name__=="__main__":
    root = tk.Tk()
    app =LoveCalculator(root)
    root.mainloop()







