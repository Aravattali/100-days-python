from  tkinter import *
from tkinter import messagebox
from  random import  choice, shuffle , randint
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [ choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [ choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data ():
    website_en = website_entry.get()
    email_en = email_entry.get()
    password_en = password_entry.get()
    if len(website_en)== 0 or len(password_en) == 0:
        messagebox.showinfo(title="Oops", message="please make sure you didn't leave any fields empty1  ")
    else:
        is_ok = messagebox.askokcancel(title= website_en, message=f"These are the details entered: {website_en}\n {email_en}\n {password_en}\n  is it ok to save it? ")
        if is_ok:
            with open(file="data.txt", mode= "a") as file:
                    file.write(f"{website_en} | {email_en} | {password_en}\n")
            website_entry.delete(0,END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50 , pady=50 , bg= "white")
canvas = Canvas(width=200, height=200, bg= "white")
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100 ,image = logo_image)
canvas.grid(column=1 , row= 0)
website = Label(text="Website: ", bg="white")
website.grid(column= 0 , row= 1)
website_entry = Entry(width=35, )
website_entry.grid(column=1 ,row=1 , columnspan=2, pady=10)
website_entry.focus()
email_username = Label(text= "Email/Username: " , bg= "white")
email_username.grid(column=0, row=2)
email_entry = Entry(width=35,)
email_entry.grid(column=1, row=2 , columnspan=2 , pady=10)
email_entry.insert(0, "Arafat@gmail.com")
password = Label(text= "Password: ", bg= "white")
password.grid(column= 0, row= 3)
password_entry = Entry(width= 21)
password_entry.grid(column=1, row=3 , columnspan=1)
generate = Button(text="Generate Password", bg= "white" , command= generate_password)
generate.grid(column=2, row= 3)
add = Button(text="Add", width=36 , bg= "white", pady= 10, command= save_data)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()