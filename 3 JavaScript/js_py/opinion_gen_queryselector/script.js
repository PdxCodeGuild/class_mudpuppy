function randRange(upper) {
	return Math.floor(Math.random() * upper)
}

function randChoice(inString) {
	return inString[randRange(inString.length)]
}
document.body.style.backgroundColor = "steelblue"
let outputDiv = document.querySelector("#output") // getting the div where we show output
let movieInput = document.querySelector("#movie-input") // getting the input
let movieButton = document.querySelector("#movie-button") // getting the button
let opinions = ['good', 'bad']
movieButton.onclick = function() { // run when the button is clicked
	let output = `You chose the movie ${movieInput.value} and that is a ${randChoice(opinions)} choice.`
	outputDiv.innerText = output
}
