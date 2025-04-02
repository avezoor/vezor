import os

def info(f, d, m):
    _f_out = 4
    _d_out = 1
    print(f"Total files: {f + _f_out}")
    print(f"Total folders: {d - _d_out}")
    print(f"Total modules: {m}")

def __count_fdm(dir):
    _f = 0
    _d = 0
    _init = 0

    for root, dirs, files in os.walk(dir):
        _f += len(files)
        
        if files or dirs:
            _d += 1
        
        _init += files.count('__init__.py')

    _m = _f - _init
    return _f, _d, _m

dir_path = os.path.join(os.getcwd(), '')
f, d, m = __count_fdm(dir_path)
info(f, d, m)
