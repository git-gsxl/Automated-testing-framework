from pytest_demo.api_package.common.base import Base_api
from pytest_demo.api_package.common.config import host
import re

cookies = {'Cookie': 'jenkins-timestamper-offset=-28800000; sessionid=dvx7vgzne4norh1j4qx78z3a2blu7em1'}

class Home_api(Base_api):

    def add_project(self, name='hrun1', _name='广深小龙', token=''):
        url = host()+'/pages/add_project/'
        body = {"project_name": name,
                "responsible_name": _name,
                "test_user": "K、J、L",
                "dev_user": "D",
                "publish_app": "hrun_web",
                "simple_desc": "hrun_web",
                "other_desc": "hrun_web"}

        res = self.post(url, body, token=token, cookies=cookies)
        return res

    def select_list(self):
        url = host()+'/pages/project_list/1/'
        res = self.get(url, cookies=cookies)
        try:
            r = re.findall("invalid\('(.+?)'\)", res)
            id = int(r[0])
        except: id=''
        return id


    def del_project(self,id, token=''):
        url = host()+'/pages/project_list/1/'
        body = {"id": id, "mode": "del"}
        res = self.post(url, body, token=token, cookies=cookies)
        return res

