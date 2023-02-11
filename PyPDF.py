import pikepdf
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

root = tk.Tk()
root.withdraw()
path = Path(filedialog.askopenfilename())
f_root = path.parent
new_name = '解密后_' + path.stem + path.suffix
with pikepdf.open(path) as f:
    f.save(f_root.joinpath(new_name))
    print('文件转换至{}'.format(f_root))
input("Press Any Key")
