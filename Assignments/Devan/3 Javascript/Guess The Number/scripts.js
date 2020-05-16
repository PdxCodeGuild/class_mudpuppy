let guessBetween = document.querySelector(".guess-between")
let userGuess = document.querySelector(".user-guess")
let submitButton = document.querySelector(".submit-button")
let hintDiv = document.querySelector(".hint-div")

let maxNum = 10
let minNum = 1
var guessCount = 0
let lastGuess = null
let correctNum = randInt(minNum, maxNum)
guessBetween.innerText = `Guess a number between ${minNum} and ${maxNum}: `

function randInt(lowerNum, upperNum) {
    return lowerNum + Math.floor(
        Math.random() * ((upperNum + 1) - lowerNum)
    )
}


console.log(correctNum)