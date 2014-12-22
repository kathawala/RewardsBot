from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import os.path
import random

# These fields need to be set before the bot can work.
# Config file is in progress, but for now, these variables
# must be set.
username = 
password =


# Specifies how many searches to do (best to put a few over the number
# you wants as some are not counted because they might be repeat searches
numSearches = 40

starturl = "https://account.live.com"

# Function which takes as many words at random out of a dictionary
# file as specified by variable "numSearches". The dictionary file
# is hard-coded here, but config file will allow user to choose
# Unix users should be able to find a dictionary file in
# the directory "/usr/share/dict/"
def randomWords():
    dictionary = open("/home/farhan/bin/words", "r")
    words = set()
    last_pos = dictionary.tell()
    rand_words = list(dictionary)

    for i in range(0, numSearches):
        word = random.choice(rand_words)
        words.add(word)

    dictionary.seek(last_pos)

    new_dict = open("/home/farhan/bin/words.bak", "w")
    for line in dictionary:
        if line not in words:
            new_dict.write(line)

    os.remove("/home/farhan/bin/words")
    os.rename("/home/farhan/bin/words.bak", "/home/farhan/bin/words")
    return words

    
# Found by opening up firefox, using the developer console (F12) and clicking
# on elements. Must have firebug and firepath add-ons installed to do this.
xpaths = { 'usernameBox' : ".//*[@id='i0116']",
           'pswdBox' : ".//*[@id='i0118']",
           'submit' : ".//*[@id='idSIButton9']",
           'preferences' : ".//*[@id='account_general']/div[5]/input[6]",
           'search' : ".//*[@id='sb_form_q']",
           'searchButton' : ".//*[@id='sb_form_go']"
         }

driver = webdriver.Firefox()

# Following functions are exception-handling wrappers for
# selenium functions. They make the driver script code easier
# to read. 

def send(xpath, value):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
        exit(1)
    elem.send_keys(value)

def click(xpath):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
        exit(1)
    elem.click()

def clear(xpath):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
        exit(1)
    elem.clear()
    

# Here begins the scripted moves for the webdriver:

driver.maximize_window()
driver.get(starturl)

# Log in
send(xpaths['usernameBox'], username)
send(xpaths['pswdBox'], password)
click(xpaths['submit'])

# sleep needed to wait for bing authentication, really isn't too slow
time.sleep(5)
terms = randomWords()

# Sleep needed here to ensure authentication transfers successfully
driver.get("http://www.bing.com")
time.sleep(5)

# Makes sure the login did not fail. A newly created account will not have 0 points,
# so this check should not fail if login is successful.
element = driver.find_element_by_xpath(xpaths['rewardsBox'])
if (element.text == "0"):
    print ("Login unsuccessful. Please check your username and password")
    exit(1)


for i in range(0, numSearches):
    clear(xpaths['search'])
    send(xpaths['search'], terms.pop())
    click(xpaths['searchButton'])
