import importlib.resources
import pickle
from enum import Enum
from typing import Dict, List, Tuple

from scipy import interpolate

from .data_vortex import temperature_03, temperature_05, temperature_08
from .vortex_instance import VortexInstance


class _DictKey(str, Enum):
    DELTA_KEY = "delta"


class _FileName(str, Enum):
    delta = "delta.pkl"
    spectra = "spectra.pkl"
    u = "u.pkl"
    v = "v.pkl"


class GeneralParameters(Enum):
    """GeneralParameters

    Parameters independent of temperature.

    Attributes:
        KF_XI: Value of fermi wave number multiplied by pippard length. This is
               equivalent to value of 2 times zero-temperature bulk gap devided by
               fermi energey. (k_F * xi = 2 * E_F / Delta_0)
        MAX_ANGULAR_MOMENTUM: Max value of angular momentum quantum number.
        MIN_ANGULAR_MOMENTUM: Min value of angular momentum quantum number.
        SIZE_KF: Systemsize scaled by fermi wave number, this is used in
                 calculation of self-consistent equation(BdG).

    """

    KF_XI = 50
    MAX_ANGULAR_MOMENTUM = 99
    MIN_ANGULAR_MOMENTUM = -100
    SIZE_KF = 400


class VortexInstanceT03(VortexInstance):
    class Parameters(Enum):
        """Parameters

        Parameters involving parameters depending on temperature.

        Attributes:
            KF_XI: Value of fermi wave number multiplied by pippard length. This is
                   equivalent to value of 2 times zero-temperature bulk gap devided by
                   fermi energey. (k_F * xi = 2 * E_F / Delta_0)
            DELTA_OVER_CDGM: Value of zero-temperature bulk gap devided by
                             level spacing of CdGM mode.
            T_OVER_TC: Temperature scaled by taransition temperature T_c.
            MAX_ANGULAR_MOMENTUM: Max value of angular momentum quantum number.
            MIN_ANGULAR_MOMENTUM: Min value of angular momentum quantum number.
            SIZE_KF: Systemsize scaled by fermi wave number, this is used in
                     calculation of self-consistent equation(BdG).

        """

        KF_XI = GeneralParameters.KF_XI.value
        DELTA_OVER_CDGM = 31.363654447926976
        T_OVER_TC = 0.3
        MAX_ANGULAR_MOMENTUM = GeneralParameters.MAX_ANGULAR_MOMENTUM.value
        MIN_ANGULAR_MOMENTUM = GeneralParameters.MIN_ANGULAR_MOMENTUM.value
        SIZE_KF = GeneralParameters.SIZE_KF.value

    def __init__(self) -> None:
        self.pair_potential: interpolate.CubicSpline
        self.spectra_dict: Dict[int, float] = dict()
        self.u_dict: Dict[int, interpolate.CubicSpline] = dict()
        self.v_dict: Dict[int, interpolate.CubicSpline] = dict()
        self._construct()

    def _construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            temperature_03
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        """get_pair_potential()

        This method returns pair potential at T = 0.3 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        Value of pair potential is scaled by zero-temperature bulk gap.

        Returns:
            scipy.interpolate.CubicSpline: pair potential at T = 0.3 T_c
        """
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        """get_ith_eigen_func()

        This method returns ith eigen functions (u, v) at T = 0.3 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        As u and v have dimension of inverse of L.L, value of them
        is scaled by 2 times fermi wave number. (k_F * k_F)

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            Tuple[scipy.interpolate.CubicSpline, scipy.interpolate.CubicSpline]:
                ith eigen functions (u_i, v_i)
        """
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int) -> float:
        """get_ith_eigen_energy()

        This method returns ith eigen energy e_i at T = 0.3 T_c.

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            float: Value of ith eigen energy e_i scaled by level spacing of CdGM mode.
        """
        return self.spectra_dict[i]


class VortexInstanceT05(VortexInstance):
    class Parameters(Enum):
        """Parameters

        Parameters involving parameters depending on temperature.

        Attributes:
            KF_XI: Value of fermi wave number multiplied by pippard length. This is
                   equivalent to value of 2 times zero-temperature bulk gap devided by
                   fermi energey. (k_F * xi = 2 * E_F / Delta_0)
            DELTA_OVER_CDGM: Value of zero-temperature bulk gap devided by
                             level spacing of CdGM mode.
            T_OVER_TC: Temperature scaled by taransition temperature T_c.
            MAX_ANGULAR_MOMENTUM: Max value of angular momentum quantum number.
            MIN_ANGULAR_MOMENTUM: Min value of angular momentum quantum number.
            SIZE_KF: Systemsize scaled by fermi wave number, this is used in
                     calculation of self-consistent equation(BdG).

        """

        KF_XI = GeneralParameters.KF_XI.value
        DELTA_OVER_CDGM = 43.66058913995896
        T_OVER_TC = 0.5
        MAX_ANGULAR_MOMENTUM = GeneralParameters.MAX_ANGULAR_MOMENTUM.value
        MIN_ANGULAR_MOMENTUM = GeneralParameters.MIN_ANGULAR_MOMENTUM.value
        SIZE_KF = GeneralParameters.SIZE_KF.value

    def __init__(self) -> None:
        self.pair_potential: interpolate.CubicSpline
        self.spectra_dict: Dict[int, float] = dict()
        self.u_dict: Dict[int, interpolate.CubicSpline] = dict()
        self.v_dict: Dict[int, interpolate.CubicSpline] = dict()
        self._construct()

    def _construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            temperature_05
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        """get_pair_potential()

        This method returns pair potential at T = 0.5 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        Value of pair potential is scaled by zero-temperature bulk gap.

        Returns:
            scipy.interpolate.CubicSpline: pair potential at T = 0.5 T_c
        """
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        """get_ith_eigen_func()

        This method returns ith eigen functions (u, v) at T = 0.5 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        As (u, v) have dimension of inverse of L.L, value of them
        is scaled by 2 times fermi wave number. (k_F * k_F)

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            Tuple[scipy.interpolate.CubicSpline, scipy.interpolate.CubicSpline]:
                ith eigen functions (u_i, v_i)
        """
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int):
        """get_ith_eigen_energy()

        This method returns ith eigen energy e_i at T = 0.5 T_c.

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            float: Value of ith eigen energy e_i scaled by level spacing of CdGM mode.
        """
        return self.spectra_dict[i]


