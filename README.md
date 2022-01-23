# Python-App-Blocker-With-Countdown
# Description
This is a program meant to boost productivity by closing user specified programs for a set amount of time. If the user were to open one the apps before the set time it automatically closes.

The user can add programs to be blocked by typing in the name.exe and clicking the "Add" button. For example if the user would want to block Spotify...

![Example1](https://user-images.githubusercontent.com/78455758/150659880-ec32e249-68ff-4c55-b764-d8330f23aba7.PNG)

If it was successfully added to the list of programs to be blocked it will be printed next to the "Blocking:" icon as shown above.

The time can be set using the entry boxes. They are seperated by hours(top box), minutes(middle box), seconds(bottom box). When the desired time has been inputted the user can start the timer by clicking the "Start" button which will invoke a seprate window that displays a countdown.

![Example2](https://user-images.githubusercontent.com/78455758/150659990-2d7f5c1e-9c0e-4429-b1e7-63554c2fe95c.PNG)

When the countdown is over the user will be presented with a message box notifying them that the blocked apps can now be opened.

![Example3](https://user-images.githubusercontent.com/78455758/150660077-653df517-7d48-493c-bb58-84b287a33b28.PNG)


# Requirements
Python was the only language used. The Tkinter library was used to create the graphical user interface and the psutil libary was used to monitor system process. In order to use psutil it must be installed. To do so use "pip install psutil" in the command line(exlcude the "") or add it through your IDE. Tkinter is more commonly used and often found already installed. 

# Credit
The countdown timer is inspired by one created by @ShaunHalverson on GitHub.

# Notes
Multiprocessing was used in order to keep track of time for the visual countdown and the one to block the apps seperately. This was done so the countdown timer will remain as accurate as possible but it is still a 2-5 seconds slower than the actual time. 
