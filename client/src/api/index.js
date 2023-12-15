import axios from 'axios'
import categoriesAPI from './categories'
import authAPI from './auth';

const instance = axios.create({
    baseURL: 'http://127.0.0.1:8000/',
    timeout: 3000,
    headers: {
        'Content-Type': 'application/json',
    },
})

const APIs = {
    categories: categoriesAPI(instance),
    authAPI: authAPI(instance),
}

export default APIs
