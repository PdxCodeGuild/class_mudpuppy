function randRange(stuff) {
    return Math.floor(Math.random() *stuff)
}

alert("Welcome to Rock, Paper, Scissors!!!")

while (true) {
    let choices = ["rock", "paper", "scissors"]
    let user = prompt (`"Choose one: ${choices}"`)
    console.log(user)

    let computer = randChoice(choices)
    console.log(computer)
}

if (user === computer) {
    alert(tie)
    console.log("you tied!")
}

if (user === "rock" ) {
    if(computer === "scissors") {
        alert("You picked rock and I picked scissors\n you win!")
    }
}

if (user === "rock") {
    if (computer === "paper") {
        alert("You picked rock and I picked papers\n I win!")
    }
}


if (user === "paper") {
    if (computer === "scissors") {
        alert("You picked paper and I picked scissors\n I win!")      
    }
}


if (user === "paper") {
    if (computer === "rock") {
        alert("You picked paper and I picked rock\n you win!")      
    }
}


if (user === "scissors") {
    if (computer === "rock") {
        alert("You picked scissors and I picked rock\n I win!")       
    }
}

if (user === "scissors") {
    if (computer === "paper") {
        alert("You picked scissors and I picked paper\n you win!")      
    }
}

if (user === "done") {
    alert("Thanks for playing!")
    break
}







