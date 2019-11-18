import ctypes
import string
import os


file_system_dict = {}


def get_drives():
    assert 'nt' == os.name
    drives = []
    buff_size = ctypes.windll.kernel32.GetLogicalDriveStringsW(0,None)
    buff = ctypes.create_string_buffer(buff_size*2)
    ctypes.windll.kernel32.GetLogicalDriveStringsW(buff_size,buff)
    volumes = filter(None, buff.raw.decode('utf-16-le').split(u'\0'))
    for letter in volumes:
        drives.append(letter.replace(":\\", ""))
    return drives


print(get_drives())

def find(file_system_dict=file_system_dict):
    drives = get_drives()

    for drive in drives:
        for root, dirs, files in os.walk(drive + ':\\'):
           for f in files:
            key = os.path.join(root, f).rsplit('\\')[-1]
            file_system_dict.update({key: os.path.join(root, f)})

            for dir in dirs:
                key = os.path.join(root, dir).rsplit('\\')[-1]
                file_system_dict.update({key: os.path.join(root, dir)})

    return file_system_dict


print(find())
