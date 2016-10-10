import sys
import re
import time


text_file = open("C:/Users/perezju/Documents/ICON/code/python/Logs/access-log", "w")

TotalAmount = 33.3
text_file.write("Purchase Amount: %s" % TotalAmount)


text_file.close()