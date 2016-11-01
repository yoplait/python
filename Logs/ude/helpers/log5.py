import re

# sample line of the log file
log_line = '''127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /apache_pb.gif HTTP/1.0" 200 2326 "http://www.example.com/start.html" "Mozilla/4.08 [en] (Win98; I ;Nav)"'''

# regular expression pattern
pattern = re.compile(r'^([0-9.]+)s([w.-]+)s([w.-]+)s([[^[]]+])s"((?:[^"]|")+)"s(d{3})s(d+|-)s"((?:[^"]|")+)"s"((?:[^"]|")+)"$')

# match
result = pattern.match(log_line)

# print the result
for part in result.groups():
    print(part)



line = '172.16.0.3 - - [25/Sep/2002:14:04:19 +0200] "GET / HTTP/1.1" 401 - "" "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.1) Gecko/20020827"'

regex = '([(\d\.)]+) - - \[(.*?)\] "(.*?)" (\d+) - "(.*?)" "(.*?)"'

print re.match(regex, line).groups()



