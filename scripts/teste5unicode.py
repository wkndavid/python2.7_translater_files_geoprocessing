# -*- coding: utf-8 -*-
# -*- coding: latin-1 -*-

import codecs as cd 

file = cd.open("teste.txt", encoding='utf-8')

data = file.read()
data = data.upper()

print(data)

# encoding for 2.7