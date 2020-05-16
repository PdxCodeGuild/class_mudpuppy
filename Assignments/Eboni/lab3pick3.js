
let choices=['r', 'p', 's']
let computerGuess = choices[Math.floor(Math.random() *3)]
let userInput =document.querySelector("#user-input")
let outputDiv =document.querySelector("#output")
let guessBt =document.querySelector("#guess-bt")


guessBt.onclick =function() {

let text
    if (userInput.value == computerGuess) {
        text=`You tie`
    }
    else if (userInput.value == 'r' && computerGuess == 'p') {
        text= `You lose`
    }
    else if (userInput.value == 'p' && computerGuess == 's') {
        text=`You lose`
    }    
    else if (userInput.value == 's' && computerGuess == 'p') {
        text= `You win`
    }
    else if (userInput.value == 'r' && computerGuess == 's') {
        text='You win'
    }
    else if (userInput.value == 'p' && computerGuess == 'r') {
        text=`You win again`
    }

    
        

    
    

    
outputDiv.innerText = text + `\nThe computer guessed: ${computerGuess}`
}

