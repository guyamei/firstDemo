'''
测试用例执行前，会自动调用conftest文件，可在里写入公共代码
'''
import pytest

from pytest_live.calculator import Calculator


@pytest.fixture(scope='class')
def calculate():
    print('开始计算')
    cal = Calculator()
    yield cal
    print('结束计算')