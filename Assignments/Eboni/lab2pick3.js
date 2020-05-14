function randRange() {
    return Math.floor(Math.random() *11)
    
}


let outputDiv=document.querySelector("#output")
let userInput=document.querySelector("#user-input")
let guessButton = document.querySelector("#guess-bt")
let computer = randRange()


guessButton.onclick = function() {

let text
    if (userInput.value == computer)
        text='Correct!'
    else if (userInput.value >= computer)
        text='Too High!'
    else if (userInput.value <= computer)
        text='Too Low!'
        console.log(computer)

outputDiv.innerText = text

}
