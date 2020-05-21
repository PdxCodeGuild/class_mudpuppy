//Lab 4 JavaScript

let promptDiv = document.querySelector("#item-input");
promptDiv.innerText = "Type your next to-do item and then let me know if you want to add, delete, or mark the item as completed.";
let itemInput = document.querySelector("#item-input");
let addButton = document.querySelector("#add-item");
let delButton = document.querySelector("#delete-item");
let compButton = document.querySelector("#complete-item");
let listDiv = document.querySelector("#list-div")

let toDoList = []

addButton.onclick = function() {
    toDoList.push({
        text: itemInput.value,
        completed: false
    });
    updateList();
};

delButton.onclick = function() {
    for (let i=0; i<toDoList.length; i++) {  //iterate over {object} within array and find the item's text
        if (toDoList[i]['text'] == itemInput.value) {
            toDoList.splice(i, 1);   //take item out of the array
            updateList();
        }
    } 
}

compButton.onclick = function() {
    //change array completed to true
    for (let i=0; i<toDoList.length; i++) {
        if (toDoList[i]['text'] == itemInput.value) {
            toDoList[i].completed = true
        }
        updateList();
    }
}

updateList = function() {
    //after any button is clicked, then run through list and print everything contained within array, and cross out if completed: true
    listDiv.innerHTML = ''
    
    for (let i=0; i<toDoList.length; i++) {
        if (toDoList[i]['completed'] === true) {  //display item w/ strikethrough
            listDiv.innerHTML += "<br>" + toDoList[i]['text'].strike();
            
        }

        else {listDiv.innerHTML += '<br>' + toDoList[i]['text']
        }; //display item
            }
        }