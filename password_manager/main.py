from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]

    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]

    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list= password_letters+ password_symbols + password_numbers

    random.shuffle(password_list)

    password= "".join(password_list)

    print(f"Your password is: {password}")

    password_entry.insert(0, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email= email_entry.get()
    password= password_entry.get()
    new_dict= {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website)==0 or len(password)==0:
        display= messagebox.showerror(title="Error", message="Either Website or password is empty")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_dict)

        except FileNotFoundError and json.decoder.JSONDecodeError:
            with open("data.json", "w") as data_file:
                json.dump (new_dict, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

def search():
    website_to_search = website_entry.get()
    try:
        with open("data.json") as data_file:
            data= json.load(data_file)

    except FileNotFoundError:
        display= messagebox.showinfo(title=" Error", message=" file doesnt exist")

    else:
        if website_to_search in data:
            email = data[website_to_search]["email"]
            password = data[website_to_search]["password"]
            messagebox.showinfo(title="Information", message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showerror(title="error", message=f"no details for {website_to_search} exist")
# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")
window.config(padx=10, pady=10, bg="white")

canvas= Canvas(width=200, height=200, highlightthickness=0, bg="White")
lock_imp= PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_imp )
canvas.grid(column=1,row=0)

website_label= Label(text= "Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry= Entry(width=45)
website_entry.grid(row=1, column= 1, columnspan=2)
website_entry.focus()

email_label= Label(text= "Email/ Username: ", bg="white")
email_label.grid(column=0, row=2)

email_entry= Entry(width= 45)
email_entry.grid(column=1,row=2, columnspan=2)
email_entry.insert(0, "kritika@email.com")


password_label= Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry= Entry(width=23)
password_entry.grid(column=1, row=3)

pass_button= Button(text= "Generate Password", command=generate_password)
pass_button.grid(column=2, row=3)


add_button=Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button= Button(text="Search", command=search)
search_button.grid(column=2, row=1)


window.mainloop()