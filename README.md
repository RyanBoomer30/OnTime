# CSCI S-33a Final-Project
Web Programming with Python and JavaScript

# Introduction
This website is a project managing app powered by the framework Django with Python as backend and HTML, CSS, Javascript as frontend. The user will be able to create multiple unique projects, add/edit as many tasks and todo lists as they want, and change status of a list to finished or unfinished.

# Main Page
From the main page, which can be accessed from any page using the navigation tab, the user can create a project by entering its name into the input box and click enter. Signing in is a requirement to use the app as each user will have their own unique set of projects. 

After creating a project, user will be able to see the list of all of created projects. On the left of each project name will be an entered field icon that allow the user to enter the project page, and on the right will be a trash icon that allow the user to delete the project. 

![](Images/Main%20Page.PNG)

# Project Page
In the project page, the first thing the user will see is an "Add note" input that allow the creation of a task. A task model is then created from the backend and added to the reloaded project page.

## Task functions
There are three main functions of a task form that are located on the green task toolbar:
* By clicking on the title of the task, the user can freely edit the name and the entering changes will be updated (only at the backend). 
* By clicking on the writing icon, the user can create a new list (only at the backend). 
* By clicking on the trash icon, the user can delete the task form entirely (both frontend and backend).

## List functions
There can be an infinite amount of list per task, but only 7 will be presented at a time using a paginator. On each list, the user can use these functions:
* By clicking on the circle icon, the user can check a list as done. This will also at the same time, crossout the list and change the color of the cirlce on the frontend.
* By clicking on the title of the list, the user can freely edit the name and the entering changes will be updated (only at the backend). 
* By clicking on the trash icon, the user can delete the list item entirely (both frontend and backend). 

## Timeline
The timeline is created using [vis](https://visjs.org/). Any tasks upon creation will be added to the timeline on the date it was created. A redline will also appears as an idication of the current time. If multiple tasks are created on the same day, their name will be stacked vertically on the timeline (vertical scrolling is enabled).

![](Images/Task%20Page.PNG)

# Login Page
This app is user required and therefore login or register will be needed. Just input your username and password like any normal website.

![](Images/Login%20Page.PNG)


