import pytest
import yaml

from test_appium.pages.app import App
import sys
sys.path.append('..')


def getyaml():
    with open('./member.yaml', encoding='utf-8') as f:
        cont = yaml.safe_load(f)
    return cont

class TestContact:

    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        self.app.quit()

    @pytest.mark.parametrize('username, phonenum', getyaml()['addmember'])
    def test_addcontact(self, username, phonenum):
        self.main.goto_contactlist().goto_addmemberpage().addmember_click().edit_member(username, phonenum).verify_ok()

    @pytest.mark.parametrize('username', getyaml()['delmember'])
    def test_delcontact(self, username):
        self.main.goto_contactlist().goto_personshow_page(username).goto_personaction_page().goto_editperson_page().delete_member().checkuserexist('checknotexist', username)
