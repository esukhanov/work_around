#!/usr/bin/python
#  -*- coding: utf-8 -*-

from  selenium import webdriver
import time
import logging
from appium import webdriver
logging.basicConfig(filename="test.log", level=logging.INFO)
logger = logging.getLogger()


capabilities = {'server':'CONFIG_UUID=4d53a683-1077-411d-84f1-da0e6a792243',
                'seleniumProtocol':'WebDriver',
                'browserName':'chrome',
                'maxInstances':'1',
                'platformName':'LINUX',
                'version':'67.0.3396.99',
                'applicationName':'',
                'platform':'LINUX'}



desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['automationName'] = 'uiautomator2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['app'] = PATH('../../../apps/selendroid-test-app.apk')

self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
els = self.driver.find_elements_by_android_uiautomator('new UiSelector().clickable(true)')
self.assertIsInstance(els, list)







