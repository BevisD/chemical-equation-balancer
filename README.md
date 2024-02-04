# chemical-equation-balancer

The aim of this project is to apply my knowledge of regex and systems of linear simultaneous equations to balancing chemical equations. 

The input is a string of the unbalanced equation, for example: $$CO_2 + H_2O \rightarrow C_6 H_{12} O_6 + O_2$$

This can be expressed generally as:  $$a\*CO_2 + b\*H_2O \rightarrow c\*C_6 H_{12} O_6 + d\*O_2$$

Regex is used to parse this input and a produce a system of linear simultaenous equations. 

Equating Terms:


$C$:  $a\*(1) + b\*(0) = c\*(6) + d\*(0)$

$O$:  $a\*(2) + b\*(1) = c\*(6) + d\*(2)$

$H$:  $a\*(0) + b\*(2) = c\*(12) + d\*(0)$

Since there are infinitely many solutions connected by a multiplication of all all coefficients by a scalar, we set the one coefficient to $1$ in this case $d$ 

This is then expressed as a matrix

$$
\begin{pmatrix}
1 & 0 & -6\\
2 & 1 & -6\\
0 & 2 & -12\\
\end{pmatrix}
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
\=
\begin{pmatrix}
0 \\
2 \\
0 \\
\end{pmatrix}
$$

Inverting the matrix gives:

$$
\begin{pmatrix}
a \\
b \\
c \\
\end{pmatrix}
\=
\begin{pmatrix}
0 & \frac{1}{2} & -\frac{1}{4} \\
-1 & \frac{1}{2} & \frac{1}{4} \\
-\frac{1}{6} & \frac{1}{12} & -\frac{1}{24} \\
\end{pmatrix}
\begin{pmatrix}
0 \\
2 \\
0 \\
\end{pmatrix}
\=
\begin{pmatrix}
1 \\
1 \\
\frac{1}{6} \\
\end{pmatrix}
$$

The solutions are scaled until all are integers resulting in the blanced equation:
$$6CO_2 + 6H_2O \rightarrow C_6 H_{12} O_6 + 6O_2$$



