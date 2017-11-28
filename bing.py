#!/bin/env python

# A python script which makes numSearches number of searches to your Bing Account
# without you having to lift a finger :) Might take an argument as to number of
# searches in the future. Who knows?

import time
import os
import random
import argparse
import getpath

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# Want to replace the time.sleep calls with webdriverwait, but not yet
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
from BingSelectors import xpath

numSearches = 30
numMobileSearches = 20
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

# should be a config option to set this
ua_string = "Mozilla/5.0 (Android 5.0.1; Mobile; rv:58.0) Gecko/58.0 Firefox/58.0"


def getRandomQueries(num_queries):
    with open(os.path.join(directory, "queries"), "r") as query_txtfile:
        all_words = list(query_txtfile)

    queries = set()
    while len(queries) < num_queries:
        queries.add(random.choice(all_words).rstrip())
    return queries

# Make a "Driver" class to fit these into
def send(xpath, value):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print("Couldn't find element specified by xpath: {x}".format(x=xpath))
    elem.send_keys(value)

def click(xpath):
    try:
        elem = driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        print("Couldn't find element specified by xpath: {x}".format(x=xpath))
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
        print("Couldn't find element specified by xpath: {x}".format(x=xpath))
    elem.clear()

# Authenticate Bing Rewards Account
def login():
    driver.maximize_window()
    driver.get(starturl)
    click(xpath['signInLink'])
    time.sleep(auth_pause/2)
    send(xpath['usernameBox'], username)
    click(xpath['submit'])
    time.sleep(auth_pause/4)
    send(xpath['pswdBox'], password)
    click(xpath['submit'])
    time.sleep(auth_pause)

def visitPCSearchPage():
    click(xpath['searchLink'])
    time.sleep(auth_pause/2)

    # switches focus to the new tab where the search window has opened up
    new_tab = driver.window_handles[-1]
    driver.switch_to_window(new_tab)

def visitMobileSearchPage():
    click(xpath['searchLinkMobile'])
    time.sleep(auth_pause/2)

def doSearches(num_searches, search_queries):
    for i in range(0, num_searches):
        clear(xpath['search'])
        send(xpath['search'], search_queries.pop())
        click(xpath['searchButton'])
        time.sleep(search_pause)


# Get search terms
terms = getRandomQueries(numSearches+numMobileSearches)

# Perform PC searches
driver = webdriver.Firefox()
login()
visitPCSearchPage()
doSearches(numSearches, terms)
driver.close()

# Perform Mobile searches
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", ua_string)
driver = webdriver.Firefox(profile)
login()
visitMobileSearchPage()
doSearches(numMobileSearches, terms)
driver.close()
