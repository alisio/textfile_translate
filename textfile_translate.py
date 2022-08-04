#!/usr/bin/env python
# coding: utf-8

"""
textfile_translate is a text file translation program. It uses google translator
service as a backend.

Usage: textfile_translate.py <SRC>

arguments:
    Path to source file, aka, the file to be translated.

Install:
    Just put the script in the path and install the required python modules:
        * `googletrans==3.1.0a0`

Limitations:
    All Google Translate service limitations are applied.
    Tested using MacOS Monterey running python 3.9


"""

__author__ = "Alisio Meneses"
__credits__ = ["tixxit"]
__license__ = "GPL"
__version__ = "0.9"
__maintainer__ = "Alisio Meneses"
__email__ = "alisio.meneses@gmail.com"

# Tested with googletrans==3.1.0a0

from googletrans import Translator
import math
import os
import sys
import getopt

# Const

dest_lang = "pt"
text_block_size = 5000
path = ""

argv = sys.argv[1:]

try:
    opts, args = getopt.getopt(argv, "l:i:")

except:
    print("Error")

for opt, arg in opts:
    if opt in ['-l']:
        dest_lang = arg
    if opt in ['-s']:
        text_block_size = arg
    elif opt in ['-i']:
        path = arg
        path_abs = os.path.abspath(path)
        filename = os.path.basename(path_abs)
        directory = os.path.dirname(path_abs)
        filename_no_ext = os.path.splitext(filename)[0]
        filename_ext = os.path.splitext(filename)[-1]


# Read Text File
f = open(path)
text = f.read()
f.close()

# Split text into blocks because google
# shoutout to stackoverflow member tixxit for this split function
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

# Split text into blocks of up to the number of characters set in text_block_size
text_blocks = list(split(text,math.ceil(len(text)/text_block_size)))
translated_text_blocks = []

#
translator = Translator()
for index, text_block in enumerate(text_blocks):
    src_lang = translator.detect(text_block)
    print(f'Translating text block {str(index)} (size {len(text_block)} characters) from {src_lang} to {dest_lang}')
    resultado = translator.translate(text_block, src_lang=src_lang.lang, dest=dest_lang)
    translated_text_blocks.append(resultado.text)


path_to_translated_file = directory + "/" + filename_no_ext + '.' + dest_lang + filename_ext

with open(path_to_translated_file, 'w+') as arquivo_final:
    print("Joining text blocks")
    arquivo_final.write("".join(translated_text_blocks))

print(f'Text file translated to {dest_lang}. New file created: {path_to_translated_file}')
