import argparse
import os

class DirectoryTreeGenerator():
    def __init__(self):
        self.path = None
        self.current_directory = os.getcwd()

    def get_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-p", "--path", default=self.current_directory)