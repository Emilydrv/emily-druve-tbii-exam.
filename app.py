import tkinter as tk
from PIL import Image, ImageTk
from helpers import clear_widgets, set_background ,resizing_images
import random
from tkinter import messagebox
import pandas as pd
from tkinter import ttk


root = tk.Tk()
root.title("Pet-Match")
screen_height = 750
screen_width = 420
root.geometry(f"{screen_width}x{screen_height}")


def pet_lists():
    # This function is used later in the "no_more ..." functions to re-fill the list of pets, after all the options have been shown once.
    global options_cats, options_dogs, options_others

    options_cats = ["cat1", "cat2", "cat3"]
    options_dogs = ["dog1", "dog2", "dog3"]
    options_others = ["other1", "other2", "other3"]


def sent():
    # This is the last page of my app, which is shown, when a user has contacted a shelter using the app.
    # Most of the pages start with calling the following definitions from the helpers function to clear everything and then add the new background image.
    clear_widgets(root)
    set_background(root, 'images/start1.jpeg')


    # It infroms the user with some text labels, that their message was sent.
    thanks_label = tk.Label(root, text= f"Thanks, {current_user}!",
                          font="Arial 23 bold",
                          bg="cadetblue4",
                          fg="black",
                          bd=2,
                          relief="solid",
                          padx=6,
                          pady=2,
                          height=2)
    thanks_label.place(relx= 0.5, y=315, anchor="center")

    thanks2_label = tk.Label(root, text="Your request has been sent to the shelter.",
                          font="Arial 15 bold",
                          bg="white",
                          fg="black",
                          bd=2,
                          relief="solid",
                          height=2)
    thanks2_label.place(relx=0.5, y=360, anchor="center")


# The following 3 pages (lines 57 - 159) are shown when a user has clicked through all options of the selected pet-type.
# It is explained only in the first of the three, since they all are pretty much the same.
def no_more_dog():
    # This is called once the user has scrolled through all dogs.
    set_background(root, 'images/lightsteelblue1.jpeg')

    #It adds some text labels.
    no_more_title = tk.Label(text="Sorry, you've seen all the options!",
                             font="arial 20 bold",
                             bg="cadetblue4",
                             fg="Black",
                             relief="solid",
                             bd=2,
                             height=3,
                             width=28)
    no_more_title.place(x=40, y=230)

    subline_title = tk.Label(text="Would you like to match again?",
                             font="arial 19",
                             bg="seashell2",
                             relief="solid",
                             bd=2,
                             fg="Black")
    subline_title.place(relx=0.5, y=317, anchor="center")

    # And creates two buttons. One to re-start and the other one quits the app.
    again_button = tk.Button(text="Match again",
                             font='lucida 16 bold',
                             bd=0,
                             command=lambda: [clear_widgets(root), pet_lists(), choose("dog")])
    again_button.place(x=60, y=370)

    exit_button = tk.Button(text="Close application",
                            font='lucida 16 bold',
                            bd=0,
                            command=root.destroy)
    exit_button.place(x=205, y=370)


def no_more_cat():
    set_background(root, 'images/lightsteelblue1.jpeg')

    no_more_title = tk.Label(text="Sorry, you've seen all the options!",
                             font="arial 20 bold",
                             bg="cadetblue4",
                             fg="Black",
                             relief="solid",
                             bd=2,
                             height=3,
                             width=28)
    no_more_title.place(x=40, y=230)

    subline_title = tk.Label(text="Would you like to match again?",
                             font="arial 19",
                             bg="seashell2",
                             relief="solid",
                             bd=2,
                             fg="Black")
    subline_title.place(relx=0.5, y=317, anchor="center")

    again_button = tk.Button(text="Match again",
                             font='lucida 16 bold',
                             bd=0,
                             command=lambda: [clear_widgets(root), pet_lists(), choose("cat")])
    again_button.place(x=60, y=370)

    exit_button = tk.Button(text="Close application",
                            font='lucida 16 bold',
                            bd=0,
                            command=root.destroy)
    exit_button.place(x=205, y=370)


def no_more_other():
    set_background(root, 'images/lightsteelblue1.jpeg')

    no_more_title = tk.Label(text="Sorry, you've seen all the options!",
                             font="arial 20 bold",
                             bg="cadetblue4",
                             fg="Black",
                             relief="solid",
                             bd=2,
                             height=3,
                             width=28)
    no_more_title.place(x=40, y=230)

    subline_title = tk.Label(text="Would you like to match again?",
                             font="arial 19",
                             bg="seashell2",
                             relief="solid",
                             bd=2,
                             fg="Black")
    subline_title.place(relx=0.5, y=317, anchor="center")

    again_button = tk.Button(text="Match again",
                             font='lucida 16 bold',
                             bd=0,
                             command=lambda: [clear_widgets(root), pet_lists(), choose("other")])
    again_button.place(x=60, y=370)

    exit_button = tk.Button(text="Close application",
                            font='lucida 16 bold',
                            bd=0,
                            command=root.destroy)
    exit_button.place(x=205, y=370)


