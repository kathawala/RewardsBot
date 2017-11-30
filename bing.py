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

numSearches = 0
numMobileSearches = 4
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

def solveQuiz(num_points):
    num_questions = num_points/10
    for i in range(0,num_questions):
        for j in range(0,4):
            quizOptionElements = getQuizOptionElements()
            quizOptionElements[j].click()
            time.sleep(search_pause)

def getQuizOptionElements():
    elements = []
    for i in range(0,4):
        key = 'quizOption'+str(i)
        elements.append(driver.find_element_by_xpath(xpath[key]))
    return elements

def getOfferPoints():
    allOfferCardTitles = driver.find_elements_by_xpath(xpath['rewardsHomeCardTitle'])
    
    allOfferCardStatuses = driver.find_elements_by_xpath(xpath['rewardsHomeCardCheckmarkOrChevron'])
    allVisibleOfferCardStatuses = [x for x in allOfferCardStatuses if x.is_displayed()]

    allOfferCardPoints = driver.find_elements_by_xpath(xpath['rewardsHomeCardPoints'])
    allVisibleOfferCardPoints = [x for x in allOfferCardPoints if x.is_displayed()]
    
    for i in range(0,len(allVisibleOfferCardStatuses)):
        elem = allVisibleOfferCardStatuses[i]
        if "mee-icon-ChevronRight" in elem.get_attribute("class"):
            title_elem = allOfferCardTitles[i]

            # Got to clean this up
            if "Quiz" in title_elem.text:
                elem.click()
                time.sleep(search_pause)
                curr_tab = driver.window_handles[0]
                new_tab = driver.window_handles[-1]
                driver.switch_to_window(new_tab)
                num_points = allVisibleOfferCardPoints[i].text.replace(' POINTS','')
                solveQuiz(num_points)
                driver.close()
                driver.switch_to_window(curr_tab)
                getOfferPoints()
                return
            else:
                elem.click()
                time.sleep(search_pause)
                curr_tab = driver.window_handles[0]
                new_tab = driver.window_handles[-1]
                driver.switch_to_window(new_tab)
                driver.close()
                driver.switch_to_window(curr_tab)
                getOfferPoints()
                return
    
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
# driver = webdriver.Firefox()
# login()
# getOfferPoints()
# visitPCSearchPage()
# doSearches(numSearches, terms)
# driver.close()
# curr_tab = driver.window_handles[0]
# driver.switch_to_window(curr_tab)
# driver.close()

# Perform Mobile searches
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", ua_string)
driver = webdriver.Firefox(profile)
login()
visitMobileSearchPage()
doSearches(numMobileSearches, terms)
driver.close()
