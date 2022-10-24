Title: Phase Transitions of Traveling Salesperson Problems solved with Linear Programming and Cutting Planes
Date: 2018-07-31 06:28
Author: surt91
Category: Phys
Tags: Publication, Physics
Slug: paper-tsp-pt
Status: published
LargeFeaturedImage: img/tsp_interp.png
Lang: en
Doi: 10.1209/0295-5075/113/30004

In this Article, we introduce an ensemble of the Traveling Salesperson problem (TSP)
that can be tuned with a parameter $\sigma$ from the trivial case of cities
equidistant on a circle to the random Euclidean TSP in a plane.

![Einfach und schwierig zu lösende TSP Konfigurationen](/img/tsp_interp.svg){: class="invertable"}

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

Here $c_{ij}$ is the distance matrix between all pairs of cities
of $V$ and $x_{ij}$ is the adjacency matrix, i.e., $x_{ij} = 1$,
if $i$ and $j$ are consecutive in the tour and $x_{ij} = 0$ otherwise.
Therefore, the first line minimizes the length of the tour.
To avoid that we conclude that $x_{ij} = 0$, i.e., staying at home,
is identified as the optimal tour, we introduce the third line to
force each city to have two connections, enough to enter and leave.
But our salesman is clever and can trick us by choosing
$x_{ij} = 0.5$. Since we can not interpret this, we introduce line 2
to force all $x_{ij}$ to integers.
Still valid are two unconnected tours, which we forbid with
the fourth line, the *subtour elimination constraints*.
Well, the careful reader might already see that we defined
one constraint for each subset of the cities, which are exponentially
many in the number of cities. But we can solve this by starting
without this class of constraints and only adding the ones which
are actually violated by a solution. The violated ones can luckily
be found easily by calculating the [minimum cut](https://en.wikipedia.org/wiki/Minimum_cut) of the proposed solution. The corresponding
constraint can be added and the procedure is repeated until no
subtour elimination constraint is violated anymore.

So does that mean that we found an efficient algorithm to solve
the traveling salesperson problem? No, unfortunately we can not
claim the [Millenium Prize](https://en.wikipedia.org/wiki/Millennium_Prize_Problems#P_versus_NP) yet. There is no known
algorithm which can efficiently solve this problem under the
integer constraint.
But if we drop this constraint, we can use efficient algorithms
of linear programming to solve the
[relaxation](https://en.wikipedia.org/wiki/Linear_programming_relaxation). The resulting length will always
be a lower bound on the actual solution and if we, by chance, find
an integer solution, we can be sure that it is actually the
optimal solution.

As the order parameter of the transitions from easy to hard we use the probability that a simplex
solver yields an integer, and therefore optimal, solution. Without  the Subtour Elimination Constraints,
the transition occurs at the point at which the optimal solution deviates
from the order of the cities on the initial circle. With the Subtour
Elimination Constraints the transition coincides with the point at which
the optimal tour changes from a zig-zag course to larger meandering arcs.
This is measured by the tortuosity
\begin{align*}
    \tau = \frac{n-1}{L} \sum_{i=1}^{n} \left( \frac{L_i}{S_i}-1 \right).
\end{align*}
which is maximal at this point. For the tortuosity the tour is divided in $N$
parts of same-sign-curvature. For each part the ratio of the direct end-to-end
distance $S_i$ to the length along the arc $L_i$ is summed.

So, we detected continuous phase transitions in the hardness
of the problem with linear programming and correlated them
with structural changes.