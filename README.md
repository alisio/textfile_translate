# Overview

`textfile_translate` is a text file translation program. It uses google translator
service as a backend.

# Install:

Put the script in the path, install the required python modules and you're good to go:

```
pip install -r requirements.txt
```

# Usage

Run:
```
textfile_translate.py [-l <LANGUAGE_CODE>] -i <SRC>
```

Options:
    -l    iso639-1 destination language code. Default: pt
    -i    Path to source file, aka, the file to be translated.


Output:

A new file containing the translated text will be created on the same as the original text file. The destination language code will be appended to the end of the new filename, before the extension.

Example:

* Input file: `article.txt`
* Output `article.pt.txt`



# Limitations

All Google Translate service limitations are applied.
Tested using MacOS Monterey running python 3.9

There's no error catching whatsoever. You are welcome to implement it yourself.

References:
* [Googletrans: Free and Unlimited Google translate API for Python](https://py-googletrans.readthedocs.io/en/latest/)
* [ISO 639 Language Codes](http://www.infoterm.info/standardization/iso_639_1_2002.php)


# Author

Antonio Alisio de Meneses Cordeiro - alisio.meneses@gmail.com
