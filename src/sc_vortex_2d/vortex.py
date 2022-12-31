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


class VortexInstanceT03(VortexInstance):
    class Parameters(Enum):
        KF_XI = 50
        DELTA_OVER_CDGM = 31.363654447926976
        T_OVER_TC = 0.3
        MAX_ANGULAR_MOMENTUM = 69
        MIN_ANGULAR_MOMENTUM = -70
        SIZE_KF = 400

    def __init__(self) -> None:
        self.pair_potential: interpolate.CubicSpline
        self.u_dict: Dict[int, interpolate.CubicSpline] = dict()
        self.v_dict: Dict[int, interpolate.CubicSpline] = dict()
        self.spectra_dict: Dict[int, float] = dict()
        self.construct()

    def construct(self) -> None:

        kfr: List[float] = [
            i * 0.1
            for i in range(
                0, self.Parameters.SIZE_KF.value * 10 + 1
            )  # [0.0, 0.1, 0.2, ..., 400]
        ]

        with importlib.resources.open_binary(t03, _FileName.delta.value) as f:
            delta_dict: Dict[str, List[float]] = pickle.load(f)
            self.pair_potential = _make_spline(
                kfr, delta_dict[_DictKey.DELTA_KEY.value]
            )

        with importlib.resources.open_binary(
            t03, _FileName.spectra.value
        ) as spc, importlib.resources.open_binary(
            t03, _FileName.u.value
        ) as u, importlib.resources.open_binary(
            t03, _FileName.v.value
        ) as v:
            self.spectra_dict = pickle.load(spc)
            u_load = pickle.load(u)
            v_load = pickle.load(v)
            for i in range(
                self.Parameters.MIN_ANGULAR_MOMENTUM.value,
                self.Parameters.MAX_ANGULAR_MOMENTUM.value + 1,
            ):  
                self.u_dict[i] = _make_spline(kfr, u_load[i])
                self.v_dict[i] = _make_spline(kfr, v_load[i])

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
        KF_XI = 50
        DELTA_OVER_CDGM = 43.66058913995896
        T_OVER_TC = 0.5
        MAX_ANGULAR_MOMENTUM = 69
        MIN_ANGULAR_MOMENTUM = -70

    def get_pair_potential(self) -> interpolate.CubicSpline:
        pass

    def get_ith_eigen_func():
        pass

    def get_ith_eigen_energy():
        pass


def cdgm_t05(x: float):
    pass


class VortexInstanceT08(VortexInstance):
    class Parameters(Enum):
        KF_XI = 50
        DELTA_OVER_CDGM = 64.11317362045985
        T_OVER_TC = 0.8
        MAX_ANGULAR_MOMENTUM = 69
        MIN_ANGULAR_MOMENTUM = -70

    def get_pair_potential(self) -> interpolate.CubicSpline:
        pass

    def get_ith_eigen_func():
        pass

    def get_ith_eigen_energy():
        pass


def _make_spline(x_vector: List[float], f: List[float]) -> interpolate.CubicSpline:
    return interpolate.CubicSpline(x_vector, f)


def cdgm_t08(x: float):
    pass
