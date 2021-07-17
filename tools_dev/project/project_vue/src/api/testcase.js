import axios from './http';

const testcase = {
    selectTestcase() {
        //第一个参数是path，后面的是其他的请求信息
        return axios('/testcase_orm', {
            "method": 'get'
        })
    }
}

export default testcase