let urlList = [
    'https://en.wikipedia.org/wiki/Psychonautics',
    'https://en.wikipedia.org/wiki/Common_mudpuppy',
    'https://en.wikipedia.org/wiki/Music_therapy',
    'https://en.wikipedia.org/wiki/Kayfabe',
    'https://en.wikipedia.org/wiki/Diana_Deutsch',
    'https://en.wikipedia.org/wiki/Chemex_Coffeemaker',
    'https://en.wikipedia.org/wiki/The_Phantom_Tollbooth',
    'https://en.wikipedia.org/wiki/Dario_Marianelli',
    'https://en.wikipedia.org/wiki/Major_Arcana',
    'https://en.wikipedia.org/wiki/Haruki_Murakami',
    'https://en.wikipedia.org/wiki/Takashi_Murakami',
    'https://en.wikipedia.org/wiki/The_Moth',
    'https://en.wikipedia.org/wiki/Portland,_Oregon',
    'https://en.wikipedia.org/wiki/Portland_Thorns_FC',
    'https://en.wikipedia.org/wiki/500_Days_of_Summer',
    'https://en.wikipedia.org/wiki/The_Egg_(2009_short_story)',
    'https://en.wikipedia.org/wiki/Music-specific_disorders#Amusia'
]

let clickMe = document.querySelector("#click-me");

function randChoice(arr) {
    return arr[Math.floor(Math.random() * (arr.length - 1))] 
    //returns random index of array  
}

function webRedirect() {
    location = randChoice(urlList)
}

clickMe.onclick = webRedirect

let timerMessage = document.querySelector("#timer-message");

let i = 10
countdown = function () {
    let timerMessageStr = `You will be redirected to your new favorite webpage in ${i} seconds`;
    timerMessage.innerHTML = timerMessageStr;
    i--
    return i
}

countdown()

setInterval(countdown, 1000);

myTimer = setTimeout(webRedirect, 10000);