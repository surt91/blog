Title: DGLshow
Date: 2014-03-19 11:28
Author: surt91
Category: Code
Tags: C++, Physik, Video, Bild, GitHub, Formel, Chaos
Slug: dglshow
Status: published
Lang: de

<video controls width="100%" poster="{filename}/img/doublePendulum.png">
<source src="{filename}/vid/doppelpendel.mp4" type="video/mp4"></source>
![Doppelpendel]({filename}/img/doublePendulum.png)
</video>

Das ist ein Doppelpendel. Ein Doppelpendel ist neben dem Dreikörperproblem und
dem Lorenz-Attraktor das Paradebeispiel für analytisch unlösbare Bewegungsgleichungen 
und chaotisches Verhalten. Aus diesem Grund sollte ein Doppelpendel auf keinem 
Schreibtisch fehlen und bietet sich als grandiose Geschenkidee für Physiker an.

Dass es analytisch unlösbar ist, lässt sich mit einem nicht rigorosen Argument
anschaulich machen: Ein Blick auf die Bewegungsgleichungen

\begin{align*}
    (m_1 + m_2) l_1 \ddot\theta_1 + m_2 l_2 \ddot\theta_2 \cos(\theta_1 - \theta_2) + m_2 l_2 \dot\theta_2^2 \sin(\theta_1 - \theta_2) + g(m_1 + m_2) \sin(\theta_1) &= 0\\
    m_2 l_2 \ddot\theta_2 + m_2 l_1 \ddot\theta_1 \cos(\theta_1 - \theta_2) - m_2 l_1 \dot\theta_1^2 \sin(\theta_1 - \theta_2) + m_2 g \sin(\theta_2) &= 0
\end{align*}

Das sind die Differentialgleichungen für die beiden Winkel $\theta_1$ und $\theta_2$
des Doppelpendels. $m_i$ sind die beiden Massen und $l_i$ die Fadenlängen.

Dieses Gleichungssystem ist zwar nicht analytisch lösbar, aber das numerische
Simulieren eines Doppelpendels ist kein großes Problem und liefert das obige
Video.

Die grundlegende Idee zur Lösung von Differentialgleichungen ist es, die Zeit
in diskreten Schritten $\tau$ vergehen zu lassen. Nach jedem Schritt wird der
Zustand so geändert, als ob sich während des Zeitschrittes nichts geändert
hätte und die "Kräfte" werden entsprechend der Bewegungsgleichungen neu berechnet.

Im einfachsten Fall, dem Euler Verfahren, sähe das für ein einfaches 
Fadenpendel nach $k$ Zeitschritten so aus
\begin{align*}
    \ddot\vartheta_{k+1} &= - mgl \sin(\vartheta_k)\\
    \dot\vartheta_{k+1} &= \tau \ddot\vartheta_{k+1} + \dot\vartheta_{k}\\
    \vartheta_{k+1} &= \tau \dot\vartheta_k + \vartheta_{k}
\end{align*}
Unglücklicherweise hat dieses Verfahren ernsthafte Probleme mit der Energieerhaltung
und braucht sehr kleine $\tau$ für brauchbare Ergebnisse.
Es gibt deutlich ausgefeiltere Methoden, wie den [klassischen Runge-Kutta](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods#The_Runge.E2.80.93Kutta_method)
Algorithmus. Es gibt Methoden, den Zeitschritt $\tau$ während der Simulation
adaptiv anzupassen, um nur wenig Rechenaufwand in den wenig fehleranfälligen
Phasen zu verbringen. Es gibt spezialisierte Methoden, die nur für bestimmte Bewegungsgleichungen
funktionieren, wie [Velocity-Verlet](https://en.wikipedia.org/wiki/Verlet_integration),
der oft für Molekulardynamiksimulationen eingesetzt wird.

Damit man $\ddot{\theta_1}$ und $\ddot{\theta_2}$ müssen die obigen Gleichungen,
die sich relativ simpel, wennauch mühsam, per Lagrange-Formalismus herleiten 
lassen, sodass es zunächst noch nach den Winkelbeschleunigungen aufgelöst werden.

\begin{align*}
    \ddot\theta_1 &= \frac{m_2 \cos(\theta_1 - \theta_2) (l_1 \sin(\theta_1 - \theta_2) \dot\theta_1^2 - g \sin(\theta_2)) + m_2 l_2 \sin(\theta_1 - \theta_2) \dot\theta_2^2 + (m_1 + m_2) g \sin(\theta_1)}{m_2 l_1 \cos^2(\theta_1 - \theta_2) - (m_1+m_2) l_1} \\
    \ddot\theta_2 &= \frac{m_2 l_2 \cos(\theta_1 - \theta_2) \sin(\theta_1 - \theta_2) \dot\theta_2^2 + (m_1+m_2) l_1 \sin(\theta_1 - \theta_2) \dot\theta_1^2 + (m_1+m_2) g \cos(\theta_1 - \theta_2) \sin(\theta_1) - (m_1+m_2) g \sin(\theta_2)}{(m_1+m_2) l_2 - m_2 l_2 \cos^2(\theta_1 - \theta_2)}
\end{align*}

Diese Geichungen sind durchaus sehr unhandlich.

Anfangs empfiehlt es sich also etwas einfacheres und vertrauteres zu lösen.
Ich habe mich für den [Lorenz Attraktor]({filename}/schmetterlingseffekt.md)
\begin{align*}
    \dot{X} &= a(Y - X) \\
    \dot{Y} &= X(b - Z) - Y \\
    \dot{Z} &= XY - cZ \\
\end{align*}
und ein [Dreikörper Problem]({filename}/dreikorperproblem.md)
\begin{align*}
    \ddot{\vec{x}_1} &= -\frac{Gm_2}{\left(x_1 - x_2\right)^3} (\vec{x}_1 - \vec{x}_2) - \frac{Gm_3}{\left(x_1 - x_3\right)^3} (\vec{x}_1 - \vec{x}_3)\\
    \ddot{\vec{x}_2} &= -\frac{Gm_1}{\left(x_2 - x_1\right)^3} (\vec{x}_2 - \vec{x}_1) - \frac{Gm_3}{\left(x_2 - x_3\right)^3} (\vec{x}_2 - \vec{x}_3)\\
    \ddot{\vec{x}_3} &= -\frac{Gm_1}{\left(x_3 - x_1\right)^3} (\vec{x}_3 - \vec{x}_1) - \frac{Gm_2}{\left(x_3 - x_2\right)^3} (\vec{x}_3 - \vec{x}_2)\\
\end{align*}
entschieden.

Da man das 3-Körperproblem trivial auf ein $N$-Körperproblem erweitern kann,
habe ich hier ein "Sonnensystem" bzw. Bohrsches "Atom"-modell simuliert.

![Sonnensystem]({filename}/img/planets.png)

Um die obigen (bewegten) Bilder zu erzeugen und um ein bewegtes Doppelpendel
für meinen Schreibtisch zu haben, -- wennauch nur auf einem Bildschirm -- habe
ich in C++ einen adaptiven Runge-Kutta-4 Löser geschrieben, der mit den Qt
Zeichenprimitiven animiert wird.

Auch wenn der Code nicht sehr aufgeräumt ist und Startwerte im Quellcode
angepasst werden müssen, sind die Quellen auf GitHub:
[github.com/surt91/DGLshow](https://github.com/surt91/DGLshow).

