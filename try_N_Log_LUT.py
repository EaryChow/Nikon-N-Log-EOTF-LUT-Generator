import colour
import numpy
import pathlib


def n_log_curve(x):
    curve_lower = ((x / (650 / 1024)) ** 3) - 0.0075
    curve_upper = numpy.exp((x - 619 / 1024) / (150 / 1024))
    curve = numpy.where(x < 452/1024, curve_lower, curve_upper)

    return curve


x_input = numpy.linspace(0.0, 1.0, 4096)
y_LUT = n_log_curve(x_input)

LUT_name = "N_Log_Curve_EOTF"
LUT_safe = LUT_name.replace(" ", "_")
LUT = colour.LUT1D(
    table=y_LUT,
    name=LUT_safe
)

colour.io.luts.write_LUT(LUT, "{}.spi1d".format(LUT_safe), method="Sony SPI1D")