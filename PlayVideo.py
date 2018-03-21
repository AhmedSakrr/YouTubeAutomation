from BasePage import BasePage


class PlayVideo(BasePage):
    def play_video(self):
        video = self.driver.find_elements_by_id("com.google.android.youtube:id/thumbnail").__getitem__(1)
        video.click()
        self.driver.back()
        playing_video = self.driver.find_element_by_id("com.google.android.youtube:id/player_view")
        # playing_video.clear()
        self.driver.swipe(1000, 1400, 60, 1400, 400)
