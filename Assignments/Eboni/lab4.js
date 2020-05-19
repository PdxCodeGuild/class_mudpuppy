let input= document.querySelector("#input")
let button = document.querySelector("#add-to-list")
let myList = document.querySelector("#my-list")
button.onclick =function() {
    let newDiv = document.createElement("li")
        newDiv.innerText= input.value
       myList.appendChild(newDiv) 
}