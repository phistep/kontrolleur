# from abc import ABC, abstractmethod

from analogio import AnalogIn

ANALOG_MAX = 65535


class Control:  # (ABC):
    # @abstractmethod
    def poll(self) -> bool: ...

    @property
    # @abstractmethod
    def value(self) -> float | int | bool: ...


class Potentiometer(Control):
    def __init__(self, pin: AnalogIn, threshold: int = 200):
        self._threshold = threshold
        self._value = 0
        self.pin = pin

    def poll(self):
        value = self.pin.value
        changed = abs(self._value - value) > self._threshold
        self._value = value
        return changed

    @property
    def value(self) -> float:
        value = self._value / ANALOG_MAX
        assert 0.0 <= value <= 1.0, f"out of range: {self._value}"
        return value
