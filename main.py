import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

import SignInPage
import HomePage
import LogOutPage
import PlayVideo


class LoginYoutubeTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {'platformName': 'Android', 'platformVersion': '8.0.0',
                        'deviceName': 'in-blr.headspin.io:8202', 'appPackage': 'com.google.android.youtube',
                        'appActivity': 'com.google.android.apps.youtube.app.application.Shell$HomeActivity',
                        'autoGrantPermissions': 'true'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        homepage = HomePage.HomePage(self.driver)
        homepage.click_on_account()
        homepage.login()

        signinpage = SignInPage.SignInPage(self.driver)
        signinpage.sign_in()

        playvideo = PlayVideo.PlayVideo(self.driver)
        playvideo.play_video()

        homepage = HomePage.HomePage(self.driver)
        homepage.click_on_account()

        logout = LogOutPage.LogOutPage(self.driver)
        logout.log_out()

    def tearDown(self):
        self.driver.quit()
        print "driver.quit"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginYoutubeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)