import os

import unittest
from unittest.main import main
from selenium import webdriver
import asyncio
from selenium.webdriver.common.by import By
import page
from papersData import papersData
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from requestsQUALIS import qualisDetector

#To silent webdriver_manager logs
os.environ['WDM_LOG_LEVEL'] = '0'



