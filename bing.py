#!/bin/env python

# A python script which makes numSearches number of searches to your Bing Account
# without you having to lift a finger :) Might take an argument as to number of
# searches in the future. Who knows?

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Want to replace the time.sleep calls with webdriverwait, but not yet
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
import time
import os
import getpath
import random
import argparse
from BingSelectors import xpath, css

numSearches = 30
auth_pause = 10
search_pause = 5

parser = argparse.ArgumentParser()
parser.add_argument("uname")
parser.add_argument("pswd")
args = parser.parse_args()
username = args.uname
password = args.pswd

starturl = "https://account.microsoft.com/rewards/dashboard"
directory = getpath.get_script_dir()

def getRandomQueries(n):
    
    with open(os.path.join(directory, "queries"), "r") as f:
        all_words = list(f)

    queries= set()
    while len(queries) < n:
        queries.add(random.choice(all_words).rstrip())
    return queries

driver = webdriver.Firefox()
#driver.set_window_size(1120, 550)

def send(xpath, value):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
    elem.send_keys(value)

def click(xpath):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
    elem.click()

def clickCSS(selector):
    try:
        elem = driver.find_element_by_css_selector(selector)
    except NoSuchElementException:
        print("Couldn't find element specified by css selector: {x}".format(x=selector))
    elem.click()

def clear(xpath):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print ("Couldn't find element specified by xpath: {x}".format(x=xpath))
    elem.clear()
    
# Authenticate Bing Rewards Account
def login(driver):
    driver.maximize_window()
    driver.get(starturl)
    click(xpath['signInLink'])
    time.sleep(auth_pause/2)
    send(xpath['usernameBox'], username)
    click(xpath['submit'])
    time.sleep(auth_pause/2)
    send(xpath['pswdBox'], password)
    click(xpath['submit'])
    time.sleep(auth_pause/2)
    click(xpath['searchLink'])
    time.sleep(auth_pause/2)

    # switches focus to the new tab where the search window has opened up
    new_tab = driver.window_handles[-1]
    driver.switch_to_window(new_tab)


# Perform searches
login(driver)
# setupDictionary()
terms = getRandomQueries(numSearches)
for i in range(0, numSearches):
    clear(xpath['search'])
    send(xpath['search'], terms.pop())
    click(xpath['searchButton'])
    time.sleep(search_pause)
driver.close()