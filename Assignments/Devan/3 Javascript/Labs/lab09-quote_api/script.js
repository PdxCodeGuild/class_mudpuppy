let url = 'https://favqs.com/api/';
let quoteBox = document.querySelector('.quote-box');
let quoteBoxBody = document.querySelector('#quote-body')
let quoteBoxDate = document.querySelector('#quote-date')
let quoteBoxAuthor = document.querySelector('#quote-author')


function getDailyQuote() {
    let dailyQuote = url+'qotd'
    axios.get(dailyQuote)
        .then(function (res) {
            var data = res.data
            var quote = data.quote
            var qBody = quote.body
            var qAuthor = quote.author

            quoteBoxBody.innerText = qBody
            quoteBoxAuthor.innerText = qAuthor
            quoteBoxBody.innerText = qBody
            
            console.log(data)


        })
}

getDailyQuote()