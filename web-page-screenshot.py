#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import unittest
import time
import datetime
from datetime import datetime


chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX)

chrome.get('https://www.google.com')
print(chrome.title)
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
name = '{}.png'.format(timestamp)
chrome.save_screenshot(name)


chrome.quit()
firefox.quit()

