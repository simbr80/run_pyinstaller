import subprocess
import os
from pathlib import Path
import shutil
import sys


def create_exe():
    orig_file = sys.argv[1]
    # orig_file = r"C:\Users\sbrence\PycharmProjects\gurs_snemanje_datotek_nepremicnine\dl_gurs_nepremicnine_backup_ver.1.0.py"
    orig_file_path = Path(orig_file)
    file_name = orig_file.rsplit("\\", 1)[1]

    # Ustvari folder z istim imenom kot je file, vendar brez .py koncnice
    working_file_to_dir = orig_file.rsplit(".", 1)[0]
    working_file_to_dir_path = Path(working_file_to_dir)

    dist_path = Path(working_file_to_dir_path, "dist")
    build_path = Path(working_file_to_dir_path, "build")
    spec_path = list(working_file_to_dir_path.glob('*.spec'))
    if spec_path:
        spec_path = spec_path[0]


    if dist_path.exists():
        delete = input("Izbrisi obstojeco exe distribucijo in vse datoteke (d/n) ?")
        if delete == "d":
            shutil.rmtree(working_file_to_dir_path, ignore_errors=True)
            print("Izbrisal sem celotno staro mapo in datoteke")

        else:
            print("Nicesar nisem izbrisal. Zakljucujem proceduro.")
            return None

    working_file_to_dir_path.mkdir(parents=True, exist_ok=True)
    print("Ustvaril novo mapo")

    # Spremeni direktorji
    os.chdir(working_file_to_dir)

    # Skopiraj file v novo mapo
    new_file_path = Path(working_file_to_dir + '\\' + file_name)
    shutil.copy(orig_file_path, new_file_path)  # For Python 3.8+.
    print("Skoprila file v novo mapo")

    print("Poganjam cmd ukaze...")
    commands = ['python -m venv env', f'{working_file_to_dir}\\env\\Scripts\\activate.bat',
                'pip install pipreqs', f'pipreqs "{working_file_to_dir}"', 'pip install -r requirements.txt',
                'pip install pyinstaller', 'pip install lxml',
                f'{working_file_to_dir}\\env\\Scripts\\pyinstaller.exe --onefile {str(new_file_path)}',
                'pip freeze > requirements.txt', f'{working_file_to_dir}\\env\\Scripts\\deactivate.bat'
                ]
    str_commands = ' && '.join(commands)
    os.system(str_commands)
    print("Zakljucil s poganjanjem cmd ukazov.")

# process = subprocess.Popen(['python', '-m', 'venv', 'env'],
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE, shell=True)
# stdout, stderr = process.communicate()
# stdout, stderr


if __name__ == '__main__':
    create_exe()