def enter_user_data():
    # This is used, when a new user is signing up for my app.
    global chosen_pet, current_user

    current_user = name.get()
    chosen_pet = combo.get()


    user_data = pd.read_csv("data/user_data.csv")
    users_ids = list(user_data["username"])

    if username.get() in users_ids:
        tk.messagebox.showwarning("WARNING!", "THIS USERNAME ALREADY EXISTS")
    else:
        user_data = {"name_of_user": ["name", name.get()],
                         "username": ["username", username.get()],
                         "petchoice": ["combo", combo.get()]
                         }
        user_data = pd.DataFrame.from_dict(user_data)
        # This converts the dictionary into a dataframe.

        # And writes the dataframe to a .csv file.
        user_data.to_csv("data/user_data.csv", index=False, mode='a', header=False)
        choose(combo.get())
        # Then it redirects the uses to the rest of the app.


def check_user():
    # This is used when a returning user is trying to sign back into the app.
    # It checks whether the username already exists and if so redirects users to the rest of the app.
    global chosen_pet, current_user
    user_data = pd.read_csv("data/user_data.csv")
    user_ids = list(user_data["username"])
    user_combos = list(pd.read_csv("data/user_data.csv").combo)
    user_names = list(pd.read_csv("data/user_data.csv").name)
    count=0

    # The following if else statement was created with the help of chatGPT. More information on that is in my report.
    if user_id.get() in user_ids:
        clear_widgets(root)
        for i in user_ids:
            if user_id.get() == i:
                chosen_pet=user_combos[count]
                current_user = user_names[count]
                choose(chosen_pet)
            count=count+1


    else:
        tk.messagebox.showwarning("WARNING", "User does not exist")


def sign_in():
    # This is the page for returning users.
    # It uses the "check_user" definition to work.
    global user_id

    clear_widgets(root)

    set_background(root, 'images/bg4.jpeg')

    # I added some labels.
    sign_in_title = tk.Label(text="Welcome back!",
                             font="arial 20 bold",
                             bg="seashell2",
                             fg="Black",
                             height=3,
                             relief="solid",
                             bd=2,
                             width=15)
    sign_in_title.place(relx=0.5, y=90, anchor="center")



    userid_label = tk.Label(root,
                              text="Enter your user name:",
                              font="arial 14",
                              fg="black",
                              bg="white",
                              relief="solid",
                              bd=0.5
                              )
    userid_label.place(x=55, y=240)

    # This is the box for the user to enter their username.
    user_id = tk.StringVar()
    userid_box = tk.Entry(root,
                          textvar=user_id,
                          fg="black",
                          bg="white",
                          width=30
                          )
    userid_box.place(relx=0.5, y=300, anchor="center")

    # This button activates the "check_user" function.
    sign_in_button = tk.Button(root,
                               text="Sign in",
                               command=check_user,
                               font='lucida 15 bold',
                               bd=0,
                               )
    sign_in_button.place(relx=0.5, y=600, anchor="center")


def sign_up():
    # This is the page for new users.
    # It uses the "enter_user_data" definition to work.
    global name, username, combo
    set_background(root, 'images/bg4.jpeg')

    # The labels inform the user what information to enter.
    sign_up_title = tk.Label(text="Sign up as a new user now!",
                             font="arial 20 bold",
                             bg="seashell2",
                             fg="black",
                             height=3,
                             relief="solid",
                             bd=2,
                             width=25)
    sign_up_title.place(relx=0.5, y=90, anchor="center")

    name_label = tk.Label(root,
                          text="What's your name?",
                          font="arial 14",
                          fg="black",
                          bg="white",
                          relief="solid",
                          bd=0.5
                          )
    name_label.place(x=55, y=210)

    # This is the box where the user can enter their name.
    name = tk.StringVar()
    name_box = tk.Entry(root,
                        textvar=name,
                        fg="black",
                        bg="white",
                        width=30
                        )
    name_box.place(relx=0.5, y=270, anchor="center")

    username_label = tk.Label(root,
                              text="Create a user name!",
                              font="arial 14",
                              fg="black",
                              bg="white",
                              relief="solid",
                              bd=0.5
                              )
    username_label.place(x=55, y=340)

    # This is the box where the user can choose their username.
    username = tk.StringVar()
    username_box = tk.Entry(root,
                            textvar=username,
                            fg="black",
                            bg="white",
                            width=30
                            )
    username_box.place(relx=0.5, y=400, anchor="center")

    # This is the dropdown menu, the instructions for which I found online at https://pythonassets.com/posts/drop-down-list-combobox-in-tk-tkinter/
    combo_label = tk.Label(root,
                           text= "What pet are you looking for?",
                           font="arial 14",
                           fg="black",
                           bg="white",
                           relief="solid",
                           bd=0.5
                           )
    combo_label.place(x=55, y=470)

    combo = ttk.Combobox(root,
                         state="readonly",
                         values=("dog", "cat", "other"),
                         width=30
                         )
    combo.place(relx=0.5, y=530, anchor="center")

    submit_button = tk.Button(root,
                           text="Submit Info",
                           font='lucida 15 bold',
                           bd=0,
                           command=enter_user_data
                           )
    submit_button.place(relx=0.5, y=610, anchor="center")


