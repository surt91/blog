console.log("Ph'nglui mglw'nafh Cthulhu R'lyeh wgah'nagl fhtagn")
var code = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];
var pos = 0;
document.addEventListener('keydown', function(e) {
    if(e.keyCode == code[pos]) {
        pos++;
        if(pos == code.length) {
            totally_serious_function();
            pos = 0;
        }
    } else {
        pos = 0;
    }
});

function totally_serious_function() {
    console.log("activate all powerups");

    var http = new XMLHttpRequest();
    // the hardcoded key is bad, but I can change it as soon as someone finds it and uses it to send mail to me -- hopefully
    var url = "https://maker.ifttt.com/trigger/easteregg_triggered/with/key/cbkCcKHICg2b26dEi4BK03";
    var params = "value1=" + navigator.userAgent;
    http.open("POST", url, true);
    http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    http.send(params);

    var img = document.createElement("img");
    img.src = "/theme/fx/happy_cthulhu.png";
    img.className += "cthulhu";

    var credits = document.createElement("div");
    credits.className += "cthulhu-credits";
    credits.innerHTML = '<p>"Happy Cthulhu" by <a href="https://kandipatterns.com/patterns/characters/happy-cthulhu-11927">GingerCandE</a></p>'
    credits.innerHTML += '<p>"SuperBluesBros Banana Blitz" by <a href="http://freemusicarchive.org/music/RoccoW/~/SuperBluesBros_Banana_Blitz">RoccoW</a> (CC-BY)</p>'
    credits.innerHTML += '<p>"rythm.js" by <a href="https://github.com/Okazari/Rythm.js">Okazari</a></p>'

    document.body.appendChild(img);
    document.body.appendChild(credits);

    var rythm = new Rythm();

    rythm.setMusic("/theme/fx/RoccoW_SuperBluesBros_Banana_Blitz.mp3");

    rythm.addRythm('post-title', 'shake', 500, 100);
    rythm.addRythm('tag', 'twist', 500, 100);
    rythm.addRythm('post-time', 'twist', 500, 100, {direction: 'left'});
    rythm.addRythm('category', 'twist', 500, 100, {direction: 'left'});
    rythm.addRythm('icon', 'twist', 500, 100, {min: -90, max: 90});
    rythm.addRythm('post-navigation', 'jump', 500, 100);

    rythm.addRythm('cthulhu', 'jump', 500, 100, {min: -30, max: 120});

    rythm.addRythm('brand-title', 'pulse', 0, 10);
    rythm.addRythm('pure-button', 'pulse', 10, 100);
    rythm.addRythm('sidebar-social-links', 'pulse', 100, 500);
    rythm.addRythm('pure-form', 'pulse', 400, 500);

    rythm.addRythm('post-content', 'vanish', 500, 100);

    rythm.addRythm('sidebar', 'color', 0, 10, {
      from: [10,50,0],
      to:[20,95,30]
    })
    rythm.addRythm('tag', 'color', 100, 500, {
      from: [100,100,255],
      to:[200,255,255]
    })

    rythm.start();
    setTimeout(function() {window.location.reload();}, 60000);
}
