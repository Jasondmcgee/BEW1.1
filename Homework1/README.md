##Welcome

this is my first homework assignment for BEW 1.1

there are is a lot of unnecessary code bits throughout the app.py. this is because I like to try stuff out during class. 

##Fortune teller

The fortune teller shows a basic html page that asks some random questions.

Depending on how you answer the question, the result will change. 

Here is a link to the assignment.

https://make-school-courses.github.io/BEW-1.1-RESTful-and-Resourceful-MVC-Architecture/#/Assignments/Weekly-Homework?id=homework-1

discussion questions: 
What happens when you press the “submit” button? Paste the full URL you are sent to on submit.
when you press submit you are taken to the webpage with the responses. the path is "/nextquestion"

What are the keys of this URL query string? How do they correspond to the “name” fields of your HTML form elements?
The keys for my fortune form are "icecream" and the spice girl names. I use the correspoding input to change which page i serve the user. 

What are the values of the URL query string? How do they correspond to what the user entered or typed?
The values of the keys are numeric values that I add up to determine how spice or icecreamy the user is. I also use a name field to get their name and use it when answering their fortune. 


##Fortune teller 2

Leveing up this project means adding a templates folder, calling html files from app.py using flasks render template, and having at least 4 responses to the fortune teller page. 
