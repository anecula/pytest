#!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import unittest
import time
import datetime
from datetime import datetime


HUB_HOST = os.environ.get('HUB_HOST')
HUB_PORT = os.environ.get('HUB_PORT')

EXECUTOR = 'http://{host}:{port}/wd/hub'.format(host=HUB_HOST, port=HUB_PORT)

print(EXECUTOR)


chrome = webdriver.Remote(
          command_executor=EXECUTOR,
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor=EXECUTOR,
          desired_capabilities=DesiredCapabilities.FIREFOX)

chrome.get('https://www.google.com')
print(chrome.title)
timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
name = '{}.png'.format(timestamp)
chrome.save_screenshot(name)


chrome.quit()
firefox.quit()

