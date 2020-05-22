function randNum(max) {
    return Math.floor(Math.random() * (max))
}

function randChoice(inThing) {
    return inThing[randNum(inThing.length)]
}

function makeEyes() {
    return randChoice(":;8X")
}

function makeNose() {
    return randChoice('->^•')
}

function makeMouth() {
    return randChoice("D|])(P")
}

function makeFace() {
    return makeEyes() + makeNose() + makeMouth()
}

var listOfEmoticons = []
var howMany = parseInt(prompt("How many emoticons do you want? "))

for (var i = 0; i < howMany; i++) {
    listOfEmoticons.push(makeFace())
}
console.log(listOfEmoticons)