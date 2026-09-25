# Kangaroo Catcher

A small Python project that demonstrates a countability-based search strategy.

An invisible kangaroo moves on the integer lattice \(\mathbb{Z}^2\). Its initial position and velocity are unknown, but all four parameters are integers.

The goal is to place one trap per time step and guarantee that the kangaroo is eventually caught.

---

## Problem

The kangaroo starts at

\[
(x_0, y_0) \in \mathbb{Z}^2
\]

and moves by the same integer vector

\[
(a,b) \in \mathbb{Z}^2
\]

after every step.

Therefore, after \(t\) steps its position is

\[
K(t) = (x_0 + at,\; y_0 + bt).
\]

The four integers

\[
x_0,\ y_0,\ a,\ b
\]

are unknown.

At every time step \(t\), we may choose exactly one lattice point and place a trap there.

The question is:

> Is there a strategy that guarantees catching the kangaroo after finitely many steps?

Yes.

---

# Mathematical idea

Every possible kangaroo trajectory is completely determined by a quadruple

\[
(x_0,y_0,a,b) \in \mathbb{Z}^4.
\]

The key fact is that

\[
\mathbb{Z}^4
\]

is countable.

That means all possible trajectories can be arranged into a sequence

\[
H_0,H_1,H_2,\ldots
\]

where

\[
H_t =
\left(
x_0^{(t)},
y_0^{(t)},
a^{(t)},
b^{(t)}
\right).
\]

At time \(t\), we take hypothesis \(H_t\) and place the trap where the kangaroo would be at that moment if this hypothesis were correct:

\[
T(t)
=
\left(
x_0^{(t)} + a^{(t)}t,\;
y_0^{(t)} + b^{(t)}t
\right).
\]

Suppose the real trajectory is

\[
H_m=(x_0,y_0,a,b).
\]

Because every quadruple appears somewhere in the enumeration, such a finite index \(m\) must exist.

At time \(m\), the trap is placed at

\[
T(m)
=
(x_0+am,\;y_0+bm),
\]

which is exactly the kangaroo's real position

\[
K(m).
\]

Therefore the kangaroo is caught no later than step \(m\).

It may be caught earlier if a different hypothetical trajectory happens to intersect the real one at the correct time.

---

# Why countability matters

The strategy works because

\[
\mathbb{Z}^4
\]

is countable.

A finite Cartesian product of countable sets is countable, so four integer parameters can be enumerated.

This is an example of a general principle:

> If every possible hidden state can be encoded by a finite tuple of integers, then the set of hypotheses is countable and can, in principle, be searched exhaustively.

If the parameters were arbitrary real numbers instead,

\[
(x_0,y_0,a,b)\in\mathbb{R}^4,
\]

the same enumeration argument would no longer work because \(\mathbb{R}^4\) is uncountable.

---

# Enumeration strategy

A simple implementation could repeatedly enumerate the full cube

\[
[-r,r]^4
\]

for

\[
r=0,1,2,\ldots
\]

and keep only points satisfying

\[
\max(|x_0|,|y_0|,|a|,|b|)=r.
\]

That works, but it repeatedly scans old points.

This project instead generates only the new boundary of each 4-dimensional cube.

For radius \(r\), the new hypotheses are exactly

\[
[-r,r]^4
\setminus
[-(r-1),r-1]^4.
\]

The number of new quadruples is

\[
(2r+1)^4-(2r-1)^4.
\]

To avoid duplicates, every quadruple is classified by the first coordinate that reaches the boundary value \(\pm r\).

---

# Complexity

The number of integer quadruples satisfying

\[
\max(|x_0|,|y_0|,|a|,|b|)\le R
\]

is

\[
(2R+1)^4.
\]

So any exhaustive enumeration that reaches every such quadruple must process

\[
\Theta(R^4)
\]

hypotheses.

The optimized generator in this project also performs

\[
\Theta(R^4)
\]

generation work up to radius \(R\).

A naive implementation that re-enumerates the entire cube for every radius would perform

\[
\sum_{r=0}^{R}(2r+1)^4
=
\Theta(R^5)
\]

iterations.

So generating only the new boundary improves the asymptotic enumeration cost from

\[
\Theta(R^5)
\]

to

\[
\Theta(R^4).
\]

---

# Project structure

```text
kangaroo-catcher/
├── main.py
├── tests.py
├── README.md
└── .gitignore
```

---

# Run

Requires Python 3.10+.

```bash
python main.py
```

Example:

```text
Kangaroo Catcher
================

Choose the kangaroo's hidden trajectory.
The kangaroo starts at (x0, y0) and moves
by the fixed integer vector (a, b) every step.

Initial x-coordinate x0: 1
Initial y-coordinate y0: -1
Horizontal step a: 0
Vertical step b: 1

Searching...

The kangaroo has been caught.
Step: ...
Position: (...)
Hypothesis used: (...)
```

The exact catching step depends on the order in which hypotheses are enumerated.

---

# Run tests

The tests use `pytest`.

Install it:

```bash
pip install pytest
```

Then run:

```bash
pytest
```

---

# Main concepts

This project illustrates several ideas from discrete mathematics and theoretical computer science:

- countable sets;
- Cartesian products of countable sets;
- exhaustive search;
- generators and lazy evaluation;
- correctness proofs;
- asymptotic complexity;
- enumeration algorithms.

The main point is that the algorithm is not designed to be fast for large coordinates.

It demonstrates the difference between

> "efficiently find"

and

> "guarantee that the object will eventually be found."

---

# Possible extensions

Some natural extensions are:

1. Visualize the kangaroo and trap positions with `matplotlib`.
2. Compare naive and optimized enumeration experimentally.
3. Generalize the search to \(\mathbb{Z}^d\).
4. Measure the number of hypotheses generated before capture.
5. Try alternative enumerations of \(\mathbb{Z}^4\).
6. Investigate what changes when some parameters are bounded.
7. Study why the analogous argument fails for arbitrary real parameters.

---

# License

This project is intended for educational use.
