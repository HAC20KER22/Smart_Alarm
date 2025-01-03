# Smart_Alarm

This project is basically designed for people who forget a lot of things.
You can set this alarm and just wait for it to pop up.
This tool only runs on windows and it needs to be configured so that it can run as background process.

The program is executed and it checks wether any alarm time as already passed by, if it does the alarm rings and then shows the user. 

For this you will need to configure a few things:
1. You need specific python modules
   pip install pyqt5
   pip install pyqt5-tools
2. You need to add the background.py file in the Task scheduler to run every 15mins in the background so as to check which alarms have gone of.

