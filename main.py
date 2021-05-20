from tkinter import *
from tkinter import messagebox
import json

# ---------------------------- Find Data ------------------------------- #


def find_data():

    search= search_entry.get().title()
    category = category_entry.get().upper()

    if category == "MOVIE":
        with open("Movie.json", "r") as data_file:
            data= json.load(data_file)
            if search in data:
                rating = data[search]["Rating"]
                coment = data[search]["Coment"]

                messagebox.showinfo(title="Watchlist data", message=f"Status : Watched.\nrating : {rating} \ncoment : {coment}")

            else:
                messagebox.showerror(title="Not found", message=f"There is no movie named '{search}' in your watchlist!")
    elif len(category) == 0:
        messagebox.showerror(title="Category box empty", message="Please fill up the 'movie/tv-series' box. \nIf you are searching for movie then write 'movie'. \nelse write 'tv-series' in the 'movie/tv-series' entry box")

    else:

        with open("tv-series.json", "r") as data_file:
            data = json.load(data_file)
            if search in data:
                rating = data[search]["Rating"]
                coment = data[search]["Coment"]

                messagebox.showinfo(title="Watchlist data",
                                    message=f"Status : Watched.\nrating : {rating} \ncoment : {coment}")

            else:
                messagebox.showerror(title="Not found", message=f"There is no series named '{search}' in your watchlist!")


# --------------------------- SAVE DATA ------------------------------- #

def save_data():
    category= category_entry.get().upper()
    name= Name_entry.get().title()
    rating= Rating_entry.get()
    review= Review_entry.get("1.0","end-1c")
    if category == "MOVIE":

        new_data = {
                name: {
                    "Rating": rating,
                    "Coment": review,
                }
        }
        if len(name)== 0 or len(category)==0:
            messagebox.showerror(title="Box empty", message="Please make sure you did not left first two entry field empty!")

        else:
            try:

                with open("Movie.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open("Movie.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except:
                with open("Movie.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)



            messagebox.showinfo(title="Saving Alert", message="Your media info has been added to watchlist")

            Name_entry.delete(0,END)
            Rating_entry.delete(0,END)
            Review_entry.delete("1.0",END)
            category_entry.delete(0,END)

    else:
        new_data = {
            name: {
                "Rating": rating,
                "Coment": review,

            }
        }
        if len(name) == 0 or len(category) == 0:
            messagebox.showerror(title="Box empty", message="Please make sure you did not left first two entry field empty!")

        else:
            try:

                with open("tv-series.json", "r") as data_file:
                    data = json.load(data_file)
                    data.update(new_data)
                with open("tv-series.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            except:
                with open("tv-series.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)

            messagebox.showinfo(title="Saving Alert", message="Your media info has been added to watchlist")

            Name_entry.delete(0, END)
            Rating_entry.delete(0, END)
            Review_entry.delete("1.0", END)
            category_entry.delete(0,END)



# --------------------------- GUI SETUP------------------------------- #



window = Tk()

window.title("My Watchlist")
window.config(padx=30, pady=20,)


canvas= Canvas(height=200, width= 200)
media_image= PhotoImage(file= "media_logo.png")
canvas.create_image(100,100, image=media_image)

canvas.grid(column=0,row=1, columnspan=3, pady=20)


category_label= Label(text=" Movie/Tv-series : ")
category_label.grid(column=0,row=2, columnspan=1, pady=5,)

category_entry= Entry(width=20)
category_entry.grid(column=1,row=2, columnspan=2, pady=5,)


Name_label= Label(text="Name :")
Name_label.grid(column=0,row=3, columnspan=1, pady=5,)


Name_entry= Entry(width=20)
Name_entry.grid(column=1,row=3, columnspan=2)


Rating_label= Label(text="Rating :")
Rating_label.grid(column=0,row=4, columnspan=1)


Rating_entry= Entry(width=20)
Rating_entry.grid(column=1,row=4, columnspan=2,)

Review_label= Label(text= "Review :")
Review_label.grid(column=0,row=5, columnspan=1)


Review_entry= Text(width= 15, height= 3,)
Review_entry.grid(column=1,row=5, columnspan=2, pady= 20)


add_button2= Button(text="Add",width= 40 , command= save_data,)
add_button2.grid(column= 0, row=6 ,columnspan=3)

search_entry= Entry(width=20,)
search_entry.grid(column=1,row=7, columnspan=1)

search_button= Button(text= "search", width= 10, bg= "deepskyblue", command=find_data)
search_button.grid(column=2,row=7, columnspan=1, pady= 10)


window.mainloop()


