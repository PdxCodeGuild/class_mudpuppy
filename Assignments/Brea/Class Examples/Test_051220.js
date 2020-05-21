function randInt(upper) {
    return Math.floor(Math.random() * upper)
}

function randChoice(inString) {
    return inString[randInt(inString.length)]
}

document.body.style.backgroundColor = "steelblue"   //changes background color of webpage via JavaScript

let ouputDiv = document.querySelector("#output")    // getting the div that will show the output
let movieInput = document.querySelector("#movie-input")     //getting the input
let movieButton = document.querySelector("#movie-button") //getting the button
    
// outputDiv.innerText = movieInput.Value

movieButton.onclick = function() {  //run when the button is clicked
    console.log(movieInput.value)   // print the value of the movie input value
    outputDiv.innerText = movieInput.value
}

let userInput = prompt("Give me a movie : ")
let opinions = ['good', 'bad']
let output = `You chose the movie ${userInput} and that is a {randChoice(opinions)} choice.`
    outputDiv.innerText = output
alert(output)
console.log(output)


// let vowels = 'aeiouy'
// for (let i=0; i<100; i++) // i+=1} //
//     console.log(randChoice(vowels))

// --------

let directions = ['North', 'East', 'South', 'West']
let start = randInt(directions.length)
let userTurns = parseInt(prompt("How many right turns? : "))
let end = start + turns
alert(`You are now facing` + directions[end % directions.length])