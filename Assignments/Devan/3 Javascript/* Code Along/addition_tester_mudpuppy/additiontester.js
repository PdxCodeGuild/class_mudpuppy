function randInt(lowerNum, upperNum) {
    return lowerNum + Math.floor(
        Math.random() * ((upperNum + 1) - lowerNum)
    )
}

let mathProblem = document.querySelector(".math-problem")
let output = document.querySelector(".output")
let userAnswer = document.querySelector(".user-answer")
let enterButton = document.querySelector(".enter-button")

let num1 = randInt(1, 5)
let num2 = randInt(1, 5)
mathProblem.innerText = `What is ${num1} + ${num2}? `


enterButton.addEventListener("click", function () {
    if (parseInt(userAnswer.value) === num1 + num2) {
        output.style.color = "green"
        output.innerText = "Correct!"
    } else {
        output.style.color = "red"
        output.innerText = "What? Try again, you fool!!"
    }
    setTimeout(() => {
        location.reload()
    }, 1000)
});

userAnswer.addEventListener("keyup", function (event) {
    if (event.keyCode == 13) {
        enterButton.click();
    }
})

// enterButton.onclick = function () {
//     if (parseInt(userAnswer.value) === num1 + num2) {
//         output.innerText = "Correct!"
//     } else {
//         output.innerText = "What? Refresh, you fool!!"
//     }
//     location.reload();
// }