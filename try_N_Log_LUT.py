import colour
import numpy
import pathlib

output_config_directory = "."
output_LUTs_directory = "."
x_input = numpy.linspace(0.0, 1.0, 4096)


def n_log_curve(x):
    curve_lower = ((x/(650/1024))**3) - 0.0075
    curve_upper = numpy.exp((x-619/1024)/(150/1024))

    curve = numpy.where(x < 0.328, curve_lower, curve_upper)

    return curve


y_LUT = n_log_curve(x_input)

LUT_name = "N_Log_Curve_EOTF"
LUT_safe = LUT_name.replace(" ", "_")
LUT = colour.LUT1D(
    table=y_LUT,
    name="N_Log_Curve_EOTF"
)

try:
    output_directory = pathlib.Path(output_config_directory)
    LUTs_directory = output_directory / output_LUTs_directory
    LUT_filename = pathlib.Path(
        LUTs_directory / "{}.spi1d".format(LUT_safe)
    )
    LUTs_directory.mkdir(parents=True, exist_ok=True)
    colour.io.luts.write_LUT(LUT, LUT_filename, method="Sony SPI1D")

except Exception as ex:
    raise ex