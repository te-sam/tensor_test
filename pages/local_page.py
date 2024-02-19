from pages.download_page import DownloadPage
import os
import urllib.request
import re

class LocalPage(DownloadPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = self.get_link_exe
        self.text = self.get_text_link_exe
        self.file_name = os.path.basename(self.url)

    def download_exe(self):
        urllib.request.urlretrieve(self.url, self.file_name)
    def get_initial_size(self):
        return float(re.search(r'Exe\s+([\d.]+)', self.text).group(1))
    def get_result_size(self):
        return round(os.path.getsize(self.file_name) / 1024 / 1024, 2)
    def check_file(self):
        return os.path.exists(self.file_name)