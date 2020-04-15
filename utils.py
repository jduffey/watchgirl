import os
from config import number_color_dict


def synchronize_time():
    command = 'sudo ntpdate -s'
    target = 'time.nist.gov'
    print(f'Syncing time with {target}')
    os.system(command + ' ' + target)


def get_color(digit_to_use_for_color):
    return number_color_dict[int(digit_to_use_for_color, 16) % 4]