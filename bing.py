#!/bin/env python

# A python script which makes numSearches number of searches to your Bing Account
# without you having to lift a finger :) Might take an argument as to number of
# searches in the future. Who knows?

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Want to replace the time.sleep calls with webdriverwait, but not yet
import time
import os.path
import subprocess
import getpath
import random
import argparse

# Argument parsing done here. Arguments accepted are username and password.
parser = argparse.ArgumentParser()
parser.add_argument("uname")
parser.add_argument("pswd")
args = parser.parse_args()
username = args.uname
password = args.pswd

# Default is 35 but can be changed. Usually all searches go through,
# but just to be safe, we add 5 extra
numSearches = 35
numMobileSearches = 20
auth_pause = 5
search_pause = 2

starturl = "https://account.live.com"
directory = getpath.get_script_dir()
# ua_string used to spoof mobile browser
ua_string = "Linux; U; Android 4.0.3; ko-kr; LG-L160L Build/IML74K) AppleWebkit/534.30 (KHTML, like Gecko)"

# Set up dictionary in script's path if necessary
def setupDictionary():
    cmd = directory + "/bing_dict.sh"
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    for line in proc.stdout:
        print (line.decode('ascii'))
    proc.wait()

# Returns a set of "n" random words to the caller
def getRandomWords(n):
    dictionary = open(directory + "/words", "r")
    words = set()
    last_pos = dictionary.tell()
    rand_words = list(dictionary)

    for i in range(0, n):
        word = random.choice(rand_words)
        words.add(word)

    dictionary.seek(last_pos)

    new_dict = open(directory + "/words.bak", "w")
    for line in dictionary:
        if line not in words:
            new_dict.write(line)

    os.remove(directory + "/words")
    os.rename(directory + "/words.bak", directory + "/words")
    return words

    
# Found by opening up firefox, using the developer console (F12) and clicking
# on elements. Must have firebug and firepath add-ons installed to do this.
xpaths = { 'usernameBox' : ".//*[@id='i0116']",
           'pswdBox' : ".//*[@id='i0118']",
           'submit' : ".//*[@id='idSIButton9']",
           'rewardsBox' : ".//*[@id='id_rc']",
           'search' : ".//*[@id='sb_form_q']",
           'searchButton' : ".//*[@id='sb_form_go']",
           'searchButtonMobile' : ".//*[@id='sbBtn']"
         }
         
driver = webdriver.Firefox()

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
    
# Authenticate Bing Rewards Account
def login(driver):
    driver.maximize_window()
    driver.get(starturl)
    send(xpaths['usernameBox'], username)
    send(xpaths['pswdBox'], password)
    click(xpaths['submit'])
    time.sleep(auth_pause)
    driver.get("http://www.bing.com")
    time.sleep(auth_pause)

# Perform web searches
login(driver)
setupDictionary()
terms = getRandomWords(numSearches)
for i in range(0, numSearches):
    clear(xpaths['search'])
    send(xpaths['search'], terms.pop())
    click(xpaths['searchButton'])
    time.sleep(search_pause)
driver.close()

# set up mobile browser
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", ua_string)
driver = webdriver.Firefox(profile)

# perform mobile searches
login(driver)
mobileTerms = getRandomWords(numMobileSearches)
for j in range(numMobileSearches):
    clear(xpaths['search'])
    send(xpaths['search'], mobileTerms.pop())
    if j > 0:
        click(xpaths['searchButton'])
    time.sleep(search_pause)
driver.close()
