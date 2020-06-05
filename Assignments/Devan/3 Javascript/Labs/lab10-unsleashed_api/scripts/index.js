var CryptoJS = require("crypto-js");

const axios = require('axios').default;
require("crypto-js/aes");
require("crypto-js/sha256");
require('dotenv').config()

let API_ID = process.env.API_ID
let API_KEY = process.env.API_KEY

/* NOTE: Definging search params, they still need to be
        added to the axios method and the urlParam */

let ORDER_STATUS = 'Parked'
let PAGE_SIZE = 2

function getSalesOrders() {
    let urlParam = `orderStatus=${ORDER_STATUS}&pageSize=${PAGE_SIZE}`;
    var hash = CryptoJS.HmacSHA256(urlParam, API_KEY);
    var hash64 = CryptoJS.enc.Base64.stringify(hash);

    axios({
        method: 'GET',
        url: 'https://api.unleashedsoftware.com/SalesOrders',
        params: {
            orderStatus: ORDER_STATUS,
            pageSize: PAGE_SIZE,
        },
        headers: {
            'Accept': 'application/json',
            'api-auth-id': API_ID,
            'api-auth-signature': hash64,
            'Content-Type': 'application/json'
        },
    }).then(function (response) {
        console.log(Object.keys(response))
        var salesOrders = response.data.Items // NOTE: An array of the orders
        var orderLines = salesOrders[0].SalesOrderLines // NOTE: The firt index of salesOrders, a array of the sales lines
        console.log(salesOrders)
        orderLines.forEach(line => {
            if (line.Product.ProductCode === 'HB-VF-01') {
                console.log(line.Product.ProductCode)
            }
        });
    }).catch(function (error) {
        console.log(error)
    })
}

getSalesOrders()