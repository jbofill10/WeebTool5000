from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import chromedriver_binary


class Browser:

    base_url = 'https://www2.kickassanime.rs'

    def __init__(self, user_cnf):
        if user_cnf['wsl']:
            self.bin_path = '/dist-packages/chromedriver_py/chromedriver_win32.exe'

        self.user_cnf = user_cnf

        self.options = Options()
        self.options.add_extension('extension_1_34_0_0.crx')

        self.driver = webdriver.Chrome(options=self.options)

    def watch_episode(self, ep):
        self.driver.get(self.base_url + ep)
