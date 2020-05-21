//Javascript Test May 14th, 2020
function fandChoice(inArr) {
    return inArr[Math.floor(Math.random() * inArr.length)]
}

let userChoice = prompt('rps: ')
let compChoice = randChoice(['r', 'p', 's'])

if (userChoice == 'r' && compChoice == 'r') {
    alert("It's a tie!")
} else if (userChoice == 'r'  && compChoice == 'p') {
    alert("Computer wins!")
}

//---------------------------------

