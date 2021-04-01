def convert_long_time(long_time):
    reverse_list = long_time.split(':')[::-1]
    total_time = 0
    for index, item in enumerate(reverse_list):
        seconds = float(item) * pow(60, index)
        total_time += seconds
    return total_time

def convert_seconds(seconds):
    secondsleft = seconds
    hour = int(seconds / 3600)
    secondsleft = secondsleft % 3600
    minute = str(int(secondsleft / 60)).zfill(2)
    secondsleft = '{:06.3f}'.format(round(secondsleft % 60, 5))
    outstring = ""
    if hour:
        outstring += f"{hour}:"
    if minute != "00" or hour:
        outstring += f"{minute}:"
    outstring += f"{secondsleft}"
    return outstring
