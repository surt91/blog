$(document).ready(function(){function h(a,b){for(i=1;i<=3;i++){var c=new RegExp("z"+i+"\\d\\w*z"+i+"\\d");if(c.test(a))for(n=1;n<=3;n++){c=new RegExp("z"+i+n);if(!c.test(a))if(!c.test(b)){c="z"+i+n;return c.slice(1,3)}}}for(i=1;i<=3;i++){c=new RegExp("z\\d"+i+"\\w*z\\d"+i);if(c.test(a))for(n=1;n<=3;n++){c=new RegExp("z"+n+i);if(!c.test(a))if(!c.test(b)){c="z"+n+i;return c.slice(1,3)}}}if(u(a)==2){if(!a.match(/13/))if(!b.match(/z13/))return 13;if(!a.match(/22/))if(!b.match(/z22/))return 22;if(!a.match(/31/))if(!b.match(/z31/))return 31}if(v(a)==
2){if(!a.match(/11/))if(!b.match(/z11/))return 11;if(!a.match(/22/))if(!b.match(/z22/))return 22;if(!a.match(/33/))if(!b.match(/z33/))return 33}return 0}function w(a,b){if(b)if(h(b,a))return h(b,a);if(b)if(h(a,b))return h(a,b);do{var c=s(1,3),x=s(1,3);c="z"+c+x}while(!y(c,a,b));return c.slice(1,3)}function y(a,b,c){a=new RegExp(a);if(!a.test(b))if(!a.test(c))return 1;return 0}function u(a){var b=0;a.match(/13/)&&b++;a.match(/22/)&&b++;a.match(/31/)&&b++;return b}function v(a){var b=0;a.match(/11/)&&
b++;a.match(/22/)&&b++;a.match(/33/)&&b++;return b}function s(a,b){if(a>b)return-1;if(a==b)return a;return a+parseInt(Math.random()*(b-a+1))}function o(a){return a?a.match(/z1\d(\w)*z1\d(\w)*z1\d/)?1:a.match(/z2\d(\w)*z2\d(\w)*z2\d/)?1:a.match(/z3\d(\w)*z3\d(\w)*z3\d/)?1:a.match(/z\d1(\w)*z\d1(\w)*z\d1/)?1:a.match(/z\d2(\w)*z\d2(\w)*z\d2/)?1:a.match(/z\d3(\w)*z\d3(\w)*z\d3/)?1:a.match(/13/)&&a.match(/22/)&&a.match(/31/)?1:a.match(/11/)&&a.match(/22/)&&a.match(/33/)?1:0:0}function t(){if(d==1){$("#status").text("x ist am Zug");
$("#debug").text("klicke hier zum Start")}else d==0&&$("#status").text("o ist am Zug");$(".feld").bind("click",function(){$("#debug").text(" ");if(d==0){$(this).text("o");$(this).unbind("click");e++;j.push($(this).attr("id").slice(1,3));d=1;f="z"+j.join("z")+"z";$("#status").text("x ist am Zug")}if(e<9&&!o(f))if(d==1){k=w(f,l);m.push(k);$("#z"+k).text("x");d=0;e++;$("#z"+k).unbind("click");l="z"+m.join("z")+"z";$("#status").text("o ist am Zug")}if(o(f)){$("#status").text("o Gewinnt");d=1;p++;g=1;
$(".feld").unbind("click")}else if(o(l)){$("#status").text("x Gewinnt");d=0;q++;g=1;$(".feld").unbind("click")}else if(e<9)if(d==1)$("#status").text("x ist am Zug");else d==0&&$("#status").text("o ist am Zug");else{$("#status").text("Unentschieden");r++;g=1;$(".feld").unbind("click")}$("#xWins").text("x: "+q);$("#oWins").text("o: "+p);$("#remis").text("-: "+r)})}var d=0,e=0,m=new Array(9),j=new Array(9),g=0,q=0,p=0,r=0,k=0,f=0,l=0;$("#xWins").text("x: "+q);$("#oWins").text("o: "+p);$("#remis").text("-: "+
r);t();$(".result").bind("click",function(){if(g==1){e=0;$(".feld").text(" ");for(var a=0;a<j.length;++a)j[a]=0;for(a=0;a<m.length;++a)m[a]=0;g=l=f=0;t()}})});