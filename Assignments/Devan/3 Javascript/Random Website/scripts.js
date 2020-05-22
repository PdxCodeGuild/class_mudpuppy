let sitesArr = ["https://www.thechive.com", "https://www.reddit.com", "https://www.attackofthecute.com", "https://www.zergnet.com", "https://www.lifehacker.com", "https://www.thisiswhyimbroke.com", "https://www.dearblankpleaseblank.com", "https://www.iwastesomuchtime.com", "https://www.fmylife.com", "https://www.oddee.com", "https://www.pinterest.com", "https://www.failblog.com", "https://www.overstock.com", "https://www.fark.com", "https://www.uncrate.com", "https://www.shitbrix.com", "https://www.2leep.com", "https://www.wonderhowto.com", "https://www.peopleofwalmart.com", "https://www.despair.com", "https://www.popcap.com", "https://www.youtube.com", "https://www.ebay.com", "https://www.facebook.com"]

function randomSite(sitesArr) {
    return sitesArr[Math.floor(Math.random() * sitesArr.length)]
}

function startTimer(duration, display) {
    var timer = duration,
        seconds;
    var timerInterval = setInterval(function () {
        seconds = parseInt(timer % 60, 10);
        seconds = seconds < 10 ? "0" + seconds : seconds;
        display.textContent = seconds;

        if (--timer < 0) {
            // timer = duration;
            clearInterval(timerInterval)
            window.location.replace(randomSite(sitesArr))
        }
    }, 1000);
}

window.onload = function () {
    var fiveSeconds = 5
    display = document.querySelector('#countdown-timer');
    startTimer(fiveSeconds, display);
};