This is a simple chose your own adventure project created for a CS11 assignment

=====================
HOW TO CREATE A STORY
=====================

Stories are organized by indentation.
For example;

||Test Header <= Title when you open the game
  |First Path| <= First option on open
    |First Option| <= First Option after you click on the first path
    |Second Option| <= Second Option listed under the one above
  |Second Path| <= Second option when you open the game
    |Third Option| <= First option after you click on the second path

Lines are organized as shown below:

Indentation (just tabs. no other characters)|Title (What shows on the button)|Text (What shows in the text box after you click on the button)|Special code that runs when the button gets clicked

----
CODE
----

Code is just normal python

Any global variables you want created go in variables.txt

All code must remain on one line. To separate the code and use indentation, use \n for enter and \t for tab
For example;

  global bombsPlanted\nif(bombsPlanted>=30):\n\toption5Enabled = True\nelse:\n\toption5Enabled = False
  
The script reads this as:

  global bombsPlanted
  if(bombsPlanted>=30):
    option5Enabled = True
  else:
    option5Enabled = False

---------
FUNCTIONS
---------

Restart() ----------------------- Goes back to line 1
End(str cause) ------------------ Shows end screen. Takes string as input to display in text box (ex. "You got electrocuted and died")
nextOption() -------------------- Skips to the next option. Useful for going back or skipping around the story (ex. currentLine = 2\nnextOption())
updateButtons(int numButtons) --- Updates the buttons. Takes number of buttons to show as input

---------
VARIABLES
---------

currentLine --------------- What line is the program on (int)
option1 ------------------- Button 01 (object)
option2 ------------------- Button 02 (object)
option3 ------------------- Button 03 (object)
option4 ------------------- Button 04 (object)
option5 ------------------- Button 05 (object)
text ---------------------- Text (object)
option1Text --------------- Button 01 text (string)
option2Text --------------- Button 02 text (string)
option3Text --------------- Button 03 text (string)
option4Text --------------- Button 04 text (string)
option5Text --------------- Button 05 text (string)
window -------------------- Tkinter window (object)
option2Enabled ------------ Is option 2 enabled (bool) ---- Use if you want to disable a line that is still in your story
option3Enabled ------------ Is option 3 enabled (bool)
option4Enabled ------------ Is option 4 enabled (bool)
option5Enabled ------------ Is option 5 enabled (bool)
