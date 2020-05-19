
# New Canvas Lab: Draw a Picture

## Canvas in HTML

In this lab, you'll be using HTML5 `canvas` to draw images onto the screen.  Here's what a `canvas element` looks like in the html:

```html
<canvas width="750" height="750"></canvas>
```

With `canvas` you give the element `width` and `height` attributes in the html, instead of the `css`.  By default, a `canvas` element has a `width` of 300 pixels and a `height` of 150 pixels.

## Canvas in JavaScript

First you need to get the JavaScript to recognize the `canvas` element, like you would other HTML elements, using ```document.querySelector```.
```javascript
let cnv = document.querySelector('canvas');
```
But you also need to define a new variable, the `context` with which you'll be drawing on the canvas.
```javascript
let ctx = cnv.getContext('2d');
```
It's a good idea to store your canvas height and width as variables.
```javascript
let w = 750;
let h = 750;
```

## Drawing a Rectangle

Let's draw a rectangle using the the `rect` method.
```javascript
// ctx.rect takes in the starting coordinates and dimensions of a rectangle
ctx.rect(250, 200, 250, 350); // ctx.rect(x, y, width, height)

// but nothing is drawn until you use another method like fill
ctx.fillStyle = 'green' // fillstyle is an attribute of ctx; it can be a color, gradient, or pattern and is 'black' by default
ctx.fill(); // fill() is a method; this line of code draws the green rectangle

// or stroke
ctx.lineWidth = 2; // lineWidth is also an attribute of ctx; it takes a number and is 1 by default
ctx.stroke(); // stroke() is a method; this line of code draws the black outline of the green rectangle
```

![](canvas-rect.png)