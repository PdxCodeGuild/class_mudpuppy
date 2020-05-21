// Javascript Redo of Python Lab 10: Average Numbers

let promptDiv = document.querySelector("#prompt");
promptDiv.innerText = "What numbers would you like to average? Type 'done' to get your result";
let numInput = document.querySelector("#num-input");
let guessButton = document.querySelector("#num-button");
let numAverage = document.querySelector("#num-average");

let numList = [];

guessButton.onclick = function() { //this function will run when someone clicks the button
    numList.push(numInput.value);
    if (numInput.value === "done") {
        let count = 0;
        let total = 0;
        numList.pop()

        for (i=0; i < numList.length; i++) {
            total += parseInt(numList[i]);
            count ++;
        }
        let numAvg = total / count;

        numAverage.innerText = (`The average of your numbers is ${numAvg}`);
        
    }
    numInput.value = ""
} 