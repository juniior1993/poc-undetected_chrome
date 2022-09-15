import os

from browserservice import BrowserService
from parserservice import ParserService


class HapagLloydHandle:
    def __init__(self, folder_to_save):
        self.folder_to_save = None
        self.bl = None
        self.folder_name = folder_to_save
        self.browser = BrowserService()
        self.browser.go_to_main_page()
        self.browser.close_cookie_options()

    def handle(self, bl):
        self.bl = bl
        self.folder_to_save = self.make_dir(bl)
        self.browser.get_bl(self.bl)
        page = self.browser.get_html_content()
        containers = ParserService().get_containers(page)
        self.save_html_content(page, 'bl_' + self.bl)

        for container in containers:
            self.container_handle(container)

    def container_handle(self, container):
        self.browser.get_container(container)
        container_html = self.browser.get_html_content()
        self.save_html_content(container_html, container)
        print(container + ' saved')

    def save_html_content(self, content, name):
        file = open(self.folder_to_save + name + '.html', 'w')
        file.write(content)
        file.close()

    def make_dir(self, document_name):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        if not os.path.exists(self.folder_name + document_name):
            os.makedirs(self.folder_name + document_name)

        return self.folder_name + document_name + '/'