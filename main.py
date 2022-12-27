import time
import turtle
import pandas
from tkinter import messagebox

# Turtle screen setup
screen = turtle.Screen()
screen.title("Skyrim")
screen.setup(width=1600, height=1148)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
image = "skyrim.gif"
icon = "map_icon.gif"
screen.addshape(image)
turtle.shape(image)
# FONT = ("Arial", 20, "bold")
FONT = ("Verdana", 15, "bold")

# Use pandas to read csv file with locations
# data is a panda data frame object
# columns are panda series
data = pandas.read_csv("Skyrim.csv")

# turtle marker
marker = turtle.Turtle()
marker.color("#FBFF00")

marker.hideturtle()
marker.penup()


def draw_point():
    marker.begin_fill()
    marker.circle(8)
    marker.end_fill()


# Used to get coordinates of locations for Skyrim.csv
def get_mouse_click_coor(x, y):
    marker.goto(x, y)
    print(x, y)
    draw_point()


# Used to get coordinates of locations for Skyrim.csv
def get_user_location():
    turtle.onscreenclick(get_mouse_click_coor)


# get_user_location()

prompt_user_again = True
while prompt_user_again:
    i = 0
    user_input = screen.textinput(title="Enter a location:", prompt="Enter a location:").title()
    if user_input == "Exit":
        exit(0)
    else:
        city = data[data.name == user_input]
        for name in data.name:
            if user_input == name:
                # print("Found!")
                # print(name)
                marker.goto(int(city.x), int(city.y))
                draw_point()
                marker.goto(int(city.x - 25), int(city.y - 20))
                marker.write(name, font=FONT)
            else:
                i += 1
                if i == 223:
                    messagebox.showinfo("Error", "Location Not Found")


turtle.mainloop()

