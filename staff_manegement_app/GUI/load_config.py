import os
import sys

def get_base_path():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.abspath(os.path.dirname(__file__))

config_path = os.path.join(get_base_path(), 'config')
config_path = 'config'
paths = [
    os.path.join(config_path, 'GUI_config.txt'),
    os.path.join(config_path, 'List_config.txt'),
    os.path.join(config_path, 'Working_print_config.txt')
]


def load_GUI_file():
    GUI_lists = {}
    try:
        with open(paths[0], 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip() or line.strip().startswith('#'):
                    continue
                parts = line.strip().split('=')
                if len(parts) == 2:
                    key, value = parts[0].strip(), parts[1].strip()
                else:
                    key = parts[0].strip()
                    value = ''
                GUI_lists[key] = value
    except FileNotFoundError:
        print(f"Error: The file at {paths[0]} does not exist.")
    return GUI_lists

def load_List_file():
    select_lists = {}
    try:
        with open(paths[1], 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip().startswith('#') or not line.strip():
                    continue
                parts = line.strip().split(':')
                list_name, list_elements = parts
                select_lists[list_name] = list_elements.split(',')
    except FileNotFoundError:
        print(f"Error: The file at {paths[1]} does not exist.")
    return select_lists

def Load_Working_config():
    select_cell = {}
    try:
        with open(paths[2], 'r', encoding='utf-8') as file:
            for line in file:
                if line.strip().startswith('#') or not line.strip():
                    continue
                parts = line.strip().split(':', 1)
                if len(parts) != 2:
                    print(f"不正な形式の行が見つかりました: {line}")
                    continue
                list_name, list_elements = parts
                select_cell[list_name] = list_elements.split(',')
    except FileNotFoundError:
        print(f"Error: The file at {paths[2]} does not exist.")
    return select_cell
