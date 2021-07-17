import requests
import yaml


with open('../common/config.yaml') as f:
    config = yaml.safe_load(f)


class Base:

    token = None

    def __init__(self):
        if self.token is None:
            corpid = config['work_wx']['corpid']
            secret = config['work_wx']['corpsecret']
            url = f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={secret}'
            response = requests.get(url)
            if response.json()['errmsg'] == 'ok':
                self.token = response.json()['access_token']
