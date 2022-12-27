from vortex_instance import VortexInstance
import json
import gzip
from enum import Enum
from scipy import interpolate
from typing import Dict, List


class JsonPath(str, Enum):
    KFR_PATH = "./json/kfr.json.gz"
    DELTA_T03_PATH = "./json/T03/delta.json.gz"
    SPECTRA_T03_PATH = "./json/T03/spectra.json.gz"
    U_T03_PATH = "./json/T03/u.json.gz"
    V_T03_PATH = "./json/T03/v.json.gz"


class JsonKey(str, Enum):
    DELTA_KEY = "delta"
    DELTA_OVER_CDGM_KEY = "delta_over_CdGM"
    KFR_KEY = "kfr"


class VortexInstanceT03(VortexInstance):
    class Parameters(Enum):
        KF_XI = 50
        DELTA_OVER_CDGM = 31.363654447926976
        T_OVER_TC = 0.3
        MAX_ANGULAR_MOMENTUM = 69
        MIN_ANGULAR_MOMENTUM = -70

    def __init__(self) -> None:
        self.kfr: List[float]
        self.pair_potential: interpolate.CubicSpline
        self.u_dict: Dict[int, interpolate.CubicHermiteSpline]
        self.v_dict: Dict[int, interpolate.CubicHermiteSpline]
        self.spectra_dict: Dict[int, float]
        self.construct_flag = True

    def construct(self) -> None:
        if self.construct_flag:
            with gzip.open(JsonPath.KFR_PATH.value, "r") as f:
                kfr_dict: Dict[str, List[float]] = json.load(f)
                self.kfr = kfr_dict[JsonKey.KFR_KEY.value]

            with gzip.open(JsonPath.DELTA_T03_PATH.value, "r") as f:
                delta_dict: Dict[str, List[float]] = json.load(f)
                self.pair_potential = make_spline(self.kfr, delta_dict[JsonKey.DELTA_KEY.value])

            with gzip.open(JsonPath.SPECTRA_T03_PATH.value, "r") as f:
                spectra_dict: Dict[str, float] = json.load(f)
                for i in range(
                    self.Parameters.MIN_ANGULAR_MOMENTUM,
                    self.Parameters.MAX_ANGULAR_MOMENTUM + 1,
                ):
                    self.spectra_dict[i] = spectra_dict[f"{i}"]

            with gzip.open(JsonPath.U_T03_PATH.value, "r") as f:
                u_dict: Dict[str, List[float]] = json.load(f)
                for i in range(
                    self.Parameters.MIN_ANGULAR_MOMENTUM,
                    self.Parameters.MAX_ANGULAR_MOMENTUM + 1,
                ):
                    self.u_dict[i] = make_spline(self.kfr, u_dict[f"{i}"])

            with gzip.open(JsonPath.V_T03_PATH.value, "r") as f:
                v_dict: Dict[str, List[float]] = json.load(f)
                for i in range(
                    self.Parameters.MIN_ANGULAR_MOMENTUM,
                    self.Parameters.MAX_ANGULAR_MOMENTUM + 1,
                ):
                    self.v_dict[i] = make_spline(self.kfr, v_dict[f"{i}"])
            self.construct_flag = False

    def get_pair_potential(self) -> interpolate.CubicSpline:
        return self.pair_potential

    def get_ith_eigen_func():
        pass

    def get_ith_eigen_energy():
        pass


def cdgm_t03(x: float):
    pass


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


def make_spline(x_vector: List[float], f: List[float]) -> interpolate.CubicSpline:
    return interpolate.CubicSpline(x_vector, f)


def cdgm_t08(x: float):
    pass
