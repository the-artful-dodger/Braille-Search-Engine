# -*- coding: utf-8 -*-

import google
from src.parser import *
import translate as t


keyword = 'apple'

res_gen = google.search(keyword, stop=10)

res = []

for site in res_gen:
    if site not in res:
        res.append(site)

print "a"

fo = open("res.html", "wb")
site_html = google.get_page(res[5])
p = Parser()
p.init_parser()
p.feed(site_html)

print p.data_list
fo.write("<meta charset='UTF-8'><html><body>")
for sentence in p.data_list:
    braille_sentence = t.convert(sentence)
    print braille_sentence
    fo.write("<p>")
    fo.write("".join(braille_sentence))
    fo.write("</p>")
#print site_html
fo.write("</body></html>")
fo.close()



print "b"

print res
