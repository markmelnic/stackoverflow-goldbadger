import time, enum, random, logging


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import NoSuchElementException


class DefaultLinksEnum(enum.Enum):
    home = "https://stackoverflow.com/"
    login = "https://stackoverflow.com/users/login"


class Timeouts:
    def srt() -> None:
        time.sleep(random.random() + random.randint(0, 1))

    def med() -> None:
        time.sleep(random.random() + random.randint(2, 3))

    def lng() -> None:
        time.sleep(random.random() + random.randint(4, 16))


class StackOverflowBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("log-level=3")
        chrome_options.add_experimental_option(
            "prefs", {"profile.default_content_setting_values.notifications": 2}
        )
        self.dv = webdriver.Chrome(
            chrome_options=chrome_options, executable_path=r"chromedriver.exe"
        )

    def login(self, email: str, password: str) -> None:
        self.dv.get(DefaultLinksEnum.login.value)

        self._cookies_handler()

        # email
        try:
            email_field = self.dv.find_element(By.NAME, "email")
        except:
            WebDriverWait(self.dv, 20).until(
                EC.frame_to_be_available_and_switch_to_it(
                    (
                        By.XPATH,
                        '//*[@id="content"]',
                    )
                )
            )
            email_field = self.dv.find_element(By.ID, "email")

        for ch in email:
            email_field.send_keys(ch)

        # password
        password_field = self.dv.find_element(By.NAME, "password")

        for ch in password:
            password_field.send_keys(ch)

        # sign in
        try:
            signin_button = self.dv.find_element(By.NAME, "submit-button")
            signin_button.click()
        except:
            html_body = self.dv.find_element(By.ID, "submit-button")
            html_body.send_keys(Keys.ENTER)

        Timeouts.med()

    def vote(self, link: str) -> None:
        """action: True to upvote, False to downvote"""

        Timeouts.med()

        page_index = 1
        while True:
            self.dv.get(link + f'&page={page_index}')

            posts = []
            for post in self.dv.find_elements(By.CLASS_NAME, "s-post-summary--content-title"):
                post_link = post.find_element(By.TAG_NAME, "a")
                posts.append(post_link.get_attribute("href"))

            for post_link in posts:
                self.dv.get(post_link)
                Timeouts.med()

                button = self.dv.find_element(
                    By.XPATH,
                    '//*[@id="question"]/div[2]/div[1]/div/button[1]'
                )
                button.click()

                Timeouts.med()

            page_index += 1

    def _cookies_handler(self) -> None:
        try:
            accept_button = self.dv.find_element(
                By.XPATH,
                "/html/body/div[4]/div/button[1]"
            )
            accept_button.click()
        except NoSuchElementException:
            pass

    def _dispose(self) -> None:
        self.dv.quit()
