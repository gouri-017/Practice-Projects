from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
base ="#ADC4CE"
light = "#F1F0E8"

# ------------------------------------------save and reset function----------------------------------------------
def reset_all():
    website_entry.delete(0, END)
    mail_entry.delete(0, END)
    password_entry.delete(0, END)
    website_entry.focus()


def save():
    website = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
        'Email':email,
        'Password':password,
        }
    }
    if len(password) < 1 or len(email) < 1 or len(website) < 1:
        messagebox.showerror(title="Oops",message="Please do not leave any field empty.")
    else:
        ok = messagebox.askokcancel(title="Save Info?",message=f"Info you entered is as follows:\n"
        f"Email: {website} \n Password: {password}\n Save this Info?")
        if ok:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
                    # print(data)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                reset_all()




# --------------------------------------------password generator-------------------------
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

def find_password():
    key = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showerror(title='oops',message="Please Put Some Entry first.")
    else:
        if website_entry.get() in data:
            messagebox.showinfo(title=website_entry.get(),
                                message=f"Email: {data[key].get('Email')}\n Password : {data[key].get('Password')} ")
        else:
            messagebox.showerror(title='oops', message="No such details for the website found")
    finally:
        website_entry.delete(0, END)

# ------------------------------------------ui----------------------------------------------


window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=100,bg=base)
# window.minsize(width=400,height=400)

canvas = Canvas(width=500,height=500,highlightthickness=0,bg=base)
pas_img = PhotoImage(file="security.png")
canvas.create_image(250,250,image=pas_img)
# canvas.create_image(500,500,image=pas_img)
canvas.grid(row=0,column=1)

#website label
website_label= Label(text="Website: ", font=("courier", 18),bg=base)
website_label.grid(row= 1, column=0)

mail_label= Label(text="Email/Username: ", font=("courier", 18),bg=base)
mail_label.grid(row= 2, column=0)

password_label= Label(text="Password: ",bg=base, font=("courier", 18))
password_label.grid(row= 3, column=0)

# entries

website_entry = Entry(width=60,bg=light, font=("courier", 12))
website_entry.grid(row= 1, column=1, )#
website_entry.focus()

mail_entry = Entry(width=84,bg=light, font=("courier", 12))
mail_entry.grid(row= 2, column=1, columnspan = 2 )#

password_entry = Entry(width=60,bg=light, font=("courier", 12))
password_entry.grid(row= 3, column=1)

generate = Button(text="Generate password",command=generate_password,bg=light, width=30, font=("courier", 10))
generate.grid(row= 3, column=2,)

add = Button(text="Add Details", width=76, command=save,bg=light,font=("courier", 10))
add.grid(row= 4, column=1,)

search = Button(text="Search", width=30,bg=light,font=("courier", 10), command=find_password)
search.grid(row= 1, column=2,)

reset_button = Button(text="Reset ", width=29, bg=light, command=reset_all, font=("courier", 10))
reset_button.grid(row= 4, column=2, )

window.mainloop()