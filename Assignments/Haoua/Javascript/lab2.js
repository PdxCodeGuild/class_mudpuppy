alert("Welcome to Lab2")

while (true) {
    let listOne = []
    let userInput = prompt("Please enter a social media platform, expletive, random sound, second random sound (IN THAT ORDER! Separate using spaces only) : ").toLowerCase();
    // console.log(userInput)

    // let listOne = []
    listOne.push(userInput.split(" "))
    // console.log(listOne)
    let social = listOne[0];
    let socialm = social[0];
    let expletive = social[1];
    let random = social[2];
    let randomTwo = social[3]
    console.log(social);
    console.log(social[0])
// alert(social);

    let lengthAns = social.length;
    // alert(`You submitted ${lengthAns} answers`);

    if (userInput ==='done') {
        alert("Thanks for playing!")
        break
    }
    else {
        alert(`You submitted ${lengthAns} answers`);
        alert(`All for the ${socialm}\nBitches love \' ${socialm}\nOh wait ${expletive}\n${random}\n${randomTwo}`)
    }
}