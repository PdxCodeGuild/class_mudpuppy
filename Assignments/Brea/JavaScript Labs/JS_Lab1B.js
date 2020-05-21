//Javascript Lab 1B: Python Lab 12 (Guess the Number)

compNum = Math.floor(Math.random() * 11)

let promptDiv = document.querySelector("#prompt")
promptDiv.innerText = "Guess what number I'm thinking of between 0 and 10..."
let userGuess = document.querySelector("#user-guess")
let guessButton = document.querySelector("#guess-button")
let numFeedback = document.querySelector("#num-feedback")


var i=0;
    guessButton.onclick = function() { //this function will run when someone clicks the button
        i++
        iCount = i
        if (i == 9) {
            finalOutput = `No more guesses, my number was ${compNum}!`
            alert(finalOutput);
        } else if (i < 10 && compNum == parseInt(userGuess.value)) {
            numFeedback.innerText = ("You guessed my number!");
        } else if (i < 10 && compNum != parseInt(userGuess.value)) {
            numFeedback.innerText = (`Try again! You have ${(10 - iCount)} guess(es) left`)
            // promptDiv = prompt("Guess what number I'm thinking of between 0 and 10: ");
        
    }
} 
