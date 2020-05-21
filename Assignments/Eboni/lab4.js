let input= document.querySelector("#input")
let button = document.querySelector("#add-to-list")
let myList = document.querySelector("#my-list")
// let removeButton = document.querySelector("#remove-button")
// let completedList = document.querySelector("#completed-list")
button.onclick =function() {
    let newli = document.createElement("li")
    let newSpan = document.createElement("span")
    let newButton = document.createElement("button")
    newli.appendChild(newSpan)
    newli.appendChild(newButton)
    myList.appendChild(newli)
         newSpan.innerText= input.value
         newButton.innerText = "Remove"
    //     myList.appendChild(newDiv)
            newButton.onclick =function() {
                this.parentNode.parentNode.removeChild(this.parentNode)
                
            }

    // let newDiv = document.createElement
    // ("div")
    
    // newButton.innerText = "Remove"
    // newSpan.innerText = input.value

    
    // newButton.onclick = function() {
    //     numSpan = this.parentNode.firstChild
    //     numSpan.innerText = parseInt(numSpan.innerText)
    // }
}