# The following 3 definitions (lines 352 - 497) are the contact-pages of the three different shelters the pets on this app are from: Hamburg, Lüneburg and Braunschweig.
# It is only explained further in the first definition, since they are so similar.
def contact1():
    set_background(root, 'images/bg4.jpeg')

    # This adds a title.
    contact_title = tk.Label(text="Contact",
                        font="arial 30 bold",
                        bg="seashell2",
                        fg="Black",
                        height=3,
                        relief="solid",
                        pady=2,
                        padx=2,
                        bd=2,
                        width=15)
    contact_title.place(relx=0.5, y=90, anchor="center")

    # This is the contact information about the shelter.
    contact1_descr = tk.Label(text="Tierschutzverein Lüneburg\nBockelmannstraße 3\n21337 Lüneburg\n04131/82424",
                              font="arial 11 ",
                              bg= "white",
                              relief="solid",
                              bd=1,
                              pady=2,
                              padx=2,
                              fg="Black")
    contact1_descr.place(relx=0.5, y=245, anchor="center")

    # In the following 3 boxes the user can enter their message to the shelter.
    name_field = tk.Text(root, height=1, width=34)
    name_field.pack()
    name_field.insert(tk.END, current_user)
    name_field.place(x=80, y=300)

    mail_field = tk.Text(root, height=1, width=34)
    mail_field.pack()
    mail_field.insert(tk.END, "enter your e-mail")
    mail_field.place(x=80, y=340)

    message_field = tk.Text(root, height=20, width=34)
    message_field.pack()
    message_field.insert(tk.END, "enter your message")
    message_field.place(x=80, y=380)

    # This button leads the user to the page confirming the message was sent.
    send_button = tk.Button(text="Send",
                            font='lucida 15 bold',
                            bd=0,
                            command= sent)
    send_button.place(relx=0.5, y=672, anchor="center")


def contact2():
    set_background(root, 'images/bg4.jpeg')

    contact_title = tk.Label(text="Contact",
                             font="arial 30 bold",
                             bg="seashell2",
                             fg="Black",
                             relief="solid",
                             bd=2,
                             pady=2,
                             padx=2,
                             height=3,
                             width=15)
    contact_title.place(relx=0.5, y=90, anchor="center")

    contact2_descr = tk.Label(text="Tierschutz Braunschweig\nBiberweg 30\n38114 Braunschweig\nTel. 0531-500007",
                              font="arial 11 ",
                              bg="white",
                              relief="solid",
                              pady=2,
                              padx=2,
                              bd=1,
                              fg="Black")
    contact2_descr.place(relx=0.5, y=242, anchor="center")

    name_field = tk.Text(root, height=1, width=34)
    name_field.pack()
    name_field.insert(tk.END, current_user)
    name_field.place(x=80, y=300)

    mail_field = tk.Text(root, height=1, width=34)
    mail_field.pack()
    mail_field.insert(tk.END, "enter your e-mail")
    mail_field.place(x=80, y=340)

    message_field = tk.Text(root, height=20, width=34)
    message_field.pack()
    message_field.insert(tk.END, "enter your message")
    message_field.place(x=80, y=380)

    send_button = tk.Button(text="Send",
                            font='lucida 15 bold',
                            bd=0,
                            command= sent
                            )
    send_button.place(relx=0.5, y=672, anchor="center")


