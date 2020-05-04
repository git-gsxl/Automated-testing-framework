# coding:utf-8
import os, sys, time
sys.path.append(os.path.dirname(os.getcwd()))                # 添加至环境变量
from pytest_demo.api_package.api.api_home import Home_api

class Test_home():

    def test_add(self, get_cookie):
        res = Home_api().add_project(name=time.time(), cookies=get_cookie)
        assert '/api/project_list/1/' in res.text

    def test_add1(self, get_cookie):
        res = Home_api().add_project(name='HttpRunnerManager', _name='自动化接口测试哈哈哈哈哈哈', cookies=get_cookie)
        assert '该项目已存在，请重新编辑' == res.text

    def test_del(self, get_cookie):
        id = Home_api().select_list(cookies=get_cookie)
        res = Home_api().del_project(id)
        assert 'ok' == res.text
