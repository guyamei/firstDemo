# -*- coding:utf-8 -*-
import requests

from AITest.src.base import Base


class Member(Base):

    def create_member(self):

        url = f'https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}'
        data = {
            'userid': 'lisi2',
            'name': 'lisi2',
            'mobile': '15233909891',
            'department': 1
        }
        res = requests.post(url, json=data)
        return res.json()