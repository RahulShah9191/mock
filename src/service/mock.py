import json
import os.path

from core.constant import *
from os import listdir
from os.path import isfile, join

from src.dto.mockobject import MockObject


class Mock(object):

    def __init__(self):
        self.mock_obj = []
        self.mock_files = []
        self.__get_all_mocks()
        self.__get_mock_objects()
        pass

    def __get_all_mocks(self, path=MOCK_DIR):
        try:
            self.mock_files = [f for f in listdir(path) if isfile(join(path, f))]
        except Exception as e:
            print(f"Error in reading mock files from path: {path}")
            raise e

    def __get_mock_objects(self, path=MOCK_DIR):
        try:
            if self.mock_files:
                mock_obj = []
                for file in self.mock_files:
                    print("Generating mock object from file: ", file)
                    with open(os.path.join(path,file), 'r') as file:
                        mock_dict = json.load(file)
                        mock_obj.append(MockObject.parse_obj(mock_dict))
                self.mock_obj = mock_obj
        except Exception as e:
            print(f"Error in parsing mock objects from file with error: {e}")
            raise e
