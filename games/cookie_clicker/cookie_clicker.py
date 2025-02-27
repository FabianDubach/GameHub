from tkinter import *
from tkinter import ttk

cookie_count = 0

autoclicker_price = 15
bought_autoclicker = 0

mine_price = 100
bought_mine = 0

driller_price = 1100
bought_driller = 0


# Click on cookie
def click():
    global cookie_count
    cookie_count += 1
    cookie_updater()

# Updates cookie count
def cookie_updater():
    if cookie_count < 1000:
        update_cookies.configure(text=f'Cookies: {round(cookie_count)}')
    elif cookie_count >= 1000 and cookie_count < 1000000:
        update_cookies.configure(text=f'Cookies: {round((cookie_count / 1000), 2)}K')
    elif cookie_count >= 1000000:
        update_cookies.configure(text=f'Cookies: {round((cookie_count / 1000000), 2)}M')

# Message: Not enough money
def not_enough_money(x):
    message.configure(text=f'You need {round(x)} more cookies!')
    message.after(2000, clear_message)

def clear_message():
    message.configure(text=' ')
    

# Item: Autoclicker
def buy_autoclicker():
    global cookie_count
    global bought_autoclicker
    global autoclicker_price
    if cookie_count >= autoclicker_price:
        cookie_count -= autoclicker_price
        bought_autoclicker += 1
        autoclicker_price *= 1.15
        autoclicker_price = round(autoclicker_price)
        autoclicker_button.configure(text=f'Buy Autoclicker! (Cost: {autoclicker_price}, Owned: {bought_autoclicker}, CPS: 0.1)')
        autoclicker_loop()
    else:
        cookies_needed = autoclicker_price - cookie_count
        not_enough_money(cookies_needed)
        
def autoclicker_loop():
        global cookie_count
        cookie_count += 0.1
        cookie_updater()
        root.after(1000, autoclicker_loop)


# Item: Mine
def buy_mine():
    global cookie_count
    global bought_mine
    global mine_price
    if cookie_count >= mine_price:
        cookie_count -= mine_price
        bought_mine += 1
        mine_price *= 1.15
        mine_price = round(mine_price)
        mine_button.configure(text=f'Buy Mine! (Cost: {mine_price}, Owned: {bought_mine}, CPS: 1)')
        mine_loop()
    else:
        cookies_needed = mine_price - cookie_count
        not_enough_money(cookies_needed)
        
def mine_loop():
        global cookie_count
        cookie_count += 1
        cookie_updater()
        root.after(1000, mine_loop)
        
        
# Item: Driller
def buy_driller():
    global cookie_count
    global bought_driller
    global driller_price
    if cookie_count >= driller_price:
        cookie_count -= driller_price
        bought_driller += 1
        driller_price *= 1.15
        driller_price = round(driller_price)
        driller_button.configure(text=f'Buy Driller! (Cost: {driller_price}, Owned: {bought_driller}, CPS: 8)')
        driller_loop()
    else:
        cookies_needed = driller_price - cookie_count
        not_enough_money(cookies_needed)
        
def driller_loop():
        global cookie_count
        cookie_count += 8
        cookie_updater()
        root.after(1000, driller_loop)


# Creates body for game
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()

# Title
ttk.Label(frm, text='Cookie Clicker by Fabian Dubach').grid(column=0, row=0)

# Click button
cookie_picture = PhotoImage(file = r"games\\cookie_clicker\\cookie.gif")
ttk.Button(frm, command=click, image=cookie_picture).grid(column=0, row=1)

# Cookie counter
update_cookies = ttk.Label(frm, text='Cookies: 0')
update_cookies.grid(column=0, row=2)

# Buy Autoclicker
autoclicker_button = ttk.Button(frm, text=f'Buy Autoclicker! (Cost: {autoclicker_price}, Owned: {bought_autoclicker}, CPS: 0.1)', command=buy_autoclicker)
autoclicker_button.grid(column=0, row=3)

# Buy Mine
mine_button = ttk.Button(frm, text=f'Buy Mine! (Cost: {mine_price}, Owned: {bought_mine}, CPS: 1)', command=buy_mine)
mine_button.grid(column=0, row=4)

# Buy Driller
driller_button = ttk.Button(frm, text=f'Buy Driller! (Cost: {driller_price}, Owned: {bought_driller}, CPS: 8)', command=buy_driller)
driller_button.grid(column=0, row=5)

# Quit game
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=6)

# Message
message = ttk.Label(frm, text=' ')
message.grid(column=0, row=7)

root.mainloop()