def contact3():
    set_background(root, 'images/bg4.jpeg')
    contact_title = tk.Label(text="Contact",
                             font="arial 30 bold",
                             bg="seashell2",
                             fg="Black",
                             height=3,
                             pady=2,
                             padx=2,
                             width=15,
                             relief="solid",
                             bd=2,
                             )
    contact_title.place(relx=0.5, y=90, anchor="center")

    contact3_descr = tk.Label(text="Hamburger Tierschutzverein\nSüderstraße 399\n20537 Hamburg\nTel. 040-211 10 60",
                             font="arial 11",
                             bg="white",
                             relief="solid",
                             pady=2,
                             padx=2,
                             bd=1,
                             fg="Black"
                              )
    contact3_descr.place(relx=0.5, y=235, anchor="center")

    name_field = tk.Text(root, height=1, width=34)
    name_field.pack()
    name_field.insert(tk.END, current_user)
    name_field.place(x=80, y=290)

    mail_field = tk.Text(root, height=1, width=34)
    mail_field.pack()
    mail_field.insert(tk.END, "enter your e-mail")
    mail_field.place(x=80, y=330)

    message_field = tk.Text(root, height=20, width=34)
    message_field.pack()
    message_field.insert(tk.END, "enter your message")
    message_field.place(x=80, y=370)

    send_button = tk.Button(text="Send",
                            font='lucida 15 bold',
                            bd=0,
                            command= sent
                            )
    send_button.place(relx=0.5, y=668, anchor="center")


# The following 9 definitions (lines 502 - 915) are the pages, on which the pets are described in more detail, in case the user wants to know more about one of the pets.
# It is only explained further in the first definition, since they are so similar.
def cat1_info():

    # This definition from the helpers stacks the background image and the image of the pet.
    resizing_images(root,
                    'images/bg3.jpeg',
                    'images/rcat1_2.jpeg',
                    screen_width,
                    screen_height,
                    160, 130, 63, 66)


    # These labels describe the animal.
    cat_name = tk.Label(text="Karl-Heinz ♂",
                        font="arial 22 bold ",
                        bg="seashell2",
                        fg="Black")
    cat_name.place(x=240, y=65)

    cat_descr1 = tk.Label(text="Age: 12 years old\n\n- Vaccinated\n \n- Neutered",
                          font="arial 15 ",
                          bg="seashell2",
                          fg="Black")
    cat_descr1.place(x=240, y=100)

    cat_descr2 = tk.Label(text="Karl-Heinz is a very sweet, affectionate cat \n \nwho is now looking for a home where he \n \ncan enjoy secure outdoor access. It's important \n \nto note that Karl-Heinz is FIV-positive. Until now, \n \nthis adorable kitty has only lived as a \n\nferal cat outdoors and is not familiar with \n \nlife inside a house or apartment. We would \n \nbe happy to provide more information about \n \nKarl-Heinz in a personal conversation.",
                          font="arial 13",
                          bg="seashell2",
                          fg="dimgray")
    cat_descr2.place(x=55, y=235)

    # The buttons add the options of either going to the contact page, going back to the pets profile page, or seeing the next pet.
    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact1()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("cat")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), cat1()])
    back_button.place(x=10, y=10)


def cat2_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rcat2_1.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)


    cat_name = tk.Label(text="Maggie ♀",
                        font="arial 22 bold ",
                        bg="seashell2",
                        fg="Black")
    cat_name.place(x=250, y=65)

    cat_descr1 = tk.Label(text="Age: 12 years old\n  \n- Vaccinated\n  \n- Microchipped\n\n- Spayed",
                          font="arial 16 ",
                          bg="seashell2",
                          fg="Black")
    cat_descr1.place(x=230, y=105)

    cat_descr2 = tk.Label(
        text="Maggie is a cat with a strong personality.She\n\nis independent and a bit of a diva. Maggie\n\nallows brief petting, but she quickly tires\n\nof human attention and makes this clear, using\n\n claws and teeth. We are looking for people who\n\ncan accommodate Maggie's character and give her\n\nspace.Maggie has been kept indoors until now, but\n\nwe think she might do well with outdoor access.\n\nThere should be no children in the same household.\n\nMaggie gets along with other cats,but she\n\ndoesn't need a companion to be happy.",
        font="arial 13",
        bg="seashell2",
        fg="dimgray")
    cat_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact2()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("cat")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), cat2()])
    back_button.place(x=10, y=10)


