let ballBox = document.querySelector("#ball-box");
let ctx = ballBox.getContext("2d");
let width = ballBox.width;
let height = ballBox.height;

let ball = {
    radius: 20,
    px: Math.random()*width,
    py: Math.random()*height,
    vx: (2*Math.random()-1)*10,
    vy: (2*Math.random()-1)*10,
};

function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.px, ball.py, ball.radius, 0, 2 * Math.PI, false);
    ctx.fillStyle = 'green';
    ctx.fill();
}

drawBall();

function mainLoop() {
    // update the ball's position
    ball.px = ball.px + ball.vx
    ball.py = ball.py + ball.vy
    ctx.clearRect(0,0,width,height)
    drawBall();
    // check if it hit a boundary
    if (ball.px > ballBox.width - ball.radius || ball.px < ball.radius) {
        ball.vx = ball.vx * -.9
    }
    if (ball.py > ballBox.height - ball.radius || ball.py <= ball.radius) {
        ball.vy = ball.vy * -.9
    }


    // draw the ball
    window.requestAnimationFrame(mainLoop);
}
setTimeout(mainLoop, 1000)