import tkinter as tk;

storyFile = open("story.txt", "r");
story = [line.rstrip('\n') for line in storyFile.readlines()];
storyFile.close();

window = tk.Tk();
window.title("Hello World");

option1Text = "1";
option2Text = "2";
option3Text = "3";

currentLine=1;

option1line = 0;
option2line = 0;
option3line = 0;

def option1Pressed():
    global currentLine, option1line;
    print("option 1 pressed");
    currentLine = option1line;
    print(str(currentLine) + ":" + str(option1line));
    nextOption();

def option2Pressed():
    global currentLine, option2line;
    print("option 2 pressed");
    currentLine = option2line;
    print(str(currentLine) + ":" + str(option2line));
    nextOption();

def option3Pressed():
    global currentLine, option3line;
    print("option 3 pressed");
    currentLine = option3line;
    print(str(currentLine) + ":" + str(option3line));
    nextOption();

option1 = tk.Button(text=option1Text, command=option1Pressed);
option2 = tk.Button(text=option2Text, command=option2Pressed);
option3 = tk.Button(text=option3Text, command=option3Pressed);

def updateButtons(numButtons):
    global option1, option2, option3;
    option1.destroy();
    option2.destroy();
    option3.destroy();

    option1 = tk.Button(text=option1Text, command=option1Pressed);
    option2 = tk.Button(text=option2Text, command=option2Pressed);
    option3 = tk.Button(text=option3Text, command=option3Pressed);

    option1.pack(padx=20, pady=20);
    if (numButtons>1): option2.pack(padx=20, pady=20);
    if (numButtons>2): option3.pack(padx=20, pady=20);

def nextOption():
    global currentLine, option1Text, option2Text, option3Text, option1line, option2line, option3line;
    numTabs = (len(story[currentLine].split(":")[0]) / 2);
    question = story[currentLine-1].split(":")[2];
    numOptionsUsed = 0;
    for i, line in enumerate(story[currentLine:], start=currentLine):
        if len(line.split(":")[0]) / 2 == numTabs:
            if numOptionsUsed < 1:
                option1Text = line.split(":")[1];
                option1line = i;
            elif numOptionsUsed < 2:
                option2Text = line.split(":")[1];
                option2line = i;
            elif numOptionsUsed < 3:
                option3Text = line.split(":")[1];
                option3line = i;
            numOptionsUsed += 1;
        elif len(line.split(":")[0]) / 2 < numTabs:
            break;
    updateButtons(numOptionsUsed);


#region MAIN
nextOption();
#endregion

# Start the event loop.
window.mainloop()