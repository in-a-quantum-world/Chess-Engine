#chess nea start screen
import sqlite3
import mysql.connector
import pygame
import pygame_widgets as pw
from pygame_widgets.button import Button as B
from pygame_widgets.textbox import TextBox

import random
import time
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw() #to hide the main window

pygame.init()
#----------------------handling screens--------------------
current = "start_screen"
very_start_screen = pygame.display.set_mode((1000,1000))
login_screen = pygame.display.set_mode((1000,1000))
signup_screen = pygame.display.set_mode((1000,1000))
start_screen = pygame.display.set_mode((1000,1000))
home_screen = pygame.display.set_mode((1000,1000))
options_screen = pygame.display.set_mode((1000,1000))
clock = pygame.time.Clock()
bg = pygame.Surface((1000,1000))
font = pygame.font.SysFont("Arial",35)

cnx = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "whyamiDoingThis@010101",
    )
#cursor = connection.cursor()
mycursor = cnx.cursor(buffered=True)
#---------------------------------
#textboxes
username_textbox = TextBox(login_screen, 250, 250, 300, 50, fontSize=30)
password_textbox = TextBox(login_screen, 550, 250, 300, 50, fontSize=30)
#--------------------------------new user--------------------------
def sign_up():
    mycursor.execute("USE chess_db;")
     
    valid_username = False
    sql_username = "SELECT username FROM chess_users WHERE username = %s"
        #try:
    user_input_username = input("enter username: ")
    user_username = [(user_input_username)]

    while valid_username == False:
        mycursor.execute("SELECT username FROM chess_users WHERE username = (%s)",user_username)
        count = 0
        for x in mycursor:
            print(x)
            count += 1
        if count > 0:
            user_username = input("Please enter a different username, this has been taken: ")
        else:
            valid_username = True
    
    """
    sql_select = "SELECT userID FROM chess_users"
    try:
        user_id_list = mycursor.execute(sql_select)
        
        max_id = max(user_id_list)
        user_userid = max_id + 1
    except:
        user_userid = 1
        
    
    """
    user_password = input("Enter a password: ")
    #mycursor.reset()
    sql_insert = "INSERT INTO chess_users(username,password) VALUES (%s,%s,%s)"
    user_vals = (user_username,user_password)
    mycursor.execute(sql_insert,user_vals)
    curr_user = Person()
    print("done?")
    cnx.commit()
    
def error_screen(message):
    messagebox.showinfo(message)


def try_login():
    print("gone to try login")
    user_input_username = username_textbox.getText()
    user_username = [(user_input_username)]
    pwd = input("Enter your password: ")
    pwd = password_textbox.getText()
    print("username entered is {}, password {}".format(user_input_username,pwd))
    sql_get_userid = "SELECT userid FROM chess_users WHERE username=(%s)"
        
    try:
        mycursor.execute(sql_get_userid,user_username)
        for x in mycursor:
            user_id = x
        
        sql_get_pwd = "SELECT password FROM chess_users WHERE username = (%s)"
        mycursor.execute(sql_get_pwd,user_username)
        try:
            for x in mycursor:
                print(x)
                length = len(str(x))
                print("length is",length)
                z = (str(x))[2:length - 3]
                print("z is",z)
                if pwd == z:
                    print("here")
                    all_valid = True
                    print("you have logged in")
                    break
                elif pwd != z:
                    z = (str(x))[2:length-2]
                    if pwd == z:
                        print("here")
                        all_valid = True
                        print("you have logged in")
                        break
                        #instantiate person class
                        #actually return true so a person class can then be instantiated etc
                    temp(user_id,username)
        except:
            print("error, no password found")
            main()
        
    except:
        print("error. username not found")
        main()
 
#----------buttons-----------------------------------
view_account_info_button = B(
    home_screen, 600, 500, 200, 100, text='view account info',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)
start_game_button = B(
    home_screen, 150, 500, 200, 100, text='start game',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)

random_move_player_button = B(
    options_screen, 600, 500, 200, 100, text='play against randomly generated moves',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)

engine_player_button  = B(
    options_screen, 600, 500, 200, 100, text='play against engine',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)

start_to_home_button  = B(
    start_screen, 600, 500, 200, 100, text='go back home',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)

#the screen for this options to start button still needs to be created
options_to_start_button = B(
    options_screen, 600, 500, 200, 100, text='choose a different option',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = print('Click')
)

submit_details_button = B(
    login_screen, 600, 300, 200, 100, text='submit',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (200,200 , 200), radius=20,
    onClick = try_login()
)

        
def login():
    login_screen.fill((50,100,70))
    global events
    global current
    current == "login"
    """
    options_to_start_button.hide()
    engine_player_button.hide()
    start_to_home_button.hide()
    start_game_button.hide()
    view_account_info_button.hide()
    random_move_player_button.hide()
    login_button.hide()
    sign_up_button.hide()
    """
    submit_button.listen(events)
    submit_button.show()
    username_textbox.listen(events)
    username_textbox.draw()
    password_textbox.listen(events)
    password_textbox.draw()
    pygame.display.update()
    pw.update(events)
    all_valid = False
#----------------------------------------------------
#PYGAME BUTTONS
login_button = B(
    login_screen, 150, 500, 200, 100, text='Login',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = login()
)

sign_up_button = B(
    login_screen, 600, 500, 200, 100, text='Sign up',
    fontSize = 50, margin = 20,
    inactiveColour = (255,200, 0),
    pressedColour = (0,200 , 200), radius=20,
    onClick = sign_up()
)
def very_first_screen():
    pass

def main():
    running = True
    count = 0
    click_list = []
    very_start_screen.fill((0,100,100))
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                running = False
            if e.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(e.key)}")
            elif e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                """
                if count == 0:
                    if (x <= 700 and x >= 500) and (y <= 550 and y >= 450):
                        print("sign up pressed")
                    elif (x <= 700 and x >= 500) and (y <= 550 and y >= 450):
                        print("login pressed")
                """
                        #sign up vutton pressed, go to function
                #600, 500, 200, 100
                #check location of button pressed and act accordingly - go to login or sign up
                #use a while loop - condition for termination is if they press on the locations of one of the buttons
        
        if current == "start_screen":
            very_start_screen.fill((0,100,70))

            username_textbox.hide()
            password_textbox.hide()
            login_button.listen(events)
            login_button.show()
            sign_up_button.listen(events)
            sign_up_button.show()
            submit_details_button.hide()
            options_to_start_button.hide()
            engine_player_button.hide()
            start_to_home_button.hide()
            start_game_button.hide()
            view_account_info_button.hide()
            random_move_player_button.hide()
    
        pw.update(events)
        pygame.display.update()
        
if __name__ == "__main__":
    main()