# NotifyUI

A python lib to help make easy and crazy notifications.

# Example

```py
from NotifyUI import NotifyElements

app=NotifyElements.NotifyApplication()
NotifyText(app.window,10,10,"Notify Elements",font=QtGui.QFont("Segoe UI",10,QtGui.QFont.Weight.Normal))
NotifyText(app.window,10,40,"Hello world!",font=QtGui.QFont("Segoe UI",13,QtGui.QFont.Weight.Bold))
NotifyText(app.window,10,70,"Extra text",font=QtGui.QFont("Segoe UI",10,QtGui.QFont.Weight.Normal),color="#a5a5a5")
app.window.setCloseClick(True)
app.send_notification()
```

Or to simply send a windows 10 inspired notification

```py
from NotifyUI import NotifyElements

NotifyElements.sendWinStyleNotify("Notify Elements","Hello World","This is a test message.")
```

# Methods of classes

## NotifyApplication
---
### send_notification():
- This sends the notification which you have created so far.

## NotifyWindow
---
### setBackgroundColor(color):
- Set the background color of the window.<br>
color: the color in string format.<br>
e.g. "red" or "#ff0000" or "rgb(255,0,0)" or "rgba(255,0,0,0.5)"

### appendStyle(property,value):
- Append a style to the style sheet.
property: the property of the style.
e.g. "background-color" or "border-radius"
value: the value of the property.
e.g. "red" or "10px" or "rgba(255,0,0,0.5)"

### addTextElement(x,y,text,font,color):
- x: x position of the text element inside the window
y: y position of the text element inside the window
text: string to be displayed
font: style of the font (Must be QFont object)
color: input hex color or rgb() for the color of text
Note: the font and color input are optional as they do have a default value

### setCloseClick(value):
- If true, the notification would close when left clicked. Default:- false

## NotifyText
---
### setBackgroundColor(color):
- Set the background color of the window.<br>
color: the color in string format.<br>
e.g. "red" or "#ff0000" or "rgb(255,0,0)" or "rgba(255,0,0,0.5)"

### appendStyle(property,value):
- Append a style to the style sheet.
property: the property of the style.
e.g. "background-color" or "border-radius"
value: the value of the property.
e.g. "red" or "10px" or "rgba(255,0,0,0.5)"

# License

To be added...
Until then, you can use if you want but do credit.