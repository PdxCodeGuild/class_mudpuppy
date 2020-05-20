var userInput = document.querySelector('.user-input')
let enterBtn = document.querySelector('.enter-btn')
let removeBtn = document.querySelector('.remove-btn')
var todoList = document.querySelector('.todo-ul')
var completedList = document.querySelector('.done-ul')
let listRel = {
    'todo': 'done',
    'done': 'todo'
}

enterBtn.addEventListener("click", function () {
    var todoTask = document.createElement("li");
    todoTask.innerText = userInput.value;
    todoTask.setAttribute("onclick", "move(this);")
    todoList.appendChild(todoTask);
    userInput.value = ''

})

userInput.addEventListener('keyup', function (event) {
    if (event.keyCode == 13) {
        enterBtn.click()
    }
})

function deleteTask(taskDel) {
    var task = taskDel.parentNode;
    var list = task.parentNode;
    list.removeChild(task)
}

function move(taskItem) {
    // try
    {
        var origList = taskItem.parentNode;
        var origList_id = origList.getAttribute("id");
        var newList_id = listRel[origList_id];
        var newList = document.getElementById(newList_id);
        origList.removeChild(taskItem);
        newList.appendChild(taskItem);
    } // catch (e) {
    //     alert('move : ' + e);
    // }
}