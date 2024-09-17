import os
import gdown
import tarfile
from modules.tklib import WindowNotify
from modules.parameters import *


class WindowDownloadData(WindowNotify):
    def __init__(self, root):
        super().__init__(root=root, title=TITLE_WINDOW_DOWNLOAD_DATA)
        self.download_and_extract_data()
        self.close()

    def download_and_extract_data(self):
        try:
            self.add_label(0, TEXT_DOWNLOAD_DATA_1)
            gdown.download(URL_GDOWN, PATH_FILE_TAR, quiet=True)

            self.add_label(1, TEXT_DOWNLOAD_DATA_2)
            with tarfile.open(PATH_FILE_TAR, "r") as tar:
                tar.extractall(PATH_FOLDER_PROJET)
            os.remove(PATH_FILE_TAR)

            self.add_label(2, TEXT_DOWNLOAD_DATA_3)
            self.after(100, self.destroy)

        except BaseException:
            self.add_label(0, TEXT_DOWNLOAD_DATA_4)
            self.after(3000,
                       func=lambda: (self.destroy(), self.root.destroy()))
