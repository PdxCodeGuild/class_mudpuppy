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

function findDiff(correctNum, userGuess) {
    return Math.abs(correctNum - userGuess)
}


submitButton.addEventListener("click", function () {
    if (parseInt(userGuess.value) === correctNum) {
        hintDiv.innerText = "Yay! You got it!"
    } else if (lastGuess !== null) {
        let dGuess = findDiff(correctNum, userGuess.value)
        let dLastGuess = findDiff(correctNum, lastGuess)
        if (dGuess < dLastGuess) {
            hintDiv.innerText = "Warmer"
        } else if (dGuess > dLastGuess) {
            hintDiv.innerText = "Colder"
        } else if (dGuess === dLastGuess) {
            hintDiv.innerText = "You entered the same number..."
        }
    } else if (parseInt(userGuess.value) !== correctNum) {
        hintDiv.innerText = "Wrong"
        lastGuess = parseInt(userGuess.value)
    }
    lastGuess = userGuess.value
    userGuess.value = ''
})



userGuess.addEventListener("keyup", function (event) {
    if (event.keyCode == 13) {
        submitButton.click();
    }
})



console.log(correctNum)