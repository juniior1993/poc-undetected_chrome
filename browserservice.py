import undetected_chromedriver as browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = 'https://www.hapag-lloyd.com/'
BL_URL = 'en/online-business/track/track-by-booking-solution.html?blno='
CONTAINER_URL = 'en/online-business/track/track-by-booking-solution.html?view=S8510&container='


class BrowserService:

    def __init__(self):
        self.browser = browser.Chrome()

    def go_to_main_page(self):
        self.browser.get('https://www.hapag-lloyd.com/en/home.html')
        WebDriverWait(self.browser, 20).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[class*='save-preference-btn-handler']")
            )
        )

    def close_cookie_options(self):
        try:
            self.browser.find_element(By.CSS_SELECTOR, "[class*='save-preference-btn-handler']").click()
        finally:
            pass

    def get_bl(self, bl):
        self.browser.get(BASE_URL + BL_URL + bl)
        WebDriverWait(self.browser, 20).until(EC.title_contains('Tracing by'))

    def get_container(self, container):
        self.browser.get(BASE_URL + CONTAINER_URL + container)
        WebDriverWait(self.browser, 20).until(EC.title_contains('Tracing by'))

    def get_html_content(self):
        return self.browser.page_source
