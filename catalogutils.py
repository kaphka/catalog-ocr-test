""" provides helper functions to organize directories and files for ocr"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *
from os.path import join, split, splitext, commonprefix, isdir
from os import makedirs, listdir
from glob import glob
import subprocess
import logging

# read initial config file
#logging.config.fileConfig('logging.conf')

def remove_ext(name):
    "drop everything after a dot"
    return name[:name.index('.')]

def transform(base, target_base, pattern, id_filter=None, ext=None):
    "create pairs of source file names and target file names"
    files = glob(join(base, pattern))
    pairs = []
    logger = logging.getLogger(__name__)
    logger.info('source files: {}'.format(join(base, pattern)))
    for fname in files:
        prefix = commonprefix([fname, base])
        target = join(target_base, fname[len(prefix):])
        if ext:
            filename = remove_ext(split(target)[1]) + ext
        else:
            filename = split(target)[1]
        targetdir = split(target)[0]
        target = join(targetdir, filename)
        if id_filter and not split(split(target)[0])[1] in id_filter:
            continue
        pairs.append((fname, target))
    return pairs

def process(pairs, cmd='echo {} to {}', execute=False):
    "process files"
    logger = logging.getLogger(__name__)
    logger.info('executing command {} on {} pairs'.format(cmd, len(pairs)))
    for source, target in pairs:
        print(cmd.format(source, target))
        if execute:
            targetdir = split(target)[0]
            if not isdir(targetdir):
                makedirs(targetdir)
                print("create dir ", targetdir)
            # p = ['tesseract', f, target, '-l deu -psm 7']
            subprocess.check_output(cmd.format(source, target).split(' '))

def result_dir_status(directory):
    "health check a directory"
    print("Status von {}: ".format(directory))