class VortexInstanceT08(VortexInstance):
    class Parameters(Enum):
        """Parameters

        Parameters involving parameters depending on temperature.

        Attributes:
            KF_XI: Value of fermi wave number multiplied by pippard length. This is
                   equivalent to value of 2 times zero-temperature bulk gap devided by
                   fermi energey. (k_F * xi = 2 * E_F / Delta_0)
            DELTA_OVER_CDGM: Value of zero-temperature bulk gap devided by
                             level spacing of CdGM mode.
            T_OVER_TC: Temperature scaled by taransition temperature T_c.
            MAX_ANGULAR_MOMENTUM: Max value of angular momentum quantum number.
            MIN_ANGULAR_MOMENTUM: Min value of angular momentum quantum number.
            SIZE_KF: Systemsize scaled by fermi wave number, this is used in
                     calculation of self-consistent equation(BdG).

        """

        KF_XI = GeneralParameters.KF_XI.value
        DELTA_OVER_CDGM = 64.11317362045985
        T_OVER_TC = 0.8
        MAX_ANGULAR_MOMENTUM = GeneralParameters.MAX_ANGULAR_MOMENTUM.value
        MIN_ANGULAR_MOMENTUM = GeneralParameters.MIN_ANGULAR_MOMENTUM.value
        SIZE_KF = GeneralParameters.SIZE_KF.value

    def __init__(self) -> None:
        self.pair_potential: interpolate.CubicSpline
        self.spectra_dict: Dict[int, float] = dict()
        self.u_dict: Dict[int, interpolate.CubicSpline] = dict()
        self.v_dict: Dict[int, interpolate.CubicSpline] = dict()
        self._construct()

    def _construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            temperature_08
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        """get_pair_potential()

        This method returns pair potential at T = 0.8 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        Value of pair potential is scaled by zero-temperature bulk gap.

        Returns:
            scipy.interpolate.CubicSpline: pair potential at T = 0.8 T_c.
        """
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        """get_ith_eigen_func()

        This method returns ith eigen functions (u, v) at T = 0.8 T_c.
        Radial coordinates is scaled by inverse of fermi wave number.
        As (u, v) have dimension of inverse of L.L, value of them
        is scaled by 2 times fermi wave number. (k_F * k_F)

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            Tuple[scipy.interpolate.CubicSpline, scipy.interpolate.CubicSpline]:
                ith eigen functions (u_i, v_i)
        """
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int):
        """get_ith_eigen_energy()

        This method returns ith eigen energy e_i at T = 0.8 T_c.

        Args:
            i (int): Angular momentum quantum number you want to get.
        Returns:
            float: Value of ith eigen energy e_i scaled by level spacing of CdGM mode.
        """
        return self.spectra_dict[i]


def _make_spline(x_vector: List[float], f: List[float]) -> interpolate.CubicSpline:
    return interpolate.CubicSpline(x_vector, f)


def _construct(my_package):
    delta_dict: Dict[str, List[float]] = dict()
    u_dict: Dict[int, interpolate.CubicSpline] = dict()
    v_dict: Dict[int, interpolate.CubicSpline] = dict()
    spectra_dict: Dict[int, float] = dict()

    kfr: List[float] = [
        i * 0.1
        for i in range(
            0, GeneralParameters.SIZE_KF.value * 10 + 1
        )  # [0.0, 0.1, 0.2, ..., 400]
    ]

    with importlib.resources.open_binary(
        my_package, _FileName.delta.value
    ) as delta, importlib.resources.open_binary(
        my_package, _FileName.spectra.value
    ) as spc, importlib.resources.open_binary(
        my_package, _FileName.u.value
    ) as u, importlib.resources.open_binary(
        my_package, _FileName.v.value
    ) as v:

        delta_dict: Dict[str, List[float]] = pickle.load(delta)
        pair_potential = _make_spline(kfr, delta_dict[_DictKey.DELTA_KEY.value])

        spectra_dict = pickle.load(spc)
        u_load = pickle.load(u)
        v_load = pickle.load(v)
        for i in range(
            GeneralParameters.MIN_ANGULAR_MOMENTUM.value,
            GeneralParameters.MAX_ANGULAR_MOMENTUM.value + 1,
        ):
            u_dict[i] = _make_spline(kfr, u_load[i])
            v_dict[i] = _make_spline(kfr, v_load[i])

    return pair_potential, spectra_dict, u_dict, v_dict
