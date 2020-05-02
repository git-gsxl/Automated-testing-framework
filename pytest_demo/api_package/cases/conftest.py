import pytest
import re
from pytest_demo.api_package.api.api_login import Login_api

@pytest.fixture(scope="session")
def get_token():
    res = Login_api().login()
    token = re.findall('"datas":"(.+?)",', res)
    return token[0]


