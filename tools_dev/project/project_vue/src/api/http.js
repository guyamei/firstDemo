import axios from 'axios'

var instance = axios.create({
    headers:{
        'Content-Type': 'application/json'
    },
    baseURL: 'http://127.0.0.1:5000'
})

export default instance