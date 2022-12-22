import axios from "axios";

export const getData = (url) =>{
    new Promise((resolve, reject) => {
        resolve(axios.get(url).then((response) =>{
            response.json()
        })).then((response) =>{
            return response
        }).catch((error) => {
            reject(error)
        })
    })
}


export const saveData = (url, body) => {
    new Promise((resolve, reject) => {
        resolve(axios.post(url, body)
        .then((response) =>{
            response.json()
        })).then((response) => {
            return response
        }).catch((error) => {
            reject(error)
        })
    })
}
