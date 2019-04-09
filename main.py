#!/usr/bin/python3

# Описание работы скрипта
#   Скрипт переименовывает расширения гербер-файлов с одинаковым именем
#   в текущей папке
#   *.F.Cupper -> *.TOP
#
# пример:
# elgp0001_p0.drl             --> elgp0001_p0.drl
# elgp0001_p0-B.Cu.gbr        --> elgp0001_p0.bot
# elgp0001_p0-B.Mask.gbr      --> elgp0001_p0.smb
# elgp0001_p0-B.SilkS.gbr     --> elgp0001_p0.ssb
# elgp0001_p0-Edge.Cuts.gbr   --> elgp0001_p0.brd
# elgp0001_p0-F.Cu.gbr        --> elgp0001_p0.top
# elgp0001_p0-F.Mask.gbr      --> elgp0001_p0.smt
# elgp0001_p0-F.SilkS.gbr     --> elgp0001_p0.sst
#
#   входной параметр: имя файла с "неправильным" расширением
#

# имя файла может содержать полный путь или быть без пути, тогда берем
# текущий путь

# в имени файла не допускается символ / и код 0

# Задачи:
# 1) Получить аргумент - имя файла
# 2) если имя голое и не указан путь, то выяснить текущий путь, где запущен скрипт
# 3) Получить список файлов по указанному пути

import os
import sys


def getPath():
    return os.path.dirname(os.path.abspath(__file__));

def renameFile(fullFileName, flags):
    # check, if the file is there
    if (os.path.exists(fullFileName) == True):
        _file_path = os.path.dirname(fullFileName);
        if (len(_file_path) > 1): _file_path = _file_path + '/';
        _file_name = os.path.basename(fullFileName)
        # check if file has 'gbr' extention
        if (os.path.splitext(fullFileName)[1] == ".gbr"):
            _file_parts_minus = _file_name.split('-');
            # check if file name has '-' separator
            if (len(_file_parts_minus) > 1):
                _rename_list = {
                    "B.Cu.gbr": "bot",
                    "B.Mask.gbr": "smb",
                    "B.SilkS.gbr": "ssb",
                    "B.Paste.gbr": "spb",
                    "B.Fab.gbr": "ffb",
                    "Edge.Cuts.gbr": "brd",
                    "F.Cu.gbr": "top",
                    "F.Mask.gbr": "smt",
                    "F.SilkS.gbr": "sst",
                    "F.Paste.gbr": "spt",
                    "F.Fab.gbr": "fab",
                };
                _gerber_name = _file_parts_minus[-2];
                _gerber_extention = _file_parts_minus[-1];
                if (_gerber_extention in _rename_list):
                    _message = "    File " + _file_name;
                    _rename_extention = _rename_list[_gerber_extention];
                    _rename_to_file_name = _gerber_name + '.' + _rename_extention;
                    _message = _message + "\t --> "  + _file_path + _rename_to_file_name;
                        #if (flags == 1):
                        #os.rename(fullFileName,
                    print(_message);
                    return 1;
    else:
        print("File " + fullFileName + "is not exist.");
    return 0;

# ----------------------------------------------------------------------------------------
# Вот тут начало

# переменные
param_path_separator = "/"
param_raw = ""
param_path = ""
param_file = ""
param_file_name_only = ""
param_file_extention = ""
param_project_file_name = ""

# проверяем, сколько параметров дано при вызове
# нам нужен только один параметр: имя файла
if len(sys.argv) > 1:
    param_raw = sys.argv[1];
else:
    print("Error. This program needs a file name as a parameter.")
    sys.exit();

# проверка наличия файла-параметра
if os.path.exists(param_raw) != True:
    print("Error. File does not exist:", param_raw);
    sys.exit();

# выделим имя файла из параметра
param_file = os.path.basename(param_raw)

# выделим только имя файла
param_file_name_only = os.path.splitext(param_file)[0]

# выделим расширение из имени файла
param_file_extention = os.path.splitext(param_file)[1]

# выделим только имя до первого минуса справа
param_project_file_name = param_file_name_only.split('-')[-2]

# проверка расширения файла
if param_file_extention != ".gbr":
    print("Error. This program needs a file name *.gbr as a parameter.")
    sys.exit();

# выделим путь из имени файла-параметра
param_path = os.path.dirname(param_raw)

# если путь пустой, то указываем текущую папку
if (param_path == ''): param_path = getPath();  # param_path = '.';

#print("-----------------------------------------------")
#print("Param raw:", param_raw)
#print("Param file:", param_file)
#print("Param file only:", param_file_name_only)
#print("Param file extention:", param_file_extention)
#print("Param project file name:", param_project_file_name)
#print("Param path:", param_path)
#print("-----------------------------------------------")
#
##print("Current Path:", getPath())
##print("Current working directory:", os.getcwd())
#
#print(os.listdir(param_path))


print("Name:", param_file);
print("Path:", param_path);

fileCnt = 0;
for name in os.listdir(param_path):
    if (renameFile(name, 0) == 1): fileCnt = fileCnt + 1;
print("Total files processed:", fileCnt);

wait = input("FINISHED. PRESS ENTER TO CONTINUE\n");





