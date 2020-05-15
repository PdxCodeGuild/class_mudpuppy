function randInt(lowerNum, upperNum) {
    return lowerNum + Math.floor(
        Math.random() * ((upperNum + 1) - lowerNum)
    )
}

let guessBetween = document.querySelector(".guess-between")
let userGuess = document.querySelector(".user-guess")
let submitButton = document.querySelector(".submit-button")
let hintDiv = document.querySelector(".hint-div")

let maxNum = 100
let minNum = 1
var guessCount = 0
let lastGuess = null
let correctNum = randInt(minNum, maxNum)
guessBetween.innerText = `Guess a number between ${minNum} and ${maxNum}: `