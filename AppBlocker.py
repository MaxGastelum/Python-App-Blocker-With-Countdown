import os
import psutil
import time
from tkinter import *
from tkinter import messagebox
import multiprocessing

#Global List to keep track of all the apps to be blocked
block_list = []

# Action function for add button
def add_program():

    #Temporary string to make sure fits criteria to be added to block list
    check = program_entry.get().strip()

    #In order to avoid duplicates or files that are not apps
    if check not in block_list and check[-4:] == '.exe':
        block_list.append(check)
        new_program = Label(mid_frame, text=check)
        new_program.config(bg= 'NavajoWhite2')
        new_program.pack(padx= 2, pady= 3)


# When start button is click ulti_count calls this function and a new window is displayed to show countdown
# Inspired by the time created by Shaun Halverson on GitHub
def display_count(in_hours, in_minutes, in_seconds):

    #Creating the new window and configuring it
    count_screen = Tk()
    count_screen.title('CountDown')
    count_screen.geometry('200x150')
    count_screen.config(bg='IndianRed4')

    #Countdown label
    count_label = Label(count_screen, text='Time Until Apps Unlock: ')
    count_label.pack(padx= 3, pady= 3)
    count_label.config(bg='snow2')

    #Creates StringVars in order to use .set function to update the timer
    hours = StringVar()
    minutes = StringVar()
    seconds = StringVar()

    #Gets values from function parameters to use as start point
    hours.set(in_hours)
    minutes.set(in_minutes)
    seconds.set(in_seconds)

    #Places the starting values in the Entry boxes
    hour_box = Entry(count_screen, width=2, font=('', 20, ''), textvariable=hours)
    hour_box.pack(padx= 2, pady= 2)

    minute_box = Entry(count_screen, width=2, font=('', 20, ''), textvariable=minutes)
    minute_box.pack(padx= 2, pady= 2)

    second_box = Entry(count_screen, width=2, font=('', 20, ''), textvariable=seconds)
    second_box.pack(padx= 2, pady= 2)

    #Safefy in case inputted spot was blank
    if str(hours.get()).strip() == '':
        hours.set('0')

    if str(minutes.get()).strip() == '':
        minutes.set('0')

    if str(seconds.get()).strip() == '':
        seconds.set('0')

    #Turns inputted time from main window into seconds
    clock_time = (int(hours.get()) * 3600) + (int(minutes.get()) * 60) + int(seconds.get())

    # Runs the countdown and updates the values until 0 seconds are left
    while clock_time > -1:

        tot_mins, tot_secs = divmod(clock_time, 60)

        tot_hours = 0

        if tot_mins > 60:
            tot_hours, tot_mins = divmod(tot_mins, 60)

        hours.set("{0:2d}".format(tot_hours))
        minutes.set("{0:2d}".format(tot_mins))
        seconds.set("{0:2d}".format(tot_secs))

        #Udaptes the window to display new values and uses the time module to asure its updating every second
        count_screen.update()
        time.sleep(1)

        #Sends a pop up message to user at 0 seconds
        if (clock_time == 0):
            messagebox.showinfo("", 'Apps Unblocked!')

        #Decrement by 1 second
        clock_time -= 1

    # Repeatedly dislays the window
    count_screen.mainloop()


# When start button is click this function is called from ulit_clock function which keeps track of how long to block
def internal_count(hours, minutes, seconds, block_list):

    if hours.strip() == '':
        hours = '0'

    if minutes.strip() == '':
        minutes = '0'

    if seconds.strip() == '':
        seconds = '0'

    # Represents the time at which the function should stop blocking the apps from opening
    clock_time = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds) + time.time()

    while (clock_time > time.time()):
        # For every element in the block list
        for program_name in block_list:
            # if program with same name as element is found using the iterator of current process it closes the program
            if program_name in (i.name() for i in psutil.process_iter()):
                # Force quits the program with the same name as the element
                os.system('TASKKILL /F /IM ' + program_name)
                continue


# When Start button is clicked this function is called
def ulti_count(hours, minutes, seconds):

    # Using multiprocessing to run both functions at the same time in order to keep both count downs accurate
    # to users requested time
    p1 = multiprocessing.Process(target=display_count, args=(hours, minutes, seconds))
    p2 = multiprocessing.Process(target=internal_count, args=(hours, minutes, seconds, block_list))

    p1.start()
    p2.start()


if __name__ == '__main__':

    #Main Window
    root = Tk()

    root.title('AppBlocker')
    root.config(bg='IndianRed4')

    # Top Frame
    top_frame = Frame(root)
    top_frame.pack(padx= 5, pady= 5)
    top_frame.config(bg='NavajoWhite2')

    program_label = Label(top_frame, text="Program to block: ")
    program_label.grid(row=0, column=0, padx= 3, pady= 2)
    program_label.config(bg='snow2')

    program_entry = Entry(top_frame)
    program_entry.grid(row=0, column=1, padx= 2, pady= 2)

    # Button calles the add_program function
    add_button = Button(top_frame, text='Add', bg='snow2', fg='IndianRed4', command=add_program)
    add_button.grid(row=0, column=2, padx= 2, pady= 2)

    # Mid Frame
    mid_frame = Frame(root)
    mid_frame.pack(padx= 5, pady= 5)
    mid_frame.config(bg='NavajoWhite2')

    blocked = Label(mid_frame, text="Blocking: ")
    blocked.pack(side=LEFT, padx= 2, pady= 3)
    blocked.config(bg='snow2')

    # Bottom Frame
    bottom_frame = Frame(root)
    bottom_frame.pack(padx= 5, pady= 5)
    bottom_frame.config(bg= 'NavajoWhite2')

    time_req_label = Label(bottom_frame, text='Time to keep Hours/Minutes/Seconds: ')
    time_req_label.pack(padx= 4, pady= 4)

    # Declaring StringVars
    hours = StringVar()
    minutes = StringVar()
    seconds = StringVar()

    # Setting the default time values to 0
    hours.set('0')
    minutes.set('0')
    seconds.set('0')

    hour_box = Entry(bottom_frame, width = 2, font=('', 20, ''), textvariable=hours)
    hour_box.pack(padx= 2, pady= 2)

    minute_box = Entry(bottom_frame, width = 2, font=('', 20, ''), textvariable=minutes)
    minute_box.pack(padx= 2, pady= 2)

    second_box = Entry(bottom_frame, width = 2, font=('', 20, ''), textvariable=seconds)
    second_box.pack(padx= 2, pady= 2)

    # Calls the multiprocessing function with the user inputted data from entries as arguemnts
    start_button = Button(bottom_frame, text='Start', bg='snow2', fg='IndianRed4', command=lambda: ulti_count(str(hours.get()), str(minutes.get()), str(seconds.get())))
    start_button.pack(padx= 2, pady= 2)

    # Repeatedly Displays window
    root.mainloop()
