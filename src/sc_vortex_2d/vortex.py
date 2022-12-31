import importlib.resources
import pickle
from enum import Enum
from typing import Dict, List, Tuple

from scipy import interpolate

from .data_vortex import t03, t05, t08
from .vortex_instance import VortexInstance


class _DictKey(str, Enum):
    DELTA_KEY = "delta"


class _FileName(str, Enum):
    delta = "delta.pkl"
    spectra = "spectra.pkl"
    u = "u.pkl"
    v = "v.pkl"


class GeneralParameters(Enum):
    KF_XI = 50
    MAX_ANGULAR_MOMENTUM = 69
    MIN_ANGULAR_MOMENTUM = -70
    SIZE_KF = 400


class VortexInstanceT03(VortexInstance):
    class Parameters(Enum):
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
        self.construct()

    def construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            t03
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int):
        return self.spectra_dict[i]


class VortexInstanceT05(VortexInstance):
    class Parameters(Enum):
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
        self.construct()

    def construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            t05
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int):
        return self.spectra_dict[i]


class VortexInstanceT08(VortexInstance):
    class Parameters(Enum):
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
        self.construct()

    def construct(self) -> None:
        self.pair_potential, self.spectra_dict, self.u_dict, self.v_dict = _construct(
            t08
        )

    def get_pair_potential(self) -> interpolate.CubicSpline:
        return self.pair_potential

    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicSpline]:
        return self.u_dict[i], self.v_dict[i]

    def get_ith_eigen_energy(self, i: int):
        return self.spectra_dict[i]


def _make_spline(x_vector: List[float], f: List[float]) -> interpolate.CubicSpline:
    return interpolate.CubicSpline(x_vector, f)


def _construct(package):
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
        package, _FileName.delta.value
    ) as delta, importlib.resources.open_binary(
        package, _FileName.spectra.value
    ) as spc, importlib.resources.open_binary(
        package, _FileName.u.value
    ) as u, importlib.resources.open_binary(
        package, _FileName.v.value
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
