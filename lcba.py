# coding: UTF-8
import os
import unittest

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

from time import sleep

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
PATH1="/Users/mingjiang/test/lcb/a 768 "
class ComplexAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.3.1'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = PATH(
            '/Users/mingjiang/.jenkins/workspace/laicunba-android/bin/Activity_Start-release.apk'
        )

        self.d = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.d.quit()


    def test_scroll(self):
        sleep(3)
        self.d.find_element_by_id("com.laicunba.carfinancing:id/next").click()
        self.d.find_element_by_id("com.laicunba.carfinancing:id/next").click()
        self.d.find_element_by_id("com.laicunba.carfinancing:id/done").click() 
        self.d.find_element_by_id("com.laicunba.carfinancing:id/negativeButton").click()
        self.d.find_element_by_id("com.laicunba.carfinancing:id/btnHome").click()
        self.d.get_screenshot_as_file(PATH1+"account.jpg")
        self.d.find_element_by_id("com.laicunba.carfinancing:id/btnDiscover").click()
        self.d.get_screenshot_as_file(PATH1+"adiscover.jpg")
        self.d.find_element_by_id("com.laicunba.carfinancing:id/btnZone").click()
        self.d.get_screenshot_as_file(PATH1+"azone.jpg")
        self.d.find_element_by_id("com.laicunba.carfinancing:id/btnAccount").click()
        self.d.get_screenshot_as_file(PATH1+"ahome.jpg")



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ComplexAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
