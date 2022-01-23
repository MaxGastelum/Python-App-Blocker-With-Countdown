# Python-App-Blocker-With-Countdown
# Description
This is a program meant to boost productivity by closing user specified programs for a set amount of time. 

The user can add programs to be blocked by typing in the name.exe and clicking the "Add" button. For example if the user would want to block Spotify...
![Example1](https://user-images.githubusercontent.com/78455758/150659880-ec32e249-68ff-4c55-b764-d8330f23aba7.PNG)
If it was successfully added to the list of programs to be blocked it will be printed next to the "Blocking:" icon as shown above.





Python was the only language used with the addition of the Tkinter library to create the graphical user interface and psutil libary was used to monitor system process. In order to use psutil it must be installed. To do so use the "pip install psutil" in the command line(exlcude the ""). Tkinter is more commonly used and often found already installed. 

# Credit
The countdown timer is inspired by one created by @ShaunHalverson on GitHub.

# Notes
Multiprocessing was used in order to keep track of time for the visual countdown and the one to block the apps seperately. This was done so the countdown timer will remain as accurate as possible but it is still a 2-5 seconds slower than the actual time. 
