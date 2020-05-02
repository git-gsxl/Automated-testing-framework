# coding:utf-8
import os, sys, time
sys.path.append(os.path.dirname(os.getcwd()))                # 添加至环境变量
from pytest_demo.api_package.api.api_home import Home_api

class Test_home():

    def test_add(self):
        res = Home_api().add_project(name=time.time())
        assert '/pages/project_list/1/' == res

    def test_add1(self):
        res = Home_api().add_project(name='HttpRunnerManager', _name='自动化接口测试哈哈哈哈哈哈')
        assert '该项目已存在，请重新编辑' == res

    def test_del(self):
        id = Home_api().select_list()
        res = Home_api().del_project(id)
        assert 'ok' == res
