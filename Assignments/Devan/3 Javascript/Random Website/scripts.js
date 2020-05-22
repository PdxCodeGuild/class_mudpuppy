function readFile(file) {
    var f = new XMLHttpRequest();
    f.open("GET", file, false);
    f.onreadystatechange = function () {
        if (f.readyState === 4) {
            if (f.status === 200 || f.status == 0) {
                var res = f.responseText;
                sitesArr = res.split('\n');
                return sitesArr
            }
        }
    }
    f.send(null);
}
readFile('./addicting-sites.txt');

function randomSite(sitesArr) {
    return sitesArr[Math.floor(Math.random() * sitesArr.length)]
}


window.location.replace(randomSite(sitesArr))