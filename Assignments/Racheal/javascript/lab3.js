// let grade = parseInt(prompt("Please enter your grade in numerical from (0-100) : "))
alert("Find out what your grade is")
while (true) {
    let grade = parseInt(prompt("Please enter your grade in numerical from (0-100)\n Type -1 to exit : "))


    if (grade > 95) {
        alert("A+")
    }

    else if (grade === 95) {
        alert("A")
    }

    else if (grade >= 90) {
        alert("A-")
    }

    else if (grade > 85) {
        alert("B+")
    }

    else if (grade === 85) {
        alert("B")
    }

    else if (grade >= 80) {
        alert("B-")
    }

    else if (grade > 75) {
        alert("C+")
    }

    else if (grade === 75) {
        alert("C")
    }

    else if (grade >= 70) {
        alert("C-")
    }

    else if (grade > 65) {
        alert("D+")
    }

    else if (grade === 65) {
        alert("D")
    }

    else if (grade >= 60) {
        alert("D-")
    }

    else if (grade < 60 && grade > -1) {
        alert("Did you even come to class bro?")
    }

    else if (grade === -1) {
        alert("Thank you for playing!")
        break
    }
    console.log(grade)
}