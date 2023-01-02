# sc_vortex_2d
This library provide numerical result of s-wave Caroli-de Gennes-Matricon mode (CdGM mode) at $T/T_c=0.3, 0.5, 0.8$.
You can get eigenenergy, eigenfunction and pair potential at each temperature.

## Description
It is known that there is low-energy excitation levels inside the s-wave vortex core in the superconductor.
These states are got by solving following Bogoliubov-de Gennes equation(BdG eq) self-consistently.

$$
\left[-\frac{1}{2k_{F}\xi_{0}}\nabla^{2}-\mu\right]\mathcal{U}_{q}(\boldsymbol{r})+\Delta(\boldsymbol{r})\mathcal{V}_{q}(\boldsymbol{r}) = E_{q}\mathcal{U}_{q}(\boldsymbol{r}) 
$$

$$
\left[\frac{1}{2k_{F}\xi_{0}}\nabla^{2}+\mu\right]\mathcal{V}_{q}(\boldsymbol{r})+\Delta^{*}(\boldsymbol{r})\mathcal{U}_{q}(\boldsymbol{r}) = E_{q}\mathcal{V}_{q}(\boldsymbol{r})  
$$

$$
\Delta(\boldsymbol{r})=g\sum_{E_{q}\leq E_{\mathrm{c}}} \mathcal{U}_{q}(r)\mathcal{V}_{q}^{*}(r)[1-2f(E_{q})] 
$$

Here, BdG eq is rewritten in dimensionless form using Pippard length $\xi_{0} = \hbar v_{F}/\Delta_{0}$ and zero-temperature bulk gap $\Delta_{0}$.
$f(E_{q})$ is Fermi distribution function. Solutions in an isolated vortex, especially CdGM mode is given by following form.

$$
\begin{bmatrix}
\mathcal{U}_{n}(r, \theta) \\
\mathcal{V}_{n}(r, \theta)
\end{bmatrix}
=\frac{1}{\sqrt{2\pi}}
\begin{bmatrix}
u_{n}(r)e^{i(n-1)\theta} \\
v_{n}(r)e^{in\theta}
\end{bmatrix}
$$


Here, $n$ corresponds to angular momentum quantum number, i.e. CdGM mode is characterized by this number. In this library, the range of $n$ is integers of in $[-70, 69]$. Note that the part of $u_{n}(r), v_{n}(r)$ in the right side of above formula is one of the target of this library, not the left side of it.

## Install

## Link
https://webpark1378.sakura.ne.jp/
