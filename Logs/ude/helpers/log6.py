import re
from collections import defaultdict, named tuple

format_pat= re.compile( 
    r"(?P<host>[\d\.]+)\s" 
    r"(?P<identity>\S*)\s" 
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s' # [SIC]
    r'"(?P<user_agent>.*?)"\s*' 
)

Access = namedtuple('Access',
    ['host', 'identity', 'user', 'time', 'request',
    'status', 'bytes', 'referer', 'user_agent'] )

def access_iter( source_iter ):
    for log in source_iter:
        for line in (l.rstrip() for l in log):
            match= format_pat.match(line)
            if match:
                yield Access( **match.groupdict() )




def apache2_logrow(s):
    ''' Fast split on Apache2 log lines

    http://httpd.apache.org/docs/trunk/logs.html
    '''
    row = [ ]
    qe = qp = None # quote end character (qe) and quote parts (qp)
    for s in s.replace('\r','').replace('\n','').split(' '):
        if qp:
            qp.append(s)
        elif '' == s: # blanks
            row.append('')
        elif '"' == s[0]: # begin " quote "
            qp = [ s ]
            qe = '"'
        elif '[' == s[0]: # begin [ quote ]
            qp = [ s ]
            qe = ']'
        else:
            row.append(s)

        l = len(s)
        if l and qe == s[-1]: # end quote
            if l == 1 or s[-2] != '\\': # don't end on escaped quotes
                row.append(' '.join(qp)[1:-1].replace('\\'+qe, qe))
                qp = qe = None
    return row


rexp = re.compile('(\d+\.\d+\.\d+\.\d+) - - \[([^\[\]:]+):'
'(\d+:\d+:\d+) -(\d\d\d\d\)] ("[^"]*") '
'(\d+) (-|\d+) ("[^"]*") (".*")\s*\Z')

a = rexp.match(line)
if not a is None:
a.group(1) #IP address
a.group(2) #day/month/year
a.group(3) #time of day
a.group(4) #timezone
a.group(5) #request
a.group(6) #code 200 for success, 404 for not found, etc.
a.group(7) #bytes transferred
a.group(8) #referrer
a.group(9) #browser
else:
#this line did not match.