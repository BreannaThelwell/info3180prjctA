//file for axios configuration. adds jwt token to requests

import axios from 'axios'

const instance = axios.create({
    baseURL: 'http://localhost:8080/api', //base api endpoint
})

//automatically include jwt in headers for requests
instance.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  })

  export default instance