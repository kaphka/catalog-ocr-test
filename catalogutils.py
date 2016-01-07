from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


from os.path import join, split, splitext,commonprefix, isdir
from os import makedirs, listdir
from glob import glob
import subprocess

def remove_ext(name):
    return name[:name.index('.')]

def transform( base, target_base, pattern, id_filter=None, ext=None):
    files = glob(join(base, pattern))
    print(join(base, pattern))
    pairs = []
    for f in files:
        prefix = commonprefix([f, base])
        target = join(target_base, f[len(base):])
        if ext:
            filename = remove_ext(split(target)[1]) + ext
        else:
            filename = split(target)[1]
        targetdir = split(target)[0]
        target = join(targetdir, filename)
        if id_filter and not (split(split(target)[0])[1] in id_filter):
            continue
        pairs.append((f, target))
    return pairs

def process(pairs, p='echo {} to {}', execute=False):
    for f, target in pairs:
        print(p.format(f, target))
        if execute:
            targetdir = split(target)[0]
            if not isdir(targetdir):
                makedirs(targetdir)
                print("create dir ", targetdir)
            # p = ['tesseract', f, target, '-l deu -psm 7']
            subprocess.check_output(p.format(f,target).split(' '))

def result_dir_status(directory):
    print("Status von {}: ".format(directory))

