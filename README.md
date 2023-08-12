# sc-vortex-2d
This library provide numerical results of s-wave Caroli-de Gennes-Matricon mode (CdGM mode) at 
$T/T_c=0.3, 0.5, 0.8$.
You can get the eigenenergy, eigenfunction and pair potential at each temperature.

## Description
It is known that there are low-energy excitation levels inside the s-wave vortex core in the superconductor.
These states are got by solving following Bogoliubov-de Gennes equation(BdG eq) self-consistently.

```math
\left[-\frac{1}{2k_{F}\xi_{0}}\nabla^{2}-\mu\right]\mathcal{U}_{q}(\boldsymbol{r})+\Delta(\boldsymbol{r})\mathcal{V}_{q}(\boldsymbol{r}) = E_{q}\mathcal{U}_{q}(\boldsymbol{r}) 
```

```math
\left[\frac{1}{2k_{F}\xi_{0}}\nabla^{2}+\mu\right]\mathcal{V}_{q}(\boldsymbol{r})+\Delta^{*}(\boldsymbol{r})\mathcal{U}_{q}(\boldsymbol{r}) = E_{q}\mathcal{V}_{q}(\boldsymbol{r})  
```

```math
\Delta(\boldsymbol{r})=g\sum_{E_{q}\leq E_{\mathrm{c}}} \mathcal{U}_{q}(r)\mathcal{V}_{q}^{*}(r)[1-2f(E_{q})] 
```

Here, BdG eq is rewritten in dimensionless form using Pippard length $\xi_{0} = \hbar v_{F}/\Delta_{0}$ and zero-temperature bulk gap $\Delta_{0}$.
$f(E_{q})$ is Fermi distribution function. Solutions in an isolated vortex, especially CdGM mode is given by following form.

```math
\begin{bmatrix}
\mathcal{U}_{n}(r, \theta) \\
\mathcal{V}_{n}(r, \theta)
\end{bmatrix}
=\frac{1}{\sqrt{2\pi}}
\begin{bmatrix}
u_{n}(r)e^{in\theta} \\
v_{n}(r)e^{i(n + 1)\theta}
\end{bmatrix}
```


Here, $n$ corresponds to angular momentum quantum number, i.e. CdGM mode is characterized by this number. In this library, the range of $n$ is integers of in $[-100, 99]$. Note that the part of $u_{n}(r), v_{n}(r)$ in the right side of above formula is one of the target of this library, not the left side of it.

## Install
You can install via [PyPI](https://pypi.org/). For example,

```
 $ pip install  sc-vortex-2d 
```

## Usage
```python
"""Sample python code"""

from sc_vortex_2d.vortex import VortexInstanceT03
from scipy import interpolate

instance: VortexInstanceT03 = VortexInstanceT03()

delta: interpolate.CubicSpline = instance.get_pair_potential() 

e0: float = instance.get_ith_eigen_energy(0) # lowest energy level in the region of e > 0.

u0, v0 = instance.get_ith_eigen_func(0) # get wave functions

params = instance.Parameters # Parameters of the system. Enum.

```
## Links
- https://webpark1378.sakura.ne.jp/
- [F. Gygi and M. Schlüter, Phys. Rev. B, 41, 822 (1990)](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.41.822)
