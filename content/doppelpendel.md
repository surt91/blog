Title: Doppelpendel
Date: 2014-03-19 11:27
Author: surt91
Category: Code
Tags: Physik, Video, Bild, Formel, Chaos
Slug: dglshow
LargeFeaturedImage: img/doublePendulum.png
Status: published
Lang: de

<video controls width="100%" poster="/img/doublePendulum.png">
<source src="/vid/doppelpendel.mp4" type="video/mp4"></source>
![Doppelpendel](/img/doublePendulum.png)
</video>

Das ist ein Doppelpendel. Ein Doppelpendel ist neben dem [Dreikörperproblem]({filename}/dreikorperproblem.md)
und dem Lorenz-Attraktor [[1]({filename}/schmetterlingseffekt.md), [2]({filename}/seltsamer-attraktor.md)]
das Paradebeispiel für analytisch unlösbare Bewegungsgleichungen
und chaotisches Verhalten. Aus diesem Grund sollte ein Doppelpendel auf keinem
Schreibtisch fehlen und bietet sich als grandiose Geschenkidee für Physiker an.

Dass es analytisch unlösbar ist, lässt sich mit einem nicht rigorosen Argument
anschaulich machen: Ein Blick auf die Bewegungsgleichungen:

\begin{align*}
    (m_1 + m_2) l_1 \ddot\vartheta_1 + m_2 l_2 \ddot\vartheta_2 \cos(\vartheta_1 - \vartheta_2) + m_2 l_2 \dot\vartheta_2^2 \sin(\vartheta_1 - \vartheta_2) + g(m_1 + m_2) \sin(\vartheta_1) &= 0\\
    m_2 l_2 \ddot\vartheta_2 + m_2 l_1 \ddot\vartheta_1 \cos(\vartheta_1 - \vartheta_2) - m_2 l_1 \dot\vartheta_1^2 \sin(\vartheta_1 - \vartheta_2) + m_2 g \sin(\vartheta_2) &= 0
\end{align*}

Das sind die Differentialgleichungen für die beiden Winkel $\vartheta_1$ und $\vartheta_2$
des Doppelpendels. $m_i$ sind die beiden Massen und $l_i$ die Fadenlängen.

Unser Ziel ist es das obige Video zu erstellen, dazu müssen wir die Bahnkurve,
also $\vartheta_1(t)$ und $\vartheta_2(t)$ bestimmen.
Dazu müssen wir die obigen Gleichungen, die sich relativ simpel,
[wenn auch mühsam, per Lagrange-Formalismus herleiten lassen](/img/doppelpendel_math.webp),
zunächst nach den Winkelbeschleunigungen aufgelösen.

\begin{align*}
    \ddot\vartheta_1 &= \frac{m_2 \cos(\vartheta_1 - \vartheta_2) (l_1 \sin(\vartheta_1 - \vartheta_2) \dot\vartheta_1^2 - g \sin(\vartheta_2)) + m_2 l_2 \sin(\vartheta_1 - \vartheta_2) \dot\vartheta_2^2 + (m_1 + m_2) g \sin(\vartheta_1)}{m_2 l_1 \cos^2(\vartheta_1 - \vartheta_2) - (m_1+m_2) l_1} \\
    \ddot\vartheta_2 &= \frac{m_2 l_2 \cos(\vartheta_1 - \vartheta_2) \sin(\vartheta_1 - \vartheta_2) \dot\vartheta_2^2 + (m_1+m_2) l_1 \sin(\vartheta_1 - \vartheta_2) \dot\vartheta_1^2 + (m_1+m_2) g \cos(\vartheta_1 - \vartheta_2) \sin(\vartheta_1) - (m_1+m_2) g \sin(\vartheta_2)}{(m_1+m_2) l_2 - m_2 l_2 \cos^2(\vartheta_1 - \vartheta_2)}
\end{align*}

Diese Gleichungen sind durchaus sehr unhandlich und können nicht analytisch,
gelöst werden -- aber [numerisch ist es kein Problem]({filename}/dglshow.md).

