Title: DGLshow
Date: 2014-03-19 11:28
Author: surt91
Category: Code
Tags: C++, Physik, Video, Bild, GitHub, Formel, Chaos
Slug: dglshow
LargeFeaturedImage: img/doublePendulum.png
Status: published
Lang: de

Nachdem ich so vielen Differenzialgleichungssystemen [[1]({filename}/dreikorperproblem.md), [2]({filename}/schmetterlingseffekt.md), [3]({filename}/seltsamer-attraktor.md), [4]({filename}/doppelpendel.md)]
begegnet bin, die sich nicht analytisch lösen lassen, habe ich mir ein
[Programm zur numerischen Lösung und Visualisierung derselben geschrieben](https://github.com/surt91/DGLshow).

<video controls width="100%" poster="/img/doublePendulum.png">
<source src="/vid/doppelpendel.mp4" type="video/mp4"></source>
![Doppelpendel](/img/doublePendulum.png)
</video>

Die grundlegende Idee zur numerischen Lösung von Differentialgleichungen ist es, die Zeit
in diskreten Schritten $\tau$ vergehen zu lassen. Nach jedem Schritt wird der
Zustand so geändert, als ob sich während des Zeitschrittes nichts geändert
hätte und die "Kräfte" werden entsprechend der Bewegungsgleichungen neu berechnet.
Für infinitesimal kleine $\tau \to \mathrm{d}t$ ist diese Methode schließlich exakt.

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
Phasen zu verbringen. Es gibt spezialisierte Methoden, die sehr gut für bestimmte Bewegungsgleichungen
funktionieren, wie [Velocity-Verlet](https://en.wikipedia.org/wiki/Verlet_integration),
der oft für Molekulardynamiksimulationen eingesetzt wird.

Chaotische Systeme haben in der Regel etwas kompliziertere Bewegungsgleichungen. Das oben abgebildete
Doppelpendel etwa wird, [wie ich in einem anderen Post beschrieben habe]({filename}/doppelpendel.md)
durch folgendes Ungetüm beschrieben.

\begin{align*}
    \ddot\theta_1 &= \frac{m_2 \cos(\theta_1 - \theta_2) (l_1 \sin(\theta_1 - \theta_2) \dot\theta_1^2 - g \sin(\theta_2)) + m_2 l_2 \sin(\theta_1 - \theta_2) \dot\theta_2^2 + (m_1 + m_2) g \sin(\theta_1)}{m_2 l_1 \cos^2(\theta_1 - \theta_2) - (m_1+m_2) l_1} \\
    \ddot\theta_2 &= \frac{m_2 l_2 \cos(\theta_1 - \theta_2) \sin(\theta_1 - \theta_2) \dot\theta_2^2 + (m_1+m_2) l_1 \sin(\theta_1 - \theta_2) \dot\theta_1^2 + (m_1+m_2) g \cos(\theta_1 - \theta_2) \sin(\theta_1) - (m_1+m_2) g \sin(\theta_2)}{(m_1+m_2) l_2 - m_2 l_2 \cos^2(\theta_1 - \theta_2)}
\end{align*}

Anfangs empfiehlt es sich also etwas einfacheres und vertrauteres zu lösen,
wie den [Lorenz-Attraktor]({filename}/schmetterlingseffekt.md)
\begin{align*}
    \dot{X} &= a(Y - X) \\
    \dot{Y} &= X(b - Z) - Y \\
    \dot{Z} &= XY - cZ \\
\end{align*}

Oder das [Dreikörperproblem]({filename}/dreikorperproblem.md)
\begin{align*}
    \ddot{\vec{x}_1} &= -\frac{Gm_2}{\left(x_1 - x_2\right)^3} (\vec{x}_1 - \vec{x}_2) - \frac{Gm_3}{\left(x_1 - x_3\right)^3} (\vec{x}_1 - \vec{x}_3)\\
    \ddot{\vec{x}_2} &= -\frac{Gm_1}{\left(x_2 - x_1\right)^3} (\vec{x}_2 - \vec{x}_1) - \frac{Gm_3}{\left(x_2 - x_3\right)^3} (\vec{x}_2 - \vec{x}_3)\\
    \ddot{\vec{x}_3} &= -\frac{Gm_1}{\left(x_3 - x_1\right)^3} (\vec{x}_3 - \vec{x}_1) - \frac{Gm_2}{\left(x_3 - x_2\right)^3} (\vec{x}_3 - \vec{x}_2)\\
\end{align*}

Da man das 3-Körperproblem trivial auf ein $N$-Körperproblem erweitern kann,
habe ich hier ein "Sonnensystem" bzw. Bohrsches "Atom"-modell simuliert.

![Sonnensystem](/img/planets.png)

Um die obigen (bewegten) Bilder zu erzeugen und um ein bewegtes Doppelpendel
für meinen Schreibtisch zu haben, -- wennauch nur auf einem Bildschirm -- habe
ich in C++ einen adaptiven Runge-Kutta-4 Löser geschrieben, der mit den Qt
Zeichenprimitiven animiert wird.

Auch wenn der Code nicht sehr aufgeräumt ist und Startwerte im Quellcode
angepasst werden müssen, sind die Quellen auf GitHub:
[github.com/surt91/DGLshow](https://github.com/surt91/DGLshow).
