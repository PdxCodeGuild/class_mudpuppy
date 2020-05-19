var userInput = document.querySelector('.user-input')
let enterBtn = document.querySelector('.enter-btn')
let removeBtn = document.querySelector('.remove-btn')
var todoList = document.querySelector('.todo-ul')
var completedList = document.querySelector('.done-ul')



enterBtn.addEventListener("click", function () {
    var todoTask = document.createElement("li");
    todoTask.innerText = userInput.value;
    todoTask.setAttribute("onclick", "move(this);")
    todoList.appendChild(todoTask);
    userInput.value = ''

})

removeBtn.addEventListener('click', function () {
    var doneTTasks = completedList
    for (var i = 0; i < doneTTasks.length; ++i) {
        pass
    }
})


var h_list_rel = {
    'todo': 'done',
    'done': 'todo'
};

function move(ot) {
    try {
        var oc = ot.parentNode;
        var oc_id = oc.getAttribute("id");
        var on_id = h_list_rel[oc_id];
        var on = document.getElementById(on_id);
        oc.removeChild(ot);
        on.appendChild(ot);
    } catch (e) {
        alert('move : ' + e);
    }
}