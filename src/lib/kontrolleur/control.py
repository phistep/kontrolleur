# from abc import ABC, abstractmethod

from analogio import AnalogIn
from digitalio import DigitalInOut, Pull
from microcontroller import Pin
from rotaryio import IncrementalEncoder

ANALOG_MAX = 65535


class Control:  # (ABC):
    # @abstractmethod
    def poll(self) -> bool | tuple[bool, ...]: ...

    @property
    # @abstractmethod
    def value(self) -> (float | int | bool | None) | tuple[
        float | int | bool | None, ...
    ]: ...


class Button(Control):
    # TODO `keypad.ShiftRegisterKeys` for more efficiency
    # TODO toggle

    def __init__(self, pin: Pin):
        from adafruit_debouncer import Debouncer

        _pin = DigitalInOut(pin)
        _pin.pull = Pull.UP
        self._button = Debouncer(_pin)
        self._value = False

    def poll(self) -> bool:
        self._button.update()
        if self._button.fell:
            self._value = True
            changed = True
        elif self._button.rose:
            self._value = False
            changed = True
        else:
            changed = False
        return changed

    @property
    def value(self) -> bool:
        return self._value


class Toggle(Control):
    def __init__(self, pin: Pin):
        from adafruit_debouncer import Debouncer

        _pin = DigitalInOut(pin)
        _pin.pull = Pull.UP
        self._button = Debouncer(_pin)
        self._value = False

    def poll(self) -> bool:
        self._button.update()
        if self._button.fell:
            self._value = not self._value
            return True
        return False

    @property
    def value(self) -> bool:
        return self._value


class Potentiometer(Control):
    def __init__(self, pin: AnalogIn, tolerance: int = 200):
        self._tolerance = tolerance
        self._value = 0
        self.pin = pin

    def poll(self):
        value = self.pin.value
        changed = abs(self._value - value) > self._tolerance
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

    # TODO use as delta

    def __init__(
        self,
        x: AnalogIn,
        y: AnalogIn,
        sw: DigitalInOut | None = None,
        tolerance: int = 200,
    ):
        # TODO auto-calib, calib params
        self._x = Potentiometer(x, tolerance=tolerance)
        self._y = Potentiometer(y, tolerance=tolerance)
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


class Distance(Control):
    """HCSR04

    https://learn.adafruit.com/ultrasonic-sonar-distance-sensors/overview
    """

    def __init__(
        self,
        trig: Pin,
        echo: Pin,
        max_: float = 30.0,
        tolerance: float = 0.5,
        average: int = 3,
    ):
        from adafruit_hcsr04 import HCSR04

        self._value = 0
        self._max = max_
        self._tolerance = tolerance
        self._average = average
        self._sensor = HCSR04(trigger_pin=trig, echo_pin=echo)

    def poll(self):
        try:
            value = (
                sum(self._sensor.distance for _ in range(self._average)) / self._average
            )
            if value > self._max:
                # changed = self._value != self._max
                # self._value = self._max
                changed = False
            else:
                changed = abs(self._value - value) > self._tolerance
                self._value = value
        except RuntimeError as e:
            print(self, e)
            changed = False
        return changed

    @property
    def value(self) -> float:
        # TODO return max on idle
        # TODO keep value when goes to zero
        value = 1 - (min(self._value, self._max) / self._max)
        return value


class Encoder(Control):
    """EC12

    https://botland.de/encoder/6909-encoder-mit-taster-24-impulse-12mm-ec12-vertikal-5-stk-5903351245432.html
    https://learn.adafruit.com/bluetooth-le-hid-volume-knob-with-circuitpython/build-the-ble-volume-knob
    """

    def __init__(self, a: Pin, b: Pin, btn: Pin):
        self._value = 0
        self._prev_value = 0
        self._encoder = IncrementalEncoder(a, b)
        # TODO button

    def poll(self) -> tuple[bool, bool, bool]:
        value = self._encoder.position
        # check prev state to emit _off_ signal of pulse
        decrement = value < self._value or self._value < self._prev_value
        increment = value > self._value or self._value > self._prev_value
        self._prev_value = self._value
        self._value = value
        return decrement, increment, False

    @property
    def value(self) -> tuple[bool, bool, bool]:
        decrement = self._value < self._prev_value
        increment = self._value > self._prev_value
        button = None
        return decrement, increment, button
