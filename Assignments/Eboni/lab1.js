
// let userInput = parseInt(prompt("Enter your score: "))
let userInput = document.querySelector("#user-input")
let outputDiv =document.querySelector("#output")
let scoreBt = document.querySelector("#score_bt")

scoreBt.onclick = function() {
    
let text
    
    if ((userInput.value <=100) && (userInput.value >=90)){
        text= `You got an A`
        
    } 
    else if ((userInput.value <=89) && (userInput.value >=80)){
        text= `You got a B`
    }
    else if ((userInput.value <=79) && (userInput.value >=70)){
        text= `You got a C you average fuck`
    }
    else if ((userInput.value <=69) && (userInput.value >=60)){
        text= `You got a D are you even trying?`
    }
    else if ((userInput.value <=59) && (userInput.value >=0)){
        text= `You fail!`
    }
    // let output = `You scored ${userInput.value}`
    // console.log(output)
    // console.log(userInput)
    // console.log(userInput.value)
    outputDiv.innerText = text
}
  




