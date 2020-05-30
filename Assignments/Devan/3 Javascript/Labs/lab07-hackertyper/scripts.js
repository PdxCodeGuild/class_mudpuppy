let hackerBox = document.querySelector("#hacker-box")

let hackerText = "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Similique rerum cum autem temporibus asperiores tempora praesentium corrupti nisi, dignissimos soluta omnis eligendi enim quis minima vel modi magnam assumenda eveniet?"

hackerBox.addEventListener('keydown', function (e) {
    e.preventDefault();
    hackerBox.innerText = hackerText
})