def cat3_info():
    resizing_images(root,
                    'images/bg3.jpeg',
                    'images/rcat3_2.jpeg',
                    screen_width,
                    screen_height,
                    160, 130, 63, 66)

    cat_name = tk.Label(text="Lilly ♀",
                        font="arial 22 bold",
                        bg="seashell2",
                        fg="Black")
    cat_name.place(x=275, y=65)

    cat_descr1 = tk.Label(text="Age:14 years old\n  \n- European Shorthair\n\n- Spayed",
                          font="arial 15 ",
                          bg="seashell2",
                          fg="Black")
    cat_descr1.place(x=235, y=100)

    cat_descr2 = tk.Label(
        text="We would describe Lilly as affectionate, cuddly\n\nand confident with a calm demeanor. She requires\n\na quiet environment. Our sweet Lilly unfortunately\n\nhas kidney issues. She is a true cuddlebug\n\nand has so much love to give. Currently, this\n\nlittle sweetheart needs some time to recover\n\nbefore she can move to a new home.",
        font="arial 13",
        bg="seashell2",
        fg="dimgray")
    cat_descr2.place(x=55, y=235)


    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact3()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("cat")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), cat3()])
    back_button.place(x=10, y=10)


def dog1_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rdog1_2.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)

    dog_name = tk.Label(text="Boogey ♂",
                        font="arial 22 bold",
                        bg="seashell2",
                        fg="Black")
    dog_name.place(x=250, y=65)

    dog_descr1 = tk.Label(text="Age:11 years old\n  \n- Vaccinated\n  \n- Microchipped\n\n- Neutered",
                          font="arial 16 ",
                          bg="seashell2",
                          fg="Black")
    dog_descr1.place(x=230, y=105)

    dog_descr2 = tk.Label(
        text="Boogey came to us because his owner passed\n\naway.For his age, this Golden Retriever is still very\n\nfit and active. He gets along well with females and\n\nneutered males, but with unneutered males\n\ninteractions can be challenging.Boogey is open and\n\naffectionate, however he shouldn't be placed with\n\nchildren or first-time dog owners. This handsome\n\nfellow has an issue: status/resource guarding. This\n\nis the reason why he couldn't find a stable home\n\nafter his owner's passing. Using a muzzle will\n\nbe mandatory in his new home.",
        font="arial 13",
        bg="seashell2",
        fg="dimgray")
    dog_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact1()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("dog")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), dog1()])
    back_button.place(x=10, y=10)


def dog2_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rdog2_2.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)

    dog_name = tk.Label(text="Scotty ♂",
                        font="arial 22 bold",
                        bg="seashell2",
                        fg="Black")
    dog_name.place(x=250, y=65)

    dog_descr1 = tk.Label(text="Age:4 years old\n  \n- Dachshundmix\n  \n- Vaccinated\n\n- Neutered",
                          font="arial 16",
                          bg="seashell2",
                          fg="Black")
    dog_descr1.place(x=230, y=105)

    dog_descr2 = tk.Label(text="Scotty had been kept inappropriately. He is a fearful\n\ndog who has little trust in humans. Currently, he\n\ncannot be touched and becomes stressed and\n\ninsecure quickly. It appears that Scotty has had\n\nminimal contact with unfamiliar people in his\n\npast. However, this anxious male gets along well\n\nwith other dogs. He tends to rely on other dogs for\n\nguidance, so having a confident companion dog in\n\nhis new home would be a significant help for him.\n\nScotty is looking for a household without children,\n\nwith experienced dog owners, who can provide\n\nhim with plenty of time and patience.",
                          font="arial 13",
                          bg="seashell2",
                          fg="dimgray")
    dog_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact2()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("dog")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), dog2()])
    back_button.place(x=10, y=10)


def dog3_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rdog3_2.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)

    dog_name = tk.Label(text="Goliath ♂",
                        font="arial 22 bold",
                        bg="seashell2",
                        fg="Black")
    dog_name.place(x=248, y=65)

    dog_descr1 = tk.Label(text="Age:3 years old\n  \n- Pomeranian\n  \n- Vaccinated\n\n- Not neutered",
                          font="arial 16 ",
                          bg="seashell2",
                          fg="Black")
    dog_descr1.place(x=230, y=105)

    dog_descr2 = tk.Label(text="Goliath’s confidence is immense, and he can sense\n\nweakness. He is at the shelter because he\n\nseriously injured his previous owners and attacked\n\nthe dog control service aggressively. Goliath is\n\ncute, can perform many tricks, and listens when\n\nyou assert your authority. Goliath knows who\n\nhe can push boundaries with but can also\n\nbe submissive when required. If you are considering\n\ngiving Goliath a home, you must be aware that you\n\nwould be taking in a potentially dangerous dog,\n\nthat is not suitable for households with children.\n\nHowever,he also has a lot of potential for change.",
                          font="arial 13",
                          bg="seashell2",
                          fg="dimgray")
    dog_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) , contact3()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root), choose("dog")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), dog3()])
    back_button.place(x=10, y=10)


