# -*- coding:utf-8 -*-
from AITest.src.member import Member

class TestCreateMember:

    @classmethod
    def setup_class(cls):
        cls.mem = Member()

    def test_create_member(self):
        res = self.mem.create_member()
        assert res['errmsg'] == 'created'














