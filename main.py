from ast import Try
from asyncio.windows_events import NULL
import tkinter as tk;

storyFile = open("story.txt", "r");
story = [line.rstrip('\n') for line in storyFile.readlines()];
storyFile.close();

window = tk.Tk();
window.title("Hello World");

option1Text = "1";
option2Text = "2";
option3Text = "3";

currentLine = 0;

option1line = 0;
option2line = 0;
option3line = 0;

question ="Lorem Ipsum";

def option1Pressed():
    global currentLine, option1line;
    print("option 1 pressed");
    currentLine = option1line;
    nextOption();

def option2Pressed():
    global currentLine, option2line;
    print("option 2 pressed");
    currentLine = option2line;
    nextOption();

def option3Pressed():
    global currentLine, option3line;
    print("option 3 pressed");
    currentLine = option3line;
    nextOption();

option1 = tk.Button(text=option1Text, command=option1Pressed);
option2 = tk.Button(text=option2Text, command=option2Pressed);
option3 = tk.Button(text=option3Text, command=option3Pressed);

text = tk.Text(window, height=5, width=50);

def updateButtons(numButtons):
    global option1, option2, option3, text;
    option1.destroy();
    option2.destroy();
    option3.destroy();
    text.delete("1.0", tk.END);

    option1 = tk.Button(text=option1Text, command=option1Pressed);
    option2 = tk.Button(text=option2Text, command=option2Pressed);
    option3 = tk.Button(text=option3Text, command=option3Pressed);
    text.insert('1.0', question);

    text.pack(padx=20, pady=20);
    if (numButtons>0): option1.pack(padx=20, pady=20);
    if (numButtons>1): option2.pack(padx=20, pady=20);
    if (numButtons>2): option3.pack(padx=20, pady=20);

def nextOption():
    global currentLine, option1Text, option2Text, option3Text, option1line, option2line, option3line, question;
    numTabs = (len(story[currentLine].split(":")[0]));
    question = story[currentLine].split(":")[2];
    numOptionsUsed = 0;
    for i, line in enumerate(story[currentLine+1:]):
        if len(line.split(":")[0]) == numTabs+1:
            if numOptionsUsed < 1:
                option1Text = line.split(":")[1];
                option1line = currentLine+1+i;
            elif numOptionsUsed < 2:
                option2Text = line.split(":")[1];
                option2line = currentLine+1+i;
            elif numOptionsUsed < 3:
                option3Text = line.split(":")[1];
                option3line = currentLine+1+i;
            numOptionsUsed += 1;
            try:
                line.split(":")[3];
                print("Execute code");
            except:
                print("No code found");
        elif len(line.split(":")[0]) <= numTabs:
            break;
    updateButtons(numOptionsUsed);


#region MAIN
nextOption();
#endregion

# Start the event loop.
window.mainloop()