def other1_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rother1_1.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)

    other_name = tk.Label(text="Agathe ♀",
                          font="arial 22 bold ",
                          bg="seashell2",
                          fg="Black")
    other_name.place(x=250, y=65)

    other_descr1 = tk.Label(text="Age: unknown\n\n- Not vaccinated\n \n- Not microchipped\n \n- Not spayed",
                            font="arial 16 ",
                            bg="seashell2",
                            fg="Black")
    other_descr1.place(x=230, y=105)

    other_descr2 = tk.Label(text="Agathe came to us from a bad living situation.\n\nShe is looking forward to a new home where she\n\nwill have plenty of space to move around, since she\n\nhasn’t experienced that in her past.This rabbit\n\nis not very familiar with humans yet and finds\n\nus quite intimidating. As a result, she is not\n\nvery cuddly at the moment. Currently, Agathe lives\n\nin our outdoor enclosure. She has already bee\n\n introduced to fresh food while with us and\n\nwill be delighted to continue receiving it.",
                            font="arial 13",
                            bg="seashell2",
                            fg="dimgray")
    other_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact1()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("other")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), other1()])
    back_button.place(x=10, y=10)


def other2_info():
    resizing_images(root,
                    'images/bg2.jpeg',
                    'images/rother2_1.jpeg',
                    screen_width,
                    screen_height,
                    120, 170, 68, 71)

    other_name = tk.Label(text="Ferrets ♀",
                          font="arial 22 bold ",
                          bg="seashell2",
                          fg="Black")
    other_name.place(x=250, y=65)

    other_descr1 = tk.Label(text="Age: multiple\n  \n- Albino\n  \n- mother and offspring\n\n- spayed",
                            font="arial 16 ",
                            bg="seashell2",
                            fg="Black")
    other_descr1.place(x=220, y=105)

    other_descr2 = tk.Label(text="The photo is just a symbolic image.\n\nThe animals in question are albino ferrets.\n\nCurrently, there are 6 female albino ferrets in the\n\nshelter,all of whom are looking for new homes.\n\nAmong them is a mother ferret with her offspring.\n\nThe mother ferret has already been spayed.",
                            font="arial 13",
                            bg="seashell2",
                            fg="dimgray")
    other_descr2.place(x=55, y=270)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact2()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("other")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), other2()])
    back_button.place(x=10, y=10)


def other3_info():
    resizing_images(root,
                    'images/bg3.jpeg',
                    'images/rother3_2.jpeg',
                    screen_width,
                    screen_height,
                    160, 130, 63, 66)

    other_name = tk.Label(text="Ludwig ♂",
                          font="arial 22 bold",
                          bg="seashell2",
                          fg="Black")
    other_name.place(x=250, y=65)


    other_descr1 = tk.Label(text="Age:3 years old\n  \n- Yellow-naped\nAmazon Parrot\n  \n- Not neutered",
                            font="arial 15 ",
                            bg="seashell2",
                            fg="Black")
    other_descr1.place(x=245, y=95)

    other_descr2 = tk.Label(text="Ludwig is a young fellow with his whole life ahead\n\nof him. He is very active and curious, and\n\nenjoys exploring his surroundings. His behavior\n\ntowards humans is currently ambivalent. On one\n\nhand, he's very curious and approaches when\n\npeople get close, but on the other hand, he\n\ndoesn't like to be touched or have humans get\n\ntoo close. Ludwig is looking for a home with at\n\nleast one companion of his own kind, ideally\n\na female parrot. The aviary where Ludwig will be\n\nhoused should be at least 6m in length, 4m in\n\ndepth and 3m in height, if free flight is possible.",
                            font="arial 13",
                            bg="seashell2",
                            fg="dimgray")
    other_descr2.place(x=55, y=235)

    contact_button = tk.Button(text="Contact Shelter",
                               font='lucida 15 bold',
                               bd=0,
                               command=lambda:[clear_widgets(root) ,contact3()])
    contact_button.place(x=220, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("other")])
    next_button.place(x=60, y=650)

    back_button = tk.Button(text="<",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root), other3()])
    back_button.place(x=10, y=10)


