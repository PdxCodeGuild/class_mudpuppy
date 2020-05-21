let input= document.querySelector("#input")
let button = document.querySelector("#add-to-list")
let myList = document.querySelector("#my-list")

// let removeButton = document.querySelector("#remove-button")
// let completedList = document.querySelector("#completed-list")
button.onclick =function() {
    let newli = document.createElement("li")
    let newSpan = document.createElement("span")
    let newButton = document.createElement("button")
    let completeButton = document.createElement("button")
    newli.appendChild(newSpan)
    newli.appendChild(newButton)
    myList.appendChild(newli)
    newli.appendChild(completeButton)
         newSpan.innerText= input.value
         newButton.innerText = "Remove"
         completeButton.innerText="Complete"
         completeButton.onclick =function() {
            console.log(this)
            console.log(this.parentNode)

             this.parentNode.style.textDecoration="line-through";
         }
   
            newButton.onclick =function() {
                this.parentNode.parentNode.removeChild(this.parentNode)
    
                
                
            }

    
}

