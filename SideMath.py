# ----------------------------------------
# SideMath
# Insanely simple little window
#   to do quick math
# jowja.com
# Version 0.1
# ----------------------------------------

from Tkinter import *
from datetime import datetime, date, time
import time, math, sys

global ans
ans = 0

# ----------------------------------------
# output text to main text field
def textTo_Window(printMe):

   window_set(1)

   viewMessage.tag_config('textWhite', foreground="White", font=("Arial",12,"bold"))
   viewMessage.tag_config('LighterGray', background="Black")

   temp = StringVar()
   temp = viewMessage.get(1.0, END)

   viewMessage.delete(1.0,END)

   viewMessage.insert('1.0', printMe)

   viewMessage.insert(END, "\n")

   tempEnd = str(viewMessage.index('end-1c'))

   viewMessage.insert(END, temp)
   viewMessage.tag_add('LighterGray', '1.0', '2.0')
   viewMessage.tag_add('textWhite', '1.0', '2.0')

   window_set(0)

# ----------------------------------------
# change window setting
def window_set(toggle) :

   if (toggle == 0) :
      viewMessage['state'] = 'disable'
   else :
      viewMessage['state'] = 'normal'

# ----------------------------------------
# Process the input for python
def processText(event) :

    pText = StringVar()
    tValue = StringVar()
    tValue = textVar.get()
    pText = tValue.lower().strip()
    global ans

    if(pText == "help"):
        helpCommands()
        clear()
        return

    elif(pText == "date"):
        textTo_Window(datetime.now().strftime('>> Date: %m / %d / %Y'))
        clear()
        return

    elif(pText== "time"):
        textTo_Window(datetime.now().strftime('>> Time: %H : %M'))
        clear()
        return

    if("math" in pText):
        textTo_Window(">> Input error.")
        return

    if("cos" in pText):
        pText = pText.replace("cos", "math.cos")
        clear()

    if("sin" in pText):
        pText = pText.replace("sin", "math.sin")
        clear()

    if("tan" in pText):
        pText = pText.replace("tan", "math.tan")
        clear()

    if("exp" in pText):
        pText = pText.replace("exp", "math.exp")
        clear()

    if("log" in pText):
        pText = pText.replace("log", "math.log")
        clear()

    if("log10" in pText):
        pText = pText.replace("log", "math.log10")
        clear()

    if("sqrt" in pText):
        pText = pText.replace("sqrt", "math.sqrt")
        clear()

    if("ee" in pText):
        pText = pText.replace("ee", "math.e")
        clear()

    if("acos" in pText):
        pText = pText.replace("acos", "math.acos")
        clear()

    if("asin" in pText):
        pText = pText.replace("asin", "math.asin")
        clear()

    if("atan" in pText):
        pText = pText.replace("atan", "math.atan")
        clear()

    if("deg" in pText):
        pText = pText.replace("deg", "math.degrees")
        clear()

    if("rad" in pText):
        pText = pText.replace("rad", "math.radians")
        clear()

    if("pi" in pText):
        pText = pText.replace("pi", "math.pi")
        clear()

    if("ans" in pText):
        pText = pText.replace("ans", str(ans))
        tValue = tValue.replace("ans", "{" + str(ans) + "}")
        clear()

    tryCatchEval(tValue,pText)

# ----------------------------------------
# The help menu
def helpCommands() :
    s = ">> Commands:\n"
    s += "  Date, Time\n"
    s += "  cos(x), sin(x), tan(x)\n"
    s += "  acos(x), asin(x), atan(x)\n"
    s += "  sqrt(x), exp(x), log(x), log10(x)\n"
    s += "  deg(x), rad(x), pi, ee\n"
    s += "  Use \'ans\' for the previous answer.\n"
    s += "  All trig commands use radians."
    textTo_Window(s)

# ----------------------------------------
# Try the math
def tryCatchEval(tValue,pText) :
    global ans
    ansTemp = ans
    try:
        ans = eval(pText)
        textTo_Window(tValue + " = " + str(ans))
        clear()
    except:
        textTo_Window(">> Input error.")
        ans = ansTemp

# ----------------------------------------
# clear
def clear() :
    textVar.set("")

# ----------------------------------------
# Window formatting
root = Tk()
root.geometry('300x300+100+100')
root.title('SideMath v0.1')
root.resizable(width=TRUE, height=TRUE)
root.minsize(200,200)
root.configure(background = 'gray50')
root.wm_iconbitmap('icon.ico')

# ----------------------------------------
# GUI Objects

# message entry
textVar = StringVar()
enterMessage = Entry(root, textvariable=textVar, font=("Arial",14), relief=GROOVE, bg="RosyBrown", fg="CornSilk")
enterMessage.bind('<Return>', processText)
textVar.set("")
enterMessage.pack(side=TOP, fill=X)

# message viewer
viewMessage = Text(root, font=("Arial",12), relief=GROOVE, bg="Gray25", fg="White")
window_set(0)
viewMessage.pack(side=TOP, fill=BOTH, expand=TRUE)

# ----------------------------------------
# Starting text
textTo_Window("")

# ----------------------------------------
# go!
root.mainloop()

# ----------------------------------------
# END
# ----------------------------------------
