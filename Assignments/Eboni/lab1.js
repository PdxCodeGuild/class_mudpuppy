
// let userInput = parseInt(prompt("Enter your score: "))
let outputDiv =document.querySelector("#output")
let userInput = document.querySelector("#user-input")
let scoreBt = document.querySelector("#score_bt")

if ((userInput <=100) && (userInput >=90)){
    console.log(`You got an A`)
} 
else if ((userInput <=89) && (userInput >=80)){
    console.log(`You got a B`)
}
else if ((userInput <=79) && (userInput >=70)){
    console.log(`You got a C you average fuck`)
}
else if ((userInput <=69) && (userInput >=60)){
    console.log(`You got a D are you even trying?`)
}
else if ((userInput <=59) && (userInput >=0)){
    console.log(`You fail!`)
}

