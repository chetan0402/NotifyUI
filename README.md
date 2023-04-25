<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

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
# Default functions
---
### `sendWinStyleNotify(app_name,title,msg,fadeTime):`
- Sends a windows 10 inspired style notification.<br>
app_name: the name of the application.<br>
title: the title of the notification.<br>
msg: the message of the notification.<br>
fadeTime: the fade time of the notificaion. (Must be a `QTime` object)<br>
e.g. "Notify Elements","Hello World","This is a test message."<br>
- Note: This function is a thread. So it won't block the main thread.
# Methods of classes

## `NotifyApplication`
---
### `send_notification():`
- This sends the notification which you have created so far.

## `NotifyWindow`
---
### `setWindowTopLeft():`
- Set the window to the top left of the screen.

### `setWindowTopRight():`
- Set the window to the top right of the screen.

### `setWindowBottomLeft():`
- Set the window to the bottom left of the screen.

### `setWindowBottomRight():`
- Set the window to the BottomRight of the screen.

### `setBackgroundColor(color):`
- Set the background color of the window.<br>
color: the color in string format.<br>
e.g. `red` or `#ff0000` or `rgb(255,0,0)` or `rgba(255,0,0,0.5)`

### `appendStyle(property,value):`
- Append a style to the style sheet.<br>
property: the property of the style.<br>
e.g. `background-color` or `border-radius`
value: the value of the property.<br>
e.g. `red` or `10px` or `rgba(255,0,0,0.5)`

### `addTextElement(x,y,text,font,color):`
- x: x position of the text element inside the window<br>
y: y position of the text element inside the window<br>
text: string to be displayed<br>
font: style of the font (Must be `QFont` object)<br>
color: input hex color or rgb() for the color of text<br>
- Note: the font and color input are optional as they do have a default value

### `setCloseClick(value):`
- If true, the notification would close when left clicked.
- Default:- false

### `setPadding(value):`
- Set the padding of the window.<br>
value: the padding in pixels.<br>
e.g. 10 or 20 or 30.<br>
- Default: 10

### `setFadeAwayTime(value):`
- Set the fade away time of the window.<Br>
fadeTime: the fade away time in milliseconds.<Br>
e.g. 1000 or 2000 or 3000.<Br>
- Default:- 500

### `setFadeAtClick(value):`
- Toggle if the window should fade away when left clicked.<br>
value: True or False.
- Default: True

### `autoFade(fade_time):`
- Automatically fade away after the specified time.<br>
fade_time: the fade time. (Must be a `QTime` object)

## `NotifyText`
---
### `setBackgroundColor(color):`
- Set the background color of the window.<br>
color: the color in string format.<br>
e.g. "red" or "#ff0000" or "rgb(255,0,0)" or "rgba(255,0,0,0.5)"

### `appendStyle(property,value):`
- Append a style to the style sheet.<br>
property: the property of the style.<br>
e.g. "background-color" or "border-radius"<br>
value: the value of the property.<br>
e.g. "red" or "10px" or "rgba(255,0,0,0.5)"

### `setFadeAtClick(value):`
- Toggle if the element should fade away when left clicked.
value: True or False.
- Default: True

### `setFadeAwayTime(value):`
- Set the fade away time of the window.<br>
fadeTime: the fade away time in milliseconds.<br>
e.g. 1000 or 2000 or 3000.<br>
- Default:- 500

## `NotifyTimer`
---
### `__init__(call_at_end,end_qtime,*args,**kwargs):`
- This class runs the function passed after the specified time.<br>
call_at_end: the function to be called after the specified time.<br>
end_qtime: the time after which the function is called. (Should be a `QTime` object)<br>
args: the arguments to be passed to the function.<br>
kargs: the keyword arguments to be passed to the function.<br>

- Note:- Declare this as a variable to keep the timer alive.