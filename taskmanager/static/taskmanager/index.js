// Run when the user update a list's status (done/not done)
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.check').forEach(button =>{
        button.onclick = function() {
            CheckToggle(this.dataset.project,this.dataset.task,this.dataset.list)
        }
    })
})

// Run when the user delete a task
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.delete').forEach(button =>{
        button.onclick = function() {
            DeleteTask(this.dataset.project,this.dataset.task)
        }
    })
})

// Run when the user delete a list
document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('.delete_list').forEach(button =>{
        button.onclick = function() {
            DeleteList(this.dataset.project,this.dataset.task, this.dataset.list)
        }
    })
})

// Delete task
function DeleteTask(project, task){
    fetch(`/deleteTask/${project}/${task}`)
    .then(response => response.json())
    .then(data => {
        var removeItem = document.getElementById(`${task}`)
        removeItem.parentNode.removeChild(removeItem)
    })
}

// Delete list
function DeleteList(project, task, list){
    fetch(`/deleteList/${project}/${task}/${list}`)
    .then(response => response.json())
    .then(data => {
        var removeItem = document.getElementById(`${list}`)
        removeItem.parentNode.removeChild(removeItem)
    })
}

// Update list
function CheckToggle(project,task,list){
    console.log(project, task, list);
    fetch(`/toggleList/${project}/${task}/${list}`)
    .then(response => response.json())
    .then(data =>{
        if (data.status == true){
            // Not done: Lighten a list's circle and remove the dash across list's name
            document.querySelector(`#list_${task}_${list}`).innerHTML = `<i class="far fa-circle fa-xs" ></i>`;
            document.querySelector(`#content_${task}_${list}`).style.textDecoration = "none";
        }else{
            // Done: Darken a list's circle and put a dash across list's name
            document.querySelector(`#list_${task}_${list}`).innerHTML = `<i class="fas fa-circle fa-xs" ></i>`;
            console.log(document.querySelector(`#content_${task}_${list}`).color)
            document.querySelector(`#content_${task}_${list}`).style.textDecoration = "line-through";
        }
    })
}

// https://visjs.org/
// DOM element where the Timeline will be attached
window.onload = function() {
    var container = document.getElementById('visualization');
    var timeList = document.querySelectorAll('.infoDate'), i;
    var titleList = document.querySelectorAll('.infoName'), i;

    var timeSet = [];
    var titleSet = [];

    for(var i = 0; i < timeList.length; i++){
        timeSet.push(timeList[i].innerHTML);
    }

    for(var i = 0; i < titleList.length; i++){
        titleSet.push(titleList[i].innerHTML);
    }
    console.log(timeSet)
    console.log(titleSet)
    
    var items = new vis.DataSet();
    var itemList = [];

    for(var i = 0; i < titleList.length; i++){
        var date = new Date(timeSet[i])
        date = date.setDate(date.getDate() + 1);
        var dict = {
            id: i,
            content: titleSet[i],
            start: date
        }
        itemList.push(dict)
    }

    items.add(itemList)
    console.log(itemList)

    // Configuration for the Timeline
    var options = {
        locale: 'en',
        moment: function(date) {
            return vis.moment(date).utc();
        },
        zoomable: false,
        horizontalScroll: false,
        verticalScroll: true,
        height: `120px`,
        autoResize: true,
        timeAxis: { scale: 'day', step: 1 },
        zoomMin: 1000 * 60 * 60 * 24 * 31,    //https://stackoverflow.com/questions/44624839/restricting-x-axis-range-for-vis-timeline-chart         
        zoomMax: 1000 * 60 * 60 * 24 * 31 * 3 //https://stackoverflow.com/questions/44624839/restricting-x-axis-range-for-vis-timeline-chart
    };

    // Create a Timeline
    var timeline = new vis.Timeline(container, items, options);
}