# The following 9 pages (lines 921 - 1274) are the profile pages for the pets added to this app as examples.
# The user can get a first impression on the pet and decide if the pet is not for them or if they want to know more.
# It is only explained further in the first definition, since they are so similar.
def dog1():
    # This definiton from the helpers function stacks the image of the pet on the background image.
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rdog1_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    # These labels add some information on the pet.
    dog_name = tk.Label(text="Boogey ♂",
                        font="arial 22 bold",
                        bg="cadetblue4",
                        fg="Black")
    dog_name.place(x=165, y=408)

    dog_descr = tk.Label(text="Age:11 years old\n  \n- Vaccinated\n  \n- Microchipped\n\n- Neutered",
                         font="arial 16",
                         bg="seashell2",
                         fg="Black")
    dog_descr.place(x=152, y=490)

    # These 3 buttons give the user the choice to either see more information, see the next pet or go to the menu to look at other types of pets.
    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , dog1_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("dog")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bg="bisque3",
                            fg="black",
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(),pet_choice(root)])
    different_button.place(x=10, y=10)


def dog2():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rdog2_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    dog_name = tk.Label(text="Scotty ♂",
                        font="arial 22 bold",
                        bg="cadetblue4",
                        fg="Black")
    dog_name.place(x=172, y=408)

    dog_descr = tk.Label(text="Age:4 years old\n  \n- Dachshundmix\n  \n- Vaccinated\n\n- Neutered",
                         font="arial 16 ",
                         bg="seashell2",
                         fg="Black")
    dog_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , dog2_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("dog")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def dog3():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rdog3_11.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    dog_name = tk.Label(text="Goliath ♂",
                        font="arial 22 bold",
                        bg="cadetblue4",
                        fg="Black")
    dog_name.place(x=165, y=408)

    dog_descr = tk.Label(text="Age:3 years old\n  \n- Pomeranian\n  \n- Vaccinated\n\n- Not neutered",
                         font="arial 16",
                         bg="seashell2",
                         fg="Black")
    dog_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , dog3_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("dog")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def cat1():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rcat1_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    cat_name = tk.Label(text="Karl-Heinz ♂",
                        font="arial 22 bold",
                        bg="cadetblue4",
                        fg="Black")
    cat_name.place(x=155, y=408)

    cat_descr = tk.Label(text="Age: 12 years old\n\n- Vaccinated\n \n- Neutered",
                         font="arial 16",
                         bg="seashell2",
                         fg="Black")
    cat_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , cat1_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("cat")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def cat2():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rcat2_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    cat_name = tk.Label(text="Maggie ♀",
                        font="arial 22 bold",
                        bg="cadetblue4",
                        fg="Black")
    cat_name.place(x=165, y=408)

    cat_descr = tk.Label(text="Age: 12 years old\n  \n- Vaccinated\n  \n- Microchipped\n\n- Spayed",
                         font="arial 16 ",
                         bg="seashell2",
                         fg="Black")
    cat_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , cat2_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) ,  choose("cat")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def cat3():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rcat3_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    cat_name = tk.Label(text="Lilly ♀",
                        font="arial 20 bold",
                        bg="cadetblue4",
                        fg="Black")
    cat_name.place(x=190, y=408)

    cat_descr = tk.Label(text="Age:14 years old\n  \n- European Shorthair\n\n- Spayed",
                         font="arial 16 ",
                         bg="seashell2",
                         fg="Black")
    cat_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , cat3_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("cat")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def other1():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rother1_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    other_name = tk.Label(text="Agathe ♀",
                          font="arial 22 bold",
                          bg="cadetblue4",
                          fg="Black")
    other_name.place(x=167, y=408)

    other_descr = tk.Label(text="Age: unknown\n\n- Not vaccinated\n \n- Not microchipped\n \n- Not spayed",
                         font="arial 16 ",
                         bg="seashell2",
                         fg="Black")
    other_descr.place(x=152, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , other1_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("other")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def other2():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rother2_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    other_name = tk.Label(text="Ferrets ♀",
                          font="arial 22 bold",
                          bg="cadetblue4",
                          fg="Black")
    other_name.place(x=170, y=408)

    other_descr = tk.Label(text="Age: multiple\n  \n- Albino\n  \n- mother and offspring\n\n- spayed",
                           font="arial 16 ",
                           bg="seashell2",
                           fg="Black")
    other_descr.place(x=140, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , other2_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) ,  choose("other")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def other3():
    resizing_images(root,
                    'images/bg1.jpeg',
                    'images/rother3_1.jpeg',
                    screen_width,
                    screen_height,
                    220, 280, 103, 100)

    other_name = tk.Label(text="Ludwig ♂",
                          font="arial 22 bold",
                          bg="cadetblue4",
                          fg="Black")
    other_name.place(x=165, y=408)

    other_descr = tk.Label(text="Age: 3 years old\n  \n- Yellow-naped\nAmazon Parrot\n  \n- Not neutered",
                           font="arial 16",
                           bg="seashell2",
                           fg="Black")
    other_descr.place(x=155, y=490)

    info_button = tk.Button(text="More Info",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , other3_info()])
    info_button.place(x=265, y=650)

    next_button = tk.Button(text="Next",
                            font='lucida 15 bold',
                            bd=0,
                            command=lambda: [clear_widgets(root) , choose("other")])
    next_button.place(x=60, y=650)

    different_button = tk.Button(text="Match different pets",
                            font='lucida 14',
                            bd=0,
                            command=lambda: [clear_widgets(root) , pet_lists(), pet_choice(root)])
    different_button.place(x=10, y=10)


