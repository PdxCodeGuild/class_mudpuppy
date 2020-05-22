function readFile(file) {
    var f = new XMLHttpRequest();
    f.open("GET", file, false);
    f.onreadystatechange = function () {
        if (f.readyState === 4) {
            if (f.status === 200 || f.status == 0) {
                var res = f.responseText;
                sitesArr = res.split('\n');
                return sitesArr
            }
        }
    }
    f.send(null);
}
readFile('./addicting-sites.txt');

function randomSite(sitesArr) {
    return sitesArr[Math.floor(Math.random() * sitesArr.length)]
}

function startTimer(duration, display) {
    var timer = duration,
        minutes, seconds;
    setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = seconds;

        if (--timer < 0) {
            window.location.replace(randomSite(sitesArr))
            // timer = duration;
        }
    }, 1000);
}

window.onload = function () {
    var fiveSeconds = 5
    display = document.querySelector('#countdown-timer');
    startTimer(fiveSeconds, display);
};