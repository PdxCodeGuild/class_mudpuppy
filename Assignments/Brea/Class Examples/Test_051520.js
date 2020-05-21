//Test Examples in Python from May 15th, 2020
//JavaScript version of Pick 6 Lab

function randInt(lowerNum, higherNum) {
    let leftOffset = lowerNum
    let middleArea = (higherNum - lowerNum) + 1 // like saying randint(2, 5)
    return leftOffset + middleArea * Math.floor(Math.random())
}

function getTicket() {
    let output = []
    for (let i=0; i<6, i++){
        output.push(randInt(1, 5))
    }
    return output
}