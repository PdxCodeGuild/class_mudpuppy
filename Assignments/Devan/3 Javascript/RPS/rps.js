function randNum(max) {
    return Math.floor(Math.random() * (max))
}

function randChoice(inThing) {
    return inThing[randNum(inThing.length)]
}

let choices = ["rock", "paper", "scissors"]
let computer = randChoice(choices)
let player = randChoice(choices)

console.log("computer: " + computer)
console.log("player: " + player)

if (player == computer)
    console.log("It's a tie.");
else if ((player == "rock") && (computer == "scissors"))
    console.log("You Win!");
else if ((player == "scissors") && (computer == "paper"))
    console.log("You Win!");
else if ((player == "paper") && (computer == "rock"))
    console.log("You Win!");
else
    console.log("You Loose!")