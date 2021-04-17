from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import cli
import chromedriver_binary


class Browser:

    base_url = 'https://www2.kickassanime.rs'

    def __init__(self, user_cnf):
        # TODO Figure out wsl shit
        if user_cnf['wsl']:
            self.bin_path = '/dist-packages/chromedriver_py/chromedriver_win32.exe'

        self.user_cnf = user_cnf
        self.options = Options()
        self.options.add_extension('extension_1_34_0_0.crx')

        self.options.add_argument("--autoplay-policy=no-user-gesture-required")

        self.driver = webdriver.Chrome(options=self.options)

    def watch_episode(self, ep):
        self.driver.get(self.base_url + ep)

        self.current_ep = self.base_url + ep

    def manage_url(self, ep_name):

        while self.browser_status():

            try:
                curr_url = self.driver.current_url

                if curr_url == self.current_ep:
                    continue

                if curr_url != self.current_ep:
                    parsed_url = self.parse_url(curr_url)

                if parsed_url in self.current_ep and 'episode' in curr_url:
                    self.current_ep = curr_url
                    cli.update_ep(ep_name,
                                  self.current_ep[len(self.base_url):])

            except:
                break

    def browser_status(self):
        try:
            self.driver.title
        except:
            return False

        return True

    def parse_url(self, url):
        url = url[len(self.base_url)+7:url.rindex('/')]

        return url[:url.rindex('-')]
