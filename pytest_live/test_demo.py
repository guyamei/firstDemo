import allure
import pytest
import yaml

def get_datas():
    with open('data.yaml') as f:
        datas = yaml.safe_load(f)
    return datas


@allure.feature('测试计算器')
class TestCal:

    @allure.story('测试相加功能_int')
    @pytest.mark.parametrize('a,b,expect', get_datas()['add_int']['datas'])
    def test_add_int(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)

    '''
    ids:给测试用例重命名
    '''

    @allure.story('测试相加功能_float')
    @pytest.mark.parametrize('a,b,expect',
                             get_datas()['add_float']['datas'],
                             ids=get_datas()['add_float']['ids'])
    def test_add_float(self, calculate, a, b, expect):
        assert expect == round(calculate.add(a, b), 2)

    @allure.story('测试相加功能_navigate')
    @pytest.mark.parametrize('a, b, expect', get_datas()['add_navigate']['datas'], ids=get_datas()['add_navigate']['ids'])
    def test_add_navigate(self, calculate, a, b, expect):
        assert expect == calculate.add(a, b)


    @allure.story('测试相除功能_notzero')
    @pytest.mark.parametrize('a,b,expect', get_datas()['div_notzero']['datas'])
    def test_div_notzero(self, calculate, a, b, expect):
        try:
            assert expect == calculate.div(a, b)
        except ZeroDivisionError:
            print('除数为0')

    @allure.story('测试相除功能_endless')
    @pytest.mark.parametrize('a,b,expect', get_datas()['div_endless']['datas'])
    def test_div_endless(self, calculate, a, b, expect):
        try:
            assert expect == round(calculate.div(a, b), 2)
        except ZeroDivisionError:
            print('除数为0')


    @allure.story('测试相除功能_zero')
    @pytest.mark.parametrize('a,b,expect', get_datas()['div_zero']['datas'])
    def test_div_zero(self, calculate, a, b, expect):
        try:
            assert expect == calculate.div(a, b)
        except ZeroDivisionError:
            print('除数为0')

        '''
        只会在0为除数的时候，测试用例会通过，如果除数不为0，测试用例反而会failed
        with pytest.raises(ZeroDivisionError):
            cal.div(1,0)
        '''

    @allure.story('测试相减功能_int')
    @pytest.mark.parametrize('a,b,expect', get_datas()['minus_int']['datas'])
    def test_minus_int(self, calculate, a, b, expect):
        assert expect == calculate.minus(a, b)

    @allure.story('测试相减功能_float')
    @pytest.mark.parametrize('a,b,expect', get_datas()['minus_float']['datas'])
    def test_minus_float(self, calculate, a, b, expect):
        assert expect == round(calculate.minus(a, b), 2)

    @allure.story('测试相乘功能_int')
    @pytest.mark.parametrize('a,b,expect', get_datas()['multi_int']['datas'])
    def test_multi_int(self, calculate, a, b, expect):
        assert expect == calculate.multi(a, b)

    @allure.story('测试相乘功能_float')
    @pytest.mark.parametrize('a,b,expect', get_datas()['multi_float']['datas'])
    def test_multi_float(self, calculate, a, b, expect):
        assert expect == calculate.multi(a, b)

    @allure.story('测试相乘功能_navigate')
    @pytest.mark.parametrize('a,b,expect', get_datas()['multi_navigate']['datas'])
    def test_multi_navigate(self, calculate, a, b, expect):
        assert expect == calculate.multi(a, b)

    @allure.story('测试相乘功能_zero')
    @pytest.mark.parametrize('a,b,expect', get_datas()['multi_zero']['datas'])
    def test_multi_zero(self, calculate, a, b, expect):
        assert expect == calculate.multi(a, b)

