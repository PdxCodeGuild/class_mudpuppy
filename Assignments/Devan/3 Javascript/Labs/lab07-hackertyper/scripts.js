let hackerText = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Similique rerum cum autem temporibus asperiores tempora praesentium corrupti nisi, dignissimos soluta omnis eligendi enim quis minima vel modi magnam assumenda eveniet?"
let hackerBox = document.querySelector("#hacker-box")
transText = ""; // This is the text that displays after typing

let index = 0 // Getting a num we can use as an index

// This will add a letter from the hacker text string after each keypress 
hackerBox.addEventListener('keydown', function (event) {
    event.preventDefault();
    hackerBox.innerText = transText
    transText += (hackerText[index])
    index++
})