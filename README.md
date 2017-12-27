## **As of Dec. 27, 2017**

**script correctly handles**

- all quizzes (including drag and drop)
- all homepage rewards bonuses
- all pc searches
- all mobile searches

**script does not handle**

- extra searches on Microsoft Edge

RewardsBot
==========

Free Bing Rewards automator built in python using selenium web driver. It takes arguments such as a username and password (to allow for you to run multiple accounts in a single script).


Usage
=====

Requirements: Firefox (adding Chrome support soon), python3, pip

Before running the script, please install selenium web driver:

    pip install -U selenium

This might require you to download pip from your package manager. Also the above command might need to be entered with administrator privileges.

To use the script, type the command:

    python bing.py <username> <password>
    
If you like, you can make the script executable by going to the directory "bing.py" is stored in and typing (with admin privileges if necessary):

    chmod +x bing.py
    bing.py <username> <password>
    
If running in an environment with both python2 and python3 installed (like Mac OS X) type "python3 bing.py" instead.


TODO
====

Would be nice to make this cross-platform and cross-browser (would be very easy to make this Chrome usable but I haven't got around to it).

I am planning to add a text file for configuration (using configparser). Would also like to accept the password without showing it on the screen (getpass?).
