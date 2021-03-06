from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import numpy as np


class InstagramBot(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        # Selenium xpaths
        # "//a[@href'accounts/login']"
        # "//input[@name='username']"
        # "//input[@password='password']"

        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(np.random.randint(2, 4))
        login_button = driver.find_element_by_xpath(
            "//a[@href='/accounts/login/?source=auth_switcher']"
        )
        login_button.click()
        time.sleep(np.random.randint(2, 4))
        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)
        password_elem = driver.find_element_by_xpath("//input[@name='password']")
        password_elem.clear()
        password_elem.send_keys(self.password)
        password_elem.send_keys(Keys.RETURN)
        time.sleep(np.random.randint(2, 4))

    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(10)

        # gathering photos
        pic_hrefs = []
        for i in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(np.random.randint(5, 7))
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name("a")
                # finding relevant hrefs
                hrefs_in_view = [
                    elem.get_attribute("href")
                    for elem in hrefs_in_view
                    if ".com/p/" in elem.get_attribute("href")
                ]
                # building list of unique photos
                [
                    pic_hrefs.append(href)
                    for href in hrefs_in_view
                    if href not in pic_hrefs
                ]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(np.random.randint(5, 7))
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(5, 7))
                like_button = lambda: driver.find_element_by_xpath(
                    '//span[@aria-label="Like"]'
                ).click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line(
                        "#"
                        + hashtag
                        + ": unique photos left: "
                        + str(unique_photos)
                        + " | Sleeping "
                        + str(second)
                    )
                    time.sleep(1)
            except Exception as e:
                time.sleep(np.random.randint(5, 7))
            unique_photos -= 1


if __name__ == "__main__":
    username = "test1"
    password = "test2"

    ig = InstagramBot(username, password)
    ig.login()
    while True:
        hashtags = [
            "python",
            "machinelearning",
            "algorithm",
            "artificialintelligence",
            "ai",
            "100daysofmlcode",
            "mathematics",
            "statistics",
            "actuary",
            "actuarial",
            "statistics",
            "html",
            "css",
            "javascript",
            "atom",
            "datascience",
            "analytics",
            "bigdata",
            "code",
            "coding",
            "jupyter",
        ]
        tag = random.choice(hashtags)
        ig.like_photo(tag)
