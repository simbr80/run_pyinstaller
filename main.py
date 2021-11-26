import subprocess
import os
from pathlib import Path

path = r"C:\Users\sbrence\PycharmProjects\gurs_snemanje_datotek_nepremicnine\dl_gurs_nepremicnine_backup_ver.1.0.py"
w_path = Path(path)

# process = subprocess.Popen(['mkdir', '123'],
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE, shell=True)
# stdout, stderr = process.communicate()
# stdout, stderr
#
#
# wd = os.getcwd()
# os.chdir("/")
# subprocess.Popen("dir")
# os.chdir(wd)

working_dir = path.rsplit("\\", 1)[0]
working_file = path.rsplit("\\", 1)[1]

# Ustvari folder z istimo imenom kot je file, vendar brez .py koncnice
working_file_to_dir = path.rsplit(".", 1)[0]
Path(working_file_to_dir).mkdir(parents=True, exist_ok=True)
os.chdir(path)



# # This is a sample Python script.
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
