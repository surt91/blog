function clock() {
    var a = new Date,
        b = a.getHours(),
        c = a.getMinutes();
    a = a.getSeconds();
    b = (b < 10 ? "0" : "") + String(b);
    c = (c < 10 ? "0" : "") + String(c);
    a = (a < 10 ? "0" : "") + String(a);
    time = new Array(b.charAt(0), b.charAt(1), c.charAt(0), c.charAt(1), a.charAt(0), a.charAt(1));
    for (z = 0; z < 6; z++) for (x = i = 1; i <= 8; i *= 2, x++) {
        t = String(x) + String(z + 1);
        if (time[z] & i) switch (t.charAt(1)) {
        case "1":
            document.getElementById("z" + t).style.visibility = 'visible';
            break;
        case "2":
            document.getElementById("z" + t).style.visibility = 'visible';
            break;
        case "3":
            document.getElementById("z" + t).style.visibility = 'visible';
            break;
        case "4":
            document.getElementById("z" + t).style.visibility = 'visible';
            break;
        case "5":
            document.getElementById("z" + t).style.visibility = 'visible';
            break;
        case "6":
            document.getElementById("z" + t).style.visibility = 'visible';
            break
        } else document.getElementById("z" + t).style.visibility = 'hidden';
    }
    window.setTimeout("clock()", 1E3)
};
