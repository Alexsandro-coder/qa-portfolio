from playwright.sync_api import Page


class BasePage:

    def __init__(self, page: Page):
        self.page = page
        self.error_alert = page.locator("[data-test='error']")
        self.title= page.locator("[data-test='title']")