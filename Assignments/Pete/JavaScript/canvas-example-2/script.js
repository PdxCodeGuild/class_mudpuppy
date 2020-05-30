let w = 1125
let h = 750

let skyCol = '#1E1478';
let mountCol = '#787044';
let bgCol = '#C4A909';
let moonCol = '#FFFF00';

let ctx = document.querySelector('canvas').getContext('2d');


function drawSky() {
    ctx.fillStyle = skyCol;
    ctx.fillRect(0, 0, w, h);
}

function drawStars() {
    ctx.fillStyle = 'white';
    for (let i=0; i<5000; i++) {
        ctx.beginPath();
        let x = Math.random() * w;
        let y = Math.random() * h;
        let r = Math.random() * 2
        ctx.arc(x, y, r, 0, 2*Math.PI);
        ctx.fill();
    }
}

function drawMountain(x, y) {

    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x - Math.abs(h - y), h);
    ctx.lineTo(x + Math.abs(h - y), h)
    ctx.closePath();
    ctx.fillStyle = mountCol;
    ctx.fill();
    ctx.lineWidth = 3;
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.lineTo(x - 100, y + 100);
    ctx.lineTo(x + 100, y + 100);
    ctx.closePath();
    ctx.fillStyle = 'white';
    ctx.fill();
    ctx.stroke();
}

function drawMoon(x, y) {
    ctx.beginPath();
    ctx.arc(x, y, 100, 0, 2*Math.PI);
    ctx.fillStyle = moonCol;
    ctx.fill();

    let grd = ctx.createRadialGradient(x, y, 0, x, y, 150);
    grd.addColorStop(0, 'rgba(255, 255, 255, 0.5');
    grd.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.fillStyle = grd;
    ctx.arc(x, y, 150, 0, 2*Math.PI);
    ctx.fill();
}

drawSky();
drawStars();
drawMoon(w / 4, h * .5);
drawMountain(250, 300);
drawMountain(w - 250, 300)
