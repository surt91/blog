Title: DGLshow
Date: 2014-03-19 11:28
Author: surt91
Category: Code
Tags: C++, Physik
Slug: dglshow
Status: published

<video controls="controls" height="576" width="592">
<source src="vid/doppelpendel.mp4" type="video/mp4"></source>
![Doppelpendel]](img/doublePendulum.png)
</video>


Das ist ein Doppelpendel. Soetwas möchte man eigentlich auf seinem
Schreibtisch stehen haben. Aber dann stellt man fest, dass ein
Doppelpendel viel zu teuer ist, und entschließt sich, dass ein
virtuelles auf dem virtuellen Schreibtisch ausreicht.

Also erinnert man sich an eine alte Vorlesung, schreibt ein kleines C++
Programm mit einen adaptiven Runge-Kutta-4 Löser, das mit den Qt
Zeichenprimitiven Lösungen visualisiert.

\begin{align}
    (m_1 + m_2) l_1 \ddot{\theta_1} + m_2 l_2 \ddot{\theta_2} \cos(\theta_1 - \theta_2) + m_2 l_2 \dot{\theta_2}^2 \sin(\theta_1 - \theta_2) + g(m_1 + m_2) \sin(\theta_1) &= 0\\
    m_2 l_2 \ddot{\theta_2} + m_2 l_1 \ddot{\theta_1} \cos(\theta_1 - \theta_2) - m_2 l_1 \dot{\theta_1}^2 sin(\theta_1 - \theta_2) + m_2 g \sin(\theta_2) &= 0
\end{align}

Das sind die Differentialgleichung für die beiden Winkel des Doppelpendels. 
Anfangs empfiehlt es sich also etwas einfacheres und vertrauteres zu lösen.
Ich habe mich für en [Lorenz Attraktor]({filename}/schmetterlingseffekt.md)
\begin{align}
    \dot{X} &= a(Y - X) \\
    \dot{Y} &= X(b - Z) - Y \\
    \dot{Z} &= XY - cZ \\
\end{align}
und ein [Dreikörper Problem]({filename}/dreikorperproblem.md) 
entschieden.
Außerdem ein Sonnensystem/Bohrsches Atommodell.

![Sonnensystem](img/planets.png)

Auch wenn der Code nicht sehr aufgeräumt ist -- und er wird vermutlich
auch nie besser aussehen -- sind die Quellen auf GitHub:
[github.com/surt91/DGLshow](https://github.com/surt91/DGLshow).

