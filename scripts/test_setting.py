import pytest
import os,sys,pytest
sys.path.append(os.getcwd())

from base.base_analyze import yml


def analyze_yml(func_name):
    d = yml("setting_data")
    # print(d[func_name])
    return d[func_name]

class Test_analyse:

    @pytest.mark.parametrize("content",analyze_yml("test_english"))
    def test_english(self,content):
        print(content)

    # @pytest.mark.parametrize("content",test_analyze_yml("test_chinnse"))
    # def test_chinnse(self,content):
    #     print(content)
