#------------------
#CREATED BY RYLYFO
#PLEASE USE THIS AS YOU WISH, BUT CREDIT ME IN IT
#THANK YOU HAVE A GOOD REST OF YOUR DAY
#------------------


try: # attempts import
    from tkinter import *
    import time
except ImportError: # in case something goes wrong with the import
    print("import error")

root = Tk() # initilzes tkinter
root.title("weird calculator") # titles the app
root.geometry("400x400") # makes the ui size 400x400

already_open = False

def ResetUI(frame): # Function with 1 passed argument, function destroys the frame we created in the Everything function
    global already_open
    already_open = False
    frame.destroy()

def Everything(whattodo): # function with one passed argument
    global already_open
    print(already_open)
    if already_open == False:
        already_open = True
        final = 0 # integer variable 
        new_frame = Frame(root) # creates a new frame
        new_frame.pack() # packs the frame so it exists
        n1 = Text(new_frame) # creates a new frame that the user can type in
        n2 = Text(new_frame) # creates another frame that the user can type in
        n1.pack() # packs the textbox so it exists
        n2.pack() # read above ^
        n1.insert("end", "Number 1 goes here")
        n2.insert("end", "Number 2 goes here")
        complete_action = Button(new_frame, text="Complete", command=lambda: CompleteAction()) # creates a new button that triggers a function on press
        complete_action.pack() # packs the button so it exists
        closeui = Button(new_frame,text="X", command=lambda: ResetUI(new_frame))
        closeui.pack()
        answer_label = Label(new_frame, text="Answer appears here") # creates a new label with the answer
        answer_label.pack()

        def CompleteAction(): # Actual math part of the calculator, called when the "Complete" button is clicked
            number1 = n1.get(1.0, "end-1c") # get the number from the textbox
            number2 = n2.get(1.0, "end-1c") # ^
        
            #the whattodo is the passed argument that we pass through the buttons when they are clicked via functions

            if whattodo == "Add": # if the passed argument is add 
                final = int(number1) + int(number2) # add the two numbers from the textbox(s) and sets the "final" variable to the answer
            elif whattodo == "Subtract": # if the passed argument is subtract
                final = int(number1) - int(number2) # subtract the two numbers from the textbox(s) and sets the "final" variable to the answer
            elif whattodo == "Multiply": # if the passed argument is multiply
                final = int(number1) * int(number2) # multiply the two numbers from the textbox(s) and sets the "final" variable to the answer 
            elif whattodo == "Division": # if the passed argument is divide
                final = int(number1) / int(number2) # divide the two numbers from the textbox(s) and sets the "final" variable to the answer 
            else: # If the whattodo variable is something else, in which case something has gone wrong with your code (probably a grammar issue)
                print("something wrong with your code") # prints that somethins is wrong
            answer_label.config(text=str(final))
        


class UI(): # function
    def __init__(self):
        print("ran") # run check
        frame = Frame(root)
        add = Button(frame, text="Add", command=lambda: Everything("Add")) # creates add button as the children of the main frame, command (whenever the button is clicked)
        # triggers a function and passes a string which tells that function what to do
        subtract = Button(frame, text="Subtract", command=lambda: Everything("Subtract"))
        multiply = Button(frame, text="Multiply", command=lambda: Everything("Multiply"))
        divide = Button(frame, text="Divide", command=lambda: Everything("Division"))
        frame.pack() # packing the ui so it actually exists
        add.pack()
        subtract.pack()
        multiply.pack()
        divide.pack()
        print("finished") # run check 2

UI() # function

root.mainloop() # need this or code dont run lol