# from abc import ABC, abstractmethod

from analogio import AnalogIn
from digitalio import DigitalInOut

ANALOG_MAX = 65535


class Control:  # (ABC):
    # @abstractmethod
    def poll(self) -> bool | tuple[bool, ...]: ...

    @property
    # @abstractmethod
    def value(self) -> (float | int | bool) | tuple[float | int | bool, ...]: ...


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


class Joystick(Control):
    """Iduino ST1079

    https://botland.de/joystick-arduino-joystick/4093-daumen-joystick-mit-taste-v2-modul-mit-platine-iduino-st1079-5903351241441.html
    """

    def __init__(
        self,
        x: AnalogIn,
        y: AnalogIn,
        sw: DigitalInOut | None = None,
        threshold: int = 200,
    ):
        # TODO auto-calib, calib params
        self._x = Potentiometer(x, threshold=threshold)
        self._y = Potentiometer(y, threshold=threshold)
        self.pin_sw = sw

        self._value_sw = None if sw is None else False

    def poll(self):
        changed_x = self._x.poll()
        changed_y = self._y.poll()

        if self.pin_sw is not None:
            value_sw = not self.pin_sw.value
            changed_sw = value_sw != self._value_sw
            self._value_sw = value_sw
        else:
            changed_sw = False

        return changed_x, changed_y, changed_sw

    @property
    def value(self) -> tuple[float, float, bool | None]:
        return self._x.value, self._y.value, self._value_sw
