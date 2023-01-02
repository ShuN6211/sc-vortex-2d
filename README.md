# sc_vortex_2d
Provide numerical result of s-wave Caroli-de Gennes-Matricon mode (CdGM mode) at $T/T_c=0.3, 0.5, 0.8$.
You can get eigenenergy, eigenfunction and pair potential.

## Description
It is known that there is low-energy excitation levels inside the vortex core in the superconductor.
The state is got by solving Bogoliubov-de Gennes equation self-consistently.

$$
\left[-\frac{1}{2k_{F}\xi_{0}}\nabla^{2}-\mu\right]\mathcal{U}_{q}(\boldsymbol{r})+\Delta(\boldsymbol{r})\mathcal{V}_{q}(\boldsymbol{r}) = E_{q}\mathcal{U}_{q}(\boldsymbol{r}) 
$$

$$
\left[\frac{1}{2k_{F}\xi_{0}}\nabla^{2}+\mu\right]\mathcal{V}_{q}(\boldsymbol{r})+\Delta^{*}(\boldsymbol{r})\mathcal{U}_{q}(\boldsymbol{r}) = E_{q}\mathcal{V}_{q}(\boldsymbol{r})  
$$

$$
\begin{bmatrix} 
-\frac{1}{2k_{F}\xi_{0}}\nabla^{2} - \mu & \Delta(\bm{r}) \\
\Delta(\bm{r})^{*} & \frac{1}{2k_{F}\xi_{0}}\nabla^{2} + \mu
\end{bmatrix}
\begin{bmatrix}
\mathcal{U}_{q}(\bm{r}) \\ \mathcal{V}_{q}(\bm{r})
\end{bmatrix}
=E_{q}
\begin{bmatrix}
\mathcal{U}_{q}(\bm{r}) \\ \mathcal{V}_{q}(\bm{r})
\end{bmatrix} 
$$