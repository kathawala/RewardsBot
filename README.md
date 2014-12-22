RewardsBot
==========

Free Bing Rewards automator built in python using selenium web driver. This is a functional WIP. Currently, most settings configuration must be done by changing variables in the program itself. I'm working on making such changes available through a text config file or through command line input/arguments


Usage
=====

Currently the bing.py file needs to be edited to include username and password of the account to be automated.

In addition, before running the script, please install selenium web driver:

    pip install -U selenium

This might require you to download pip from your package manager. Also the above command might need to be entered with administrator privileges.

To use the script, download these files to some directory in your path and simply type:

    bing
    

TODO
====

I am planning to add a text file for configuration (using configparser). I would also like to allow the user to send arguments and use options. For instance, making the number of Searches an option and having an argument be the username (then password could be sent using getpass).

Instead of arguments, I would be open to user input dialogs, for instance a prompt asking "How many searches would you like to do?" and then using the user's input in the program.

Ideally, if called with no arguments or options, the program should default to config file information. If called with arguments or options, the program should use those to override the config file information.
