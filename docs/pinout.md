# Pinout

![schematics](img/schematic.png)

## Controller

[`ESP32-S3-Pico`][esp32-s3-pico]

| Usage     | ADC        | Name       | Pin | ESP32 | Pin | Name   | Usage         |
| ---------:| ----------:| ----------:| ---:|:-----:|:--- |:------ |:------------- |
|           |            |     `VBUS` |  40 |  USB  |   1 | `GP11` | `MP1 CORE`    |
|           |            |     `VSYS` |  39 |       |   2 | `GP12` | `S3`          |
|   PWR GND |            |      `GND` |  38 |       |   3 | `GND`  |               |
|           |            |   `3V3_EN` |  37 |       |   4 | `GP13` | (`MP2 KNOB`)  |
|   PWR VCC |            | `3V3(OUT)` |  36 |       |   5 | `GP14` | `S2`          |
|           | `ADC1_CH9` |     `GP10` |  35 |       |   6 | `GP15` | `S1`          |
| I²C `SCL` | `ADC1_CH8` |      `GP9` |  34 |       |   7 | `GP16` | `S0`          |
|           |            |      `GND` |  33 |       |   8 | `GND`  |               |
| I²C `SDA` | `ADC1_CH7` |      `GP8` |  32 |       |   9 | `GP17` | (`MP3 SLIDE`) |
|           | `ADC1_CH6` |      `GP7` |  31 |       |  10 | `GP18` |               |
|           |            |      `RUN` |  30 |       |  11 | `GP33` | (`SR1 CORE`)  |
|           | `ADC1_CH5` |      `GP6` |  29 |       |  12 | `GP34` | (`SR2 DIST`)  |
|           |            |      `GND` |  28 |       |  13 | `GND`  |               |
|           | `ADC1_CH4` |      `GP5` |  27 |       |  14 | `GP35` | `SPI MOSI`    |
|           | `ADC1_CH3` |      `GP4` |  26 |       |  15 | `GP36` | `SPI CLK`     |
|           | `ADC1_CH1` |      `GP2` |  25 |       |  16 | `GP37` | `SPI MISO`    |
|     `SIG` | `ADC1_CH0` |      `GP1` |  24 |       |  17 | `GP38` |               |
|           |            |      `GND` |  23 |       |  18 | `GND`  |               |
|  (`JOY1`) |            |     `GP41` |  22 |       |  19 | `GP39` |               |
|  (`JOY2`) |            |     `GP42` |  21 |       |  20 | `GP40` |               |


## Analog Bus

`CD74HC4067M` (read)

| Usage             | Pin `CD74HC4067M` |        Pin `ESP32` |
| ----------------- | -----------------:| ------------------:|
| Adress (shared)   |              `S0` |             `GP16` |
| Adress (shared)   |              `S1` |             `GP15` |
| Adress (shared)   |              `S2` |             `GP14` |
| Adress (shared)   |              `S3` |             `GP12` |
| Signal (shared)   |             `SIG` | `ADC1_CH0` / `GP1` |
| Enable MP1_Core   |              `EN` |             `GP11` |
| Enable MP2_Knob   |              `EN` |           (`GP13`) |
| Enable MP1_Slider |              `EN` |           (`GP17`) |


## Digital Bus: SPI

[`74HC165`][74hc165] (read), `74HC959` (write)

| Usage                 |   Pin `74HC165` |    Pin `74HC959` |         Pin `ESP32` |
| --------------------- | ---------------:| ----------------:| -------------------:|
| `SCK` Clock (shared)  |            `CP` |          `SRCLK` | `GP36` (`FSPI_CLK`) |
| `MOSI` Write (shared) |             --- |            `SER` |              `GP35` |
| `MISO` Read (shared)  |            `Q7` |              --- |   `GP37` (`FSPI_Q`) |
| Enable SR1_Core       |           `PL'` |              --- |            (`GP33`) |
| Enable SR2_Distance   |           `PL'` |              --- |            (`GP34`) |
|                       |                 |             `OE` |                     |

|  Wiring |           Usage | Name  | Pin | `74HC165` | Pin | Name  | Usage       | Wiring  |
| -------:| ---------------:| -----:|----:|:---------:|:----|:----- |:----------- |:------- |
|   `SRX` | latch (trigger) | `PL'` |   1 |     U     |  16 | `VCC` | `VCC`       | `3V3`   |
|  `GP36` |       `SPI CLK` |  `CP` |   2 |           |  15 | `CE'` | chip enable | `GND`   |
| _input_ |           input |  `D4` |   3 |           |  14 | `D3`  | input       | _input_ |
| _input_ |           input |  `D5` |   4 |           |  13 | `D2`  | input       | _input_ |
| _input_ |           input |  `D6` |   5 |           |  12 | `D1`  | input       | _input_ |
| _input_ |           input |  `D7` |   6 |           |  11 | `D0`  | input       | _input_ |
|     --- |    output (inv) | `Q7'` |   7 |           |  10 | `DS`  | daisy chain | `3V3`   |
|   `GND` |           `GND` | `GND` |   8 |           |   9 | `Q7`  | `SPI MISO`  | `GP37`  |

Inputs cannot be left floating: either tie to LOW/HIGH or use Pull-Up/Down resisotrs (5--10k)

[esp32-s3-pico]: https://files.waveshare.com/wiki/common/Esp32-s3_datasheet_en.pdf
[74hc165]: https://assets.nexperia.com/documents/data-sheet/74HC_HCT165.pdf
