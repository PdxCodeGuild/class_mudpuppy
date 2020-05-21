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
    var taskDiv = document.createElement('div')
    var deleteBtn = document.createElement('button')
    var todoTask = document.createElement('li')

    deleteBtn.classList.add('remove-btn', 'close')
    deleteBtn.innerHTML = '&times;'
    deleteBtn.setAttribute("onclick", "deleteTask(this);")

    todoTask.innerText = userInput.value;
    todoTask.setAttribute("onclick", "move(this);")

    taskDiv.appendChild(deleteBtn);
    taskDiv.appendChild(todoTask);
    todoList.appendChild(taskDiv)

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
    try {
        var taskDiv = taskItem.parentNode;
        var origList = taskDiv.parentNode;
        var origList_id = origList.getAttribute("id");
        var newList_id = listRel[origList_id];
        var newList = document.getElementById(newList_id);
        origList.removeChild(taskDiv);
        newList.appendChild(taskDiv);
    } catch (e) {
        alert('move : ' + e);
    }
}

function clearDone() {
    completedList.forEach(function (task) {
        completedList.removeChild(task)
    })
}