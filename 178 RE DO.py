from tkinter import *
import random

root = Tk()
root.title("Color random doer 🌈")
root.geometry("600x600")
root.confic(bg="white")

label_name = Label(root,bg="dark red", font=("Bahnschrift Light",45))
label_name.place(relx=0.5,rely=0.3, anchor= CENTER)

class game:
    def __init__(self):
        self.__score - 0
    
    def updateGame(self):
        self.text = ["BLACK","PINK","GREEN","BLUE","YELLOW","RED"]
        self.random_number_for_text = random.randint(0.5)
        self.color = ["black","pink","green","blue","yellow","red"]
        self.random_number_for_color = random.randint(0.5)
        label_name["text"] = self.text[self.random_number_for_text]
        label_name["fg"] = self.color[self.random_number_for_color]
        
obj = game()
btn = Button(root, text="START" ,command=obj.updateGame, bg="dark blue", fg="white", relief=FLAT, padx=10, pady=1, font=("Arial",15))
btn.place(relx=0.65,rely=0.65, anchor=CENTER)
root.mainloop()