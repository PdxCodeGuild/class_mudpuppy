// JavaScript Lab 1A: Python Lab 2 (Mad Libs)

let userColor = prompt("Give me a color : ");
let userFood = prompt("Give me a plural food : ");
let userRhyme = prompt("Give a word that rhymes with ham : ");

let output = `Here's your MadLib: \n
Do you like ${userColor} ${userFood} and ham? \n
I do not like them Sam-I-${userRhyme} \n`;
alert(output);

var keepGoing = 'y'
let output2

if (keepGoing === 'y') keepGoing = prompt("Would you like to build the next part of the story? (y/n): ")
    if (keepGoing === 'y') { // 2nd part of story
        let userPlace = prompt("Give me a place : ")
        let userRhyme2 = prompt("Give me a noun that rhymes with your place : ")

        output2 = `Would you like them in a ${userPlace}? \n
        Would you like them with a ${userRhyme2}? \n
        Not in a ${userPlace}, not with a ${userRhyme2}
        I do not like them Sam-I-${userRhyme} \n`
        
        alert(output + output2);
        } else if (keepGoing == 'n') {
            alert("Thanks for playing Mad Libs!");
        }
    

if (keepGoing === 'y') keepGoing = prompt("Would you like to build the next part of the story? (y/n): ")
    if (keepGoing === 'y') { // 3rd part of story
        let userPlace = prompt("Give me a type of car : ")
        let userRhyme2 = prompt("Give me a something that rhymes with your car : ")

        let output3 = `Would you like them in a ${userPlace}? \n
        Would you like them with a ${userRhyme2}? \n
        Not in a ${userPlace}, not with a ${userRhyme2}
        I do not like them Sam-I-${userRhyme}`
        
        alert(output + output2 + output3);
        } else if (keepGoing == 'n') {
            alert("Thanks for playing Mad Libs!");
        }
        