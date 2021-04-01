import data_manipulations

second = data_manipulations.convert_long_time("1:23:42.123")
longtime = data_manipulations.convert_seconds(second)

print(second, longtime)
