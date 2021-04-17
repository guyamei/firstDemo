import pytest
from test_selenium.page.main_page import MainPage


class TestAddMember:

    def setup(self):
        self.main = MainPage()

    @pytest.mark.skip()
    @pytest.mark.parametrize('username,aid,phone', [('测试1', '123', '13390982871')])
    def test_add_member(self, username,aid,phone):
        """
        用来测试添加成员功能
        :return:
        """
        #   1.跳转到添加成员页 2.添加成员 3.获取成员列表，做断言验证
        list = self.main.goto_add_member().add_member(username, aid, phone).get_list()
        assert username in list


    @pytest.mark.parametrize('name', ['财务二部'])
    def test_add_department(self, name):

        self.main.goto_contact().add_department(name)





