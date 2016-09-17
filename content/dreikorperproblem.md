Title: Dreikörperproblem
Date: 2012-06-03 16:21
Author: surt91
Category: Code
Tags: Physik, Video, Chaos
Slug: dreikorperproblem
Status: published

Nein, ich habe keine analytische Lösung dafür gefunden. (Soweit ich mich
erinnere, hat Poincaré bewiesen, dass es nicht lösbar ist.)  
Aber ich habe eine numerische Lösung mit dem vorher vorgestellten
[Runge-Kutta Löser]({filename}/schmetterlingseffekt.md)
erstellt. Und ich habe einen hübschen Film daraus gemacht.

<video controls="controls" height="600" width="600">
<source src="{filename}/vid/dreiKorper.mp4" type="video/mp4"></source>
<source src="{filename}/vid/dreiKorper.webm" type="video/webm"></source>
Your browser does not support the video tag.
</video>

Als Standbild ist es nicht ganz so ästhetisch, wie der
[Lorenz-Attraktor]({filename}/schmetterlingseffekt.md),
aber animiert ist es -- meiner Meinung nach -- wunderbar anzusehen.

Und hier die Startwerte: (bei einer Gravitationskonstanten von 1)  
Blau: $M=5, x_0=0, y_0=0, v_x0=0, v_y0=0$  
Rot : $M=1, x_0=1, y_0=0, v_x0=0, v_y0=1$  
Grün: $M=1, x_0=1, y_0=1, v_x0=1, v_y0=0$