def choose(chosen_pet):
    # This operates which pet is shown to the user at what point.
    # It is a big if/else statement that shuffles through all the pages.
    clear_widgets(root)

    if chosen_pet == "dog":
        if options_dogs == []:
            no_more_dog()

        dog_selection = random.choice(options_dogs)

        if dog_selection == "dog1":
            options_dogs.remove("dog1")
            dog1()
        elif dog_selection == "dog2":
            options_dogs.remove("dog2")
            dog2()
        elif dog_selection == "dog3":
            options_dogs.remove("dog3")
            dog3()

    elif chosen_pet == "cat":
        if options_cats == []:
            no_more_cat()

        cat_selection = random.choice(options_cats)

        if cat_selection == "cat1":
            options_cats.remove("cat1")
            cat1()
        elif cat_selection == "cat2":
            options_cats.remove("cat2")
            cat2()
        elif cat_selection == "cat3":
            options_cats.remove("cat3")
            cat3()

    elif chosen_pet == "other":
        if options_others == []:
            no_more_other()

        other_selection = random.choice(options_others)

        if other_selection == "other1":
            options_others.remove("other1")
            other1()
        elif other_selection == "other2":
            options_others.remove("other2")
            other2()
        elif other_selection == "other3":
            options_others.remove("other3")
            other3()


def pet_choice(root):
    # With this page the user can take a look at some other types of pets after they have already defined in their profile, which pet-type they are looking for.
    global options_cats, options_dogs, options_others

    clear_widgets(root)


    set_background(root, 'images/lightsteelblue1.jpeg')

    # It adds a label.
    pet_name = tk.Label(text="What kind of pet are you looking for?",
                        font="century 20 bold",
                        bg="bisque3",
                        fg="Black",
                        relief="solid",
                        bd=2,
                        pady=4,
                        padx=1,
                        height=3,
                        width=27)
    pet_name.place(x=20, y=90)

    # And places three buttons for the three kinds of pets.
    dog_button = tk.Button(text="Dog",
                           font='lucida 20 ',
                           height=1,
                           width=8,
                           bd=0,
                           padx=2,
                           pady=2,
                           command=lambda: choose("dog"))
    dog_button.place(x=140, y=270)

    cat_button = tk.Button(text="Cat",
                           font='lucida 20',
                           height=1,
                           width=8,
                           bd=0,
                           padx=2,
                           pady=2,
                           command=lambda: choose("cat"))
    cat_button.place(x=140, y=370)

    other_button = tk.Button(text="Other",
                             font='lucida 20 ',
                             height=1,
                             width=8,
                             bd=0,
                             padx=2,
                             pady=2,
                             command=lambda: choose("other"))
    other_button.place(x=140, y=470)


def homepage(root):
    # This is the homepage, where the user starts out.
    pet_lists()
    # It calls pet_lists function to start by filling the lists with the pets, since that is needed after the next step.
    set_background(root, 'images/start1.jpeg')

    # A label is placed to welcome the user.
    name_label = tk.Label(root, text="Welcome to Pet-Match!",
                          font="Arial 24 bold",
                          bg="cadetblue4",
                          fg="black",
                          bd=2,
                          relief="solid",
                          padx=4,
                          pady=2,
                          height=3)
    name_label.place(relx=0.5, y=270, anchor="center")


    # The defninition places two buttons as options to either sign in or sign up as a new user.
    sign_up_button = tk.Button(root,
                             text="Sign up now!",
                             font='lucida 20',
                             bg="lightskyblue2",
                             fg="black",
                             bd=0,
                             padx=2,
                             pady=2,
                             command=lambda: sign_up())
    sign_up_button.place(relx=0.5, y=360, anchor="center")


    sign_in_button = tk.Button(root,
                             text="Sign back in!",
                             font='lucida 20',
                             bg="lightskyblue2",
                             fg="black",
                             bd=0,
                             padx=2,
                             pady=2,
                             command=lambda: sign_in())
    sign_in_button.place(relx=0.5, y=410, anchor="center")

homepage(root)
#This launches the homepage to start the app.

root.mainloop()