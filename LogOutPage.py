import HomePage
from BasePage import BasePage


class LogOutPage(BasePage):
    def log_out(self):
        # sign_out = self.driver.find_element_by_android_uiautomator(
        #     'new UiScrollable(new UiSelector().scrollable(false).instance(0)).scrollIntoView(new UiSelector().'
        #     'text("Sign out").instance(0));')
        sign_out = self.driver.find_element_by_xpath("//*[contains(@text, 'Sign out')]")
        sign_out.click()

    #def verify_page(self):

