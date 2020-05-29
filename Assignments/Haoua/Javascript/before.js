<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://use.fontawesome.com/0208a2bb23.js"></script>
    <link href="jslab4.css" rel="stylesheet">
</head>

<body>
    <div id="container">
        <div id="head">
            <div id="date"></div>
            <div id="clear">
                <i class="fa fa-circle-thin" aria-hidden="true"></i>
            </div>
        </div>
    
        <div id="content">

            <!-- <input id="user" name="item" placeholder="(Add, Remove or Complete a task?)"> -->
            <!-- <p> To add an item to the list click Add</p> -->

            <ol id="list-title">To do list
                <li id="list-item1" class="list-items">Buy Snacks</li>
                <li id="list-item2" class="list-items">Complete Python Labs</li>
                <li id="list-item3" class="list-items">Rename Html Labs</li>
                <li id="list-item4" class="list=items">Finish Wedding Invitations</li>
            </ol>
        

            <button type="button" id="submit-button">add</button>
            <button type="button" id="dlt-button">delete</button>
            <button type="button" id="com-button">complete</button>
        </div>

        <div id="add-stuff">
            <i class="fa fa-plus-circle" aria-hidden="true"></i>

            <input id="user" name="item" placeholder="(Add, Remove or Complete a task?)">

            
            <button type="button" id="submit-button">add</button>
            <button type="button" id="dlt-button">delete</button>
            <button type="button" id="com-button">complete</button>

        </div>
    </div>

    <script>
        let empty = document.querySelector("#clear")
        let date = document.querySelector("#date")
        
        let complete = querySelector("#com-button")
        let userChoice = prompt("What would you like to do Remove or Complete?")
        arr = []
        let button = document.querySelector("#submit-button");
        
        let divContainer = document.querySelector("#container");

        let list = document.querySelector("#list-title");

        let snacks = document.querySelector("#list-item1");
        let python = document.querySelector("#list-item2");
        let html = document.querySelector("#list-item3");
        let invites = document.querySelector("#list-item4");
        //let clear = document.querySelector("#clear-button")
        let userAdd = document.querySelector("#user");
        let deleted = document.querySelector("#dlt-button")
        
        arr.push(snacks.innerText, python.innerText, html.innerText, invites.innerText)
        
        
        //let newItem = list.createElement("li")
        //list.appendChild(newItem)

        deleted.onclick = function() {
            //<!-- remove = prompt("What would you like to remove? : "); -->
            if (userAdd.value in arr) {
                let index = arr.indexOf(remove);
                arr.splice(index, index + 1);
                console.log(arr);
            }
         

        }
        button.onclick = function() {
            let newItem = document.createElement("li");
            newItem.innerText = userAdd.value;
            list.appendChild(newItem);
            alert(`You add ${userAdd.value}`);
            arr.push(newItem.innerText)
        }

        console.log(arr)

       // if (userChoice === "remove" ||"Remove") {
       //     remove = prompt("What would you like to remove? : ");
       //     if (remove in arr) {
       //         let index = arr.indexOf(remove);
       //         arr.splice(index, index + 1);
        //        console.log(arr);
       //     }
         
        //}