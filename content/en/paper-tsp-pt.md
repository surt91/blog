Title: Phase Transitions of Traveling Salesperson Problems solved with Linear Programming and Cutting Planes
Date: 2018-07-31 06:28
Author: surt91
Category: Phys
Tags: Publication, Physics
Slug: paper-tsp-pt
Status: published
Lang: en
Doi: 10.1209/0295-5075/113/30004

In this Article, we introduce an ensemble of the Traveling Salesperson problem (TSP)
that can be tuned with a parameter $\sigma$ from the trivial case of cities
equidistant on a circle to the random Euclidean TSP in a plane.
For this ensemble we determine some phase transitions from an "easy" phase to
a "not-that-easy" phase using linear programming. For each of these transitions
we present structural properties of the optimal solution, which change at these
points characteristically. Since the optimal solution is independent of the
solution method, those phase transitions are not only relevant for the specific
linear program respectively the solver implementation used to solve them, but
a fundamental property of this TSP ensemble.

We used the classical linear program of Dantzig:
\begin{align}
    \label{eq:objective}
    &\text{minimize}     &  \sum_i \sum_{j<i} c_{ij} x_{ij}\\
    \label{eq:int}
    &\text{subject to}   &  x_{ij}                                &\in \{0,1\}\\ %\mathbb{Z}\\
    \label{eq:inout}
    &                    &  \sum_{j} x_{ij}                       &= 2&            & \forall i \in V \\
    \label{eq:sec}
    &                    &  \sum_{i \in S, j \notin S} x_{ij}     &\ge 2&          & \forall S \varsubsetneq V, S \ne \varnothing
\end{align}
As the order parameter of the transitions we use the probability that a simplex
solver yields an integer, and therefore optimal, solution. Without the last
contraint \eqref{eq:sec}, the "Subtour Elimination Constraints",
the transition occurs at the point at which the optimal solution deviates
from the order of the cities on the initial circle. With the "Subtour
Elimination Constraints" the transition coincides with the point at which
the optimal tour changes from a zig-zag course to larger meandering arcs.
This is measured by the tortuosity
\begin{align*}
    \tau = \frac{n-1}{L} \sum_{i=1}^{n} \brac{\frac{L_i}{S_i}-1}.
\end{align*}
which is maximal at this point. For the tortuosity the tour is divided in $N$
parts of same-sign-curvature. For each part the ratio of the direct end-to-end
distance $S_i$ to the length along the arc $L_i$ is summed.
