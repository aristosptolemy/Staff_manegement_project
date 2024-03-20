
config_path = 'staff_manegement_app/config/'
path = [f'{config_path}GUI_config.txt',f'{config_path}List_config.txt']


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