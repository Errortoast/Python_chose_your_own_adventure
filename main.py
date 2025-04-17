import tkinter as tk;
import time;

storyFile = open("story.txt", "r");
story = [line.rstrip('\n') for line in storyFile.readlines()];
storyFile.close();

# Read the variables file
with open("variables.txt", "r") as var_file:
    variables_code = var_file.read()
exec(variables_code, globals())

window = tk.Tk();
window.title("Hello World");

option1Text = "1";
option2Text = "2";
option3Text = "3";
option4Text = "4";
option5Text = "5";

currentLine = 0;
oldLine = 0;

option1line = 0;
option2line = 0;
option3line = 0;
option4line = 0;
option5line = 0;

question ="Lorem Ipsum";

option2Enabled = True;
option3Enabled = True;
option4Enabled = True;
option5Enabled = True;

storyEnded = False

def option1Pressed():
    global currentLine, option1line;
    currentLine = option1line;
    nextOption();

def option2Pressed():
    global currentLine, option2line;
    currentLine = option2line;
    nextOption();

def option3Pressed():
    global currentLine, option3line;
    currentLine = option3line;
    nextOption();

def option4Pressed():
    global currentLine, option4line;
    currentLine = option4line;
    nextOption();

def option5Pressed():
    global currentLine, option5line;
    currentLine = option5line;
    nextOption();

def restart():
    global currentLine, text, restartButton, exitButton, storyEnded;
    text.delete("1.0", tk.END);
    restartButton.destroy();
    exitButton.destroy();
    currentLine=0;
    storyEnded = False;
    nextOption();

option1 = tk.Button(text=option1Text, command=option1Pressed);
option2 = tk.Button(text=option2Text, command=option2Pressed);
option3 = tk.Button(text=option3Text, command=option3Pressed);
option4 = tk.Button(text=option4Text, command=option4Pressed);
option5 = tk.Button(text=option5Text, command=option5Pressed);

text = tk.Text(window, height=5, width=50, wrap='word');

restartButton = tk.Button(text="Restart", command=restart);
exitButton = tk.Button(text="Exit", command=quit);

def updateButtons(numButtons):
    global option1, option2, option3, option4, option5, text;
    option1.destroy();
    option2.destroy();
    option3.destroy();
    option4.destroy();
    option5.destroy();
    text.delete("1.0", tk.END);
    restartButton.destroy();
    exitButton.destroy();

    option1 = tk.Button(text=option1Text, command=option1Pressed);
    option2 = tk.Button(text=option2Text, command=option2Pressed);
    option3 = tk.Button(text=option3Text, command=option3Pressed);
    option4 = tk.Button(text=option4Text, command=option4Pressed);
    option5 = tk.Button(text=option5Text, command=option5Pressed);
    text.insert('1.0', question);

    text.pack(padx=20, pady=20);
    if (numButtons>0): option1.pack(padx=10, pady=10);
    if (numButtons>1): option2.pack(padx=10, pady=10);
    if (numButtons>2): option3.pack(padx=10, pady=10);
    if (numButtons>3): option4.pack(padx=10, pady=10);
    if (numButtons>4): option5.pack(padx=10, pady=10);

def nextOption():
    global currentLine, option1Text, option2Text, option3Text, option4Text, option5Text, option1line, option2line, option3line, option4line, option5line, question, option5Enabled, option4Enabled, option3Enabled, option2Enabled;
    option2Enabled = True;
    option3Enabled = True;
    option4Enabled = True;
    option5Enabled = True;
    try:
        code_str = story[currentLine].split("|")[3]
        code_str = bytes(code_str, "utf-8").decode("unicode_escape")
        exec(code_str, globals())
    except IndexError:
        print("Expected code segment not found in the story line.");
    except Exception as e:
        print(f"Error executing code: {e}");
    if storyEnded:
        return;
    numTabs = (len(story[currentLine].split("|")[0]));
    question = story[currentLine].split("|")[2];
    numOptionsUsed = 0;
    numOptionsFound = 0;
    for i, line in enumerate(story[currentLine+1:]):
        if len(line.split("|")[0]) == numTabs+1:
            if numOptionsFound < 1:
                option1Text = line.split("|")[1];
                option1line = currentLine+1+i;
                numOptionsUsed += 1;
            elif numOptionsFound < 2 and option2Enabled == True:
                option2Text = line.split("|")[1];
                option2line = currentLine+1+i;
                numOptionsUsed += 1;
            elif numOptionsFound < 3 and option3Enabled == True:
                option3Text = line.split("|")[1];
                option3line = currentLine+1+i;
                numOptionsUsed += 1;
            elif numOptionsFound < 4 and option4Enabled == True:
                option4Text = line.split("|")[1];
                option4line = currentLine+1+i;
                numOptionsUsed += 1;
            elif numOptionsFound < 5 and option5Enabled == True:
                option5Text = line.split("|")[1];
                option5line = currentLine+1+i;
                numOptionsUsed += 1;
            numOptionsFound +=1;
        elif len(line.split("|")[0]) <= numTabs:
            break;
    updateButtons(numOptionsUsed);

def end(cause = "You Died"):
    global option1, option2, option3, option4, option5, text, restartButton, exitButton, storyEnded;
    option1.destroy();
    option2.destroy();
    option3.destroy();
    option4.destroy();
    option5.destroy();
    text.delete("1.0", tk.END);
    restartButton.destroy();
    exitButton.destroy();

    restartButton = tk.Button(text="Restart", command=restart);
    exitButton = tk.Button(text="Exit", command=quit);
    text.insert("1.0", cause);

    text.pack(padx=20, pady=20);
    restartButton.pack(padx=10, pady=10);
    exitButton.pack(padx=10, pady=10);
    storyEnded = True

#region MAIN
nextOption();
#endregion

# Start the event loop.
window.mainloop();