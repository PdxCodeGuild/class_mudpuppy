let eyes = [':', ';', '8']
let nose = ['-', '*', '+']
let mouth = [']', '},', 'D']

let randomEye = eyes[Math.floor(Math.random() * eyes.length)];
let randomNose = nose[Math.floor(Math.random() * nose.length)];
let randomMouth = mouth[Math.floor(Math.random() * mouth.length)];

console.log(`${randomEye}${randomNose}${randomMouth}`)


