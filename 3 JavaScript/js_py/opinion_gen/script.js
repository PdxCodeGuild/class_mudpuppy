function randRange(upper) {
	return Math.floor(Math.random() * upper)
}

function randChoice(inString) {
	return inString[randRange(inString.length)]
}
let userInput = prompt("Give me a movie: ")
let opinions = ['good', 'bad']
let output = `You chose the movie ${userInput} and that is a ${randChoice(opinions)} choice.`
alert(output)
console.log(output)
