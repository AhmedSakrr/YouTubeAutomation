from BasePage import BasePage
import LogOutPage
from time import sleep


class HomePage(BasePage) :
    def login(self):
        try:
            logout = LogOutPage.LogOutPage(self.driver)
            homepage = logout.log_out()
            homepage.click_on_account()
        except:
            print "logout unsuccessful"

    def click_on_account(self):
        account_button = self.driver.find_element_by_id("com.google.android.youtube:id/mobile_topbar_avatar")
        account_button.click()
        if account_button.is_displayed():
            account_button.click()

