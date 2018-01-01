## **As of Jan. 1, 2017**

**script correctly handles**

- all quizzes (including drag and drop)
- all homepage rewards bonuses
- all pc searches
- all mobile searches

**script does not handle**

- extra searches on Microsoft Edge
- auto-updating, when the Bing website changes, it would be best to avoid manual updates 

RewardsBot
==========

Free Bing Rewards automator built in python using selenium web driver. It takes arguments such as a username and password (to allow for you to run multiple accounts in a single script).


Usage
=====

### Mac OS X

(Currently Firefox must be installed to make this work. See installation instructions [here](https://support.mozilla.org/en-US/kb/how-download-and-install-firefox-mac). I'm working on Chrome compatibility).

These instructions require installation of `homebrew`. Follow installation instructions [here](https://brew.sh/). After installing homebrew, run the following commands in a terminal.
```
git clone 'https://github.com/kathawala/RewardsBot.git'
cd RewardsBot
brew install python3 geckodriver
pip3 install selenium
python3 bing.py <username> <password>
```
It may be needed to run some commands as administrator (type `sudo` before the command and then type in your password when prompted). When running the script please replace `<username>` with your Bing username and `<password>` with your Bing password.

### Linux

Install Firefox, geckodriver, and python 3 using your distribution's package manager. Having done so, continue as follows.

Before running the script, please install selenium web driver:
```
pip install -U selenium
```
This might require you to download pip from your package manager. Also the above command might need to be entered with administrator privileges (using `sudo`).

To use the script, run the command:
```
python bing.py <username> <password>
```
If running in an environment with both python 2 and python 3 installed run `python3 bing.py` instead.

If you like, you can make the script executable by going to the directory "bing.py" is stored in and typing (with admin privileges if necessary):
```
chmod +x bing.py
bing.py <username> <password>
```
TODO
====

Would be nice to make this cross-platform and cross-browser (would be very easy to make this Chrome usable but I haven't got around to it).

I am planning to add a text file for configuration (using configparser). Would also like to accept the password without showing it on the screen (getpass?).
