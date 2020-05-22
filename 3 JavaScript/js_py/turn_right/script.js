function randRange(upper) {
	return Math.floor(Math.random() * upper)
}

function randChoice(inString) {
	return inString[randRange(inString.length)]
}
let directions = ['North', 'East', 'South', 'West']
let start = randRange(directions.length)
alert('You are facing ' + directions[start])
let user_turns = parseInt(prompt("Turn right how many times? "))
let end = start + user_turns
alert('You are facing ' + directions[end % directions.length])
