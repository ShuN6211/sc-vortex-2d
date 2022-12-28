from abc import ABC, abstractmethod
from typing import Tuple
from scipy import interpolate


class VortexInstance(ABC):
    @abstractmethod
    def get_pair_potential(self) -> interpolate.CubicSpline:
        pass

    @abstractmethod
    def get_ith_eigen_func(
        self, i: int
    ) -> Tuple[interpolate.CubicSpline, interpolate.CubicHermiteSpline]:
        pass

    @abstractmethod
    def get_ith_eigen_energy(self, i: int) -> float:
        pass
