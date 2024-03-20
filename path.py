from pathlib import Path

def default_path():
    #print(Path(__file__).resolve().parent)
    parent_path = Path(__file__).resolve().parent
    return parent_path
    
