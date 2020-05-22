// NOTE Getting the list of sites from a JSON file
fetch("./addicting_sites.json").then(function (res) {
    return res.json()
}).then(function (data) {
    sitesArr = data
    console.log(sitesArr)
    // FIXME sitesArr is not being returned
    return sitesArr
}).catch(function (error) {
    console.error("Couldn't retreive the data");
    console.error(error)
})


// NOTE Getting a random index of sites array
// BUG sitesArr is not defined
let randomSite = sitesArr[Math.floor(Math.random() * sitesArr.length)];


// NOTE Setting up a countdown timer that shows a button
function startTimer(duration, display) {
    var timer = duration,
        seconds;
    var timerInterval = setInterval(function () {
        seconds = parseInt(timer % 60, 10);
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = seconds;

        if (--timer < 0) {
            clearInterval(timerInterval)
            display.textContent = ''
            redirectBtn = document.createElement("button")
            redirectBtn.classList.add('btn', 'btn-danger')
            redirectBtn.setAttribute('onclick', 'window.location.replace(randomSite)')
            redirectBtn.innerText = randomSite
            display.appendChild(redirectBtn)
        }
    }, 1000);
}


// NOTE Starting the timer
window.onload = function () {
    var fiveSeconds = 5
    display = document.querySelector('#countdown-timer');
    startTimer(fiveSeconds, display);
}