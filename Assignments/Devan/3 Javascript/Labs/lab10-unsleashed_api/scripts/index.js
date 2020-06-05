var CryptoJS = require("crypto-js");

const axios = require('axios').default;
require("crypto-js/aes");
require("crypto-js/sha256");
require('dotenv').config()

let API_ID = process.env.API_ID
let API_KEY = process.env.API_KEY


function getSalesOrders() {
    let urlParam = "orderStatus=Backordered";
    var hash = CryptoJS.HmacSHA256(urlParam, API_KEY);
    var hash64 = CryptoJS.enc.Base64.stringify(hash);

    axios({
        method: 'GET',
        url: 'https://api.unleashedsoftware.com/SalesOrders',
        params: {
            orderStatus: 'Backordered'
        },
        headers: {
            'Accept': 'application/json',
            'api-auth-id': API_ID,
            'api-auth-signature': hash64,
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
        console.log(Object.keys(response))
        console.log(response.data)
    }).catch(function (error) {
        console.log(error)
    })
}

getSalesOrders()