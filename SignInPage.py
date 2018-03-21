from BasePage import BasePage


class SignInPage(BasePage):
    def sign_in(self):
        sign_in_button = self.driver.find_element_by_id("com.google.android.youtube:id/button")
        sign_in_button.click()

        choose_account = self.driver.find_element_by_id("com.google.android.youtube:id/name")
        choose_account.click()
        print "login successfully"
