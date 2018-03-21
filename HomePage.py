from BasePage import BasePage
import LogOutPage
from time import sleep


class HomePage(BasePage) :
    def login(self):
        try:
            logout = LogOutPage.LogOutPage(self.driver)
            logout.log_out()
            account_button2 = self.driver.find_element_by_id("com.google.android.youtube:id/mobile_topbar_avatar")
            account_button2.click()
            sleep(4)
        except:
            print "logout unsuccessful"

    def click_on_account(self):
        sleep(4)
        account_button = self.driver.find_element_by_id("com.google.android.youtube:id/mobile_topbar_avatar")
        account_button.click()
        sleep(4)
