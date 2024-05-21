
config_path = 'config/'
path = [f'{config_path}GUI_config.txt',f'{config_path}List_config.txt',f'{config_path}Working_print_config.txt']


def load_GUI_file():
    GUI_lists = {}
    with open(path[0], 'r', encoding='utf-8') as file:
        for line in file:
            # コメント行または空行を無視
            if not line.strip() or line.strip().startswith('#'):
                continue
            
            # キーと値を分割し、両方の不要な空白を削除
            parts = line.strip().split('=')
            if len(parts) == 2:
                key, value = parts[0].strip(), parts[1].strip()
            else:
                key = parts[0].strip()
                value = ''  # デフォルト値を設定
            
            GUI_lists[key] = value
    #print(GUI_lists)
    return GUI_lists

def load_List_file():
    
    select_lists = {}
    with open(path[1], 'r', encoding='utf-8') as file:
        for line in file:
            # コメント行または空行を無視する
            if line.strip().startswith('#') or not line.strip():
                continue
            
            # データ行が正しい形式であることを確認
            parts = line.strip().split(':')

            list_name, list_elements = parts
            select_lists[list_name] = list_elements.split(',')

    #print(f'load_config.txt output test list {select_lists}')#テスト出力
    return select_lists


def Load_Working_config():
    select_cell = {}
    with open(path[2], 'r', encoding='utf-8') as file:
        for line in file:
            # コメント行または空行を無視する
            if line.strip().startswith('#') or not line.strip():
                continue
            
            # データ行が正しい形式であることを確認
            parts = line.strip().split(':', 1)  # ここで最大分割数を1に設定

            if len(parts) != 2:
                print(f"不正な形式の行が見つかりました: {line}")
                continue  # 形式が正しくない行は無視する

            list_name, list_elements = parts
            select_cell[list_name] = list_elements.split(',')

    return select_cell
