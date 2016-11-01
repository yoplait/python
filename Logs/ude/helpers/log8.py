from re import compile, search
from sys import exit
from time import strptime
from datetime import datetime, timedelta, tzinfo

#change this variable to point to the location of the apache access log file 
LOG_FILE_LOCATION = 'C:\code\udemy\log1.txt'

LINES_PROCESSED = 0

log_entry_parts = [

    r'(?P<ext_log>[a-zA-Z]+ [ ]?[0-9]+ [0-9]+:[0-9]+:[0-9]+ domU\S+ logger:)',   # external access log output
    r'(?P<client_ip>\S+)',                                                   # remote host %h
    r'(?P<server_ip>\S+)',                                                   # local ip %A
    r'\[(?P<request_time>.+)\]',                                             # request time %t
    r'"(?P<raw_request>.+)"',                                                # request "%r"
    r'(?P<status_code>[0-9]+)',                                              # status %>s
    r'(?P<response_size>\S+)',                                               # size %b (careful, can be '-')
    r'(?P<response_time>[0-9]+)',                                            # response time %D
    r'"(?P<referer>.*)"',                                                    # referer "%{Referer}i"
    r'"(?P<user_agent>.*)"',                                                 # user agent "%{User-agent}i"
]

raw_request_parts = [r'(?P<method>GET|POST)', r'(?P<request_uri>\S+)', r'(?P<protocol>\S+)']

valid_url_patterns = [
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/topics',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/articles',
                        #r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/summary',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/images',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/videos',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/tweets',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/sources',
                        r'^/topic/(?P<guid>[a-zA-Z0-9_-]+)/stories',
                        r'^/topics',
                        r'^/topics/related',
                        r'^/source/(?P<guid>[a-zA-Z0-9_-]+)',
                        r'^/source/(?P<guid>[a-zA-Z0-9_-]+)/topics',
                        r'^/source/(?P<guid>[a-zA-Z0-9_-]+)/articles',
                        r'^/sources',
                        r'^/article/(?P<guid>[a-zA-Z0-9_-]+)',
                        r'^/article/(?P<guid>[a-zA-Z0-9_-]+)/articles',
                        r'^/article/(?P<guid>[a-zA-Z0-9_-]+)/topics',
                        r'^/article/(?P<guid>[a-zA-Z0-9_-]+)/images',
                        r'^/articles',
                        r'^/stories',
                        r'^/author/(?P<guid>[a-zA-Z0-9_-]+)',
                        r'^/author/(?P<guid>[a-zA-Z0-9_-]+)/articles',
                        r'^/author/(?P<guid>[a-zA-Z0-9_-]+)/topics',
                        r'^/authors',
                        r'^/category/(?P<dashed_name>[a-zA-Z0-9_-]+)/articles',
                        r'^/category/(?P<dashed_name>[a-zA-Z0-9_-]+)/topics',
                        r'^/category/(?P<dashed_name>[a-zA-Z0-9_-]+)/images',
                        r'^/category/(?P<dashed_name>[a-zA-Z0-9_-]+)/stories',
                     ]

#Compile the patterns and create the RegEx objects
raw_request_pattern_obj   = compile(r'\s'.join(raw_request_parts))
log_entry_pattern_obj     = compile(r'\s+'.join(log_entry_parts)+r'\s*')
valid_url_pattern_objects = [compile(url_pattern) for url_pattern in valid_url_patterns]

#A hash for mapping raw requests to Platform methods
#REST request resource1/resource2 will be mapped to module.method
request_to_method_map = [
                            {'resource1': 'topic', 'module': 'Topic', 'map': { 'topics': 'Get Related Topics',
                                                                                'articles': 'Get Topic Articles',
                                                                                'summary': 'Summary',
                                                                                'images': 'Get Topic Images',
                                                                                'videos': 'Get Related Videos',
                                                                                'tweets': 'Get Related Tweets',
                                                                                'sources': 'Get Related Sources',
                                                                                'stories': 'Get Topic Stories',
                                                                                '': 'Get Topic',
                                                                              }},
                            {'resource1': 'topics', 'module': 'Topic', 'map': {'related': 'Extract Related Topics', '': 'Search Topics'}},

                             {'resource1': 'article', 'module': 'Article', 'map': {'topics': 'Get Article Topics', 
                                                                                   'articles': 'Get Related Articles', 
                                                                                   'images': 'Get Article Images',
                                                                                   '': 'Get Article'}},

                             {'resource1': 'articles', 'module': 'Article', 'map':  {'': 'Search Articles'}},
                             
                             {'resource1': 'stories', 'module': 'Article', 'map':  {'': 'Search Stories'}},

                             {'resource1': 'source', 'module': 'Source', 'map':  {'topics': 'Get Source Topics', 
                                                                                  'articles': 'Get Source Articles', 
                                                                                  '': 'Get Source'}},

                             {'resource1': 'sources', 'module': 'Source', 'map': {'': 'Search Source'}},

                             {'resource1': 'author', 'module': 'Author', 'map':  {'topics': 'Get Author Topics', 
                                                                                  'articles': 'Get Author Articles', 
                                                                                  '': 'Get Author'}},

                             {'resource1': 'authors', 'module': 'Author', 'map':  {'': 'Search Authors'}},

                             {'resource1': 'category', 'module': 'Category', 'map':  { 'topics': 'Get Category Topics', 
                                                                                       'articles': 'Get Category Articles',
                                                                                       'images': 'Get Category Images',
                                                                                       'stories': 'Get Category Stories',
                                                                                       'sources': 'Get Category Sources'}}
                        ]

class Timezone(tzinfo):

    def __init__(self, name="+0000"):
        self.name = name
        seconds = int(name[:-2])*3600 + int(name[-2:])*60
        self.offset = timedelta(seconds=seconds)

    def utcoffset(self, dt):
        return self.offset

    def dst(self, dt):
        return timedelta(0)

    def tzname(self, dt):
        return self.name

def get_log_contents(log_file_location=LOG_FILE_LOCATION):
    
    try:
        log_file = open(log_file_location, 'r')
    except IOError:
        exit("Log file not found at "+log_file_location)
        
    return log_file.read()

def process_access_log(log_file_location=LOG_FILE_LOCATION):
    #globals()['LINES_PROCESSED'] = 0
    try:
        log_file = open(log_file_location, 'r')
    except IOError:
        exit("Log file not found at "+log_file_location)
    
    results = [process_log_entry(line) for line in log_file if is_valid_log_entry(line) is True]
    results = [result for result in results if result is not None and result['valid'] is True]
    print "Number of valid requests %d" % len(results)
    return results

def is_valid_log_entry(entry):
    return (log_entry_pattern_obj.match(entry) is not None) and True or False

#parse each line from the log file
def process_log_entry(entry):
    
    matches = log_entry_pattern_obj.match(entry)    
    result  = matches.groupdict()
    
    #process the raw request to obtain information
    request = process_raw_request(result['raw_request'])
    
    if request == None:
        #print "Invalid  API call %s " % result['raw_request']
        return
    
    result["status_code"]   = int(result["status_code"])    
    result["response_size"] = (result["response_size"] != "-") and int(result["response_size"]) or 0
    
    #process the request time to adjust for time zone information
    result['request_time'] = process_request_time(result['request_time'])
    
    if request['valid'] == True:
        result['guid']       = request['guid']
        result['parameters'] = request['parameters']
        result['access_key'] = request['access_key']
        resources = request['resources']
        if request['resources'] != None:
            result['resource1'] = resources['resource1']
            result['resource2'] = resources['resource2']
        if request['method']:
            result['module_name'] = request['method']['module']
            result['method_name'] = request['method']['method']
    else:
        result['parameters'] = result['guid'] = result['resource1'] = result['resource2'] = None
    
    result['valid'] = request['valid']
    #globals()['LINES_PROCESSED'] += 1
    #print "Lines processed-> %d" % globals()['LINES_PROCESSED']
    return result

def process_request_time(request_time):

    date_time = strptime(request_time[:-6], "%d/%b/%Y:%H:%M:%S")
    time_zone = Timezone(request_time[-5:])

    time_info = list(date_time[:6]) + [ 0, None ]
    #time_info = list(date_time[:6])
    
    dt = datetime(*time_info) 
    
    #return dt
    return dt -  timedelta(seconds = time_zone.offset.seconds)

def process_raw_request(raw_request_string):

    matches = raw_request_pattern_obj.match(raw_request_string)
    if matches is None: 
        return    
    
    request = matches.groupdict()    
    if is_valid_request_url(request['request_uri']) is False:
        #request['valid'] = False
        #request['guid']  = request['url'] = request['resources']  = None
        return
    
    request['valid']      = True
    request['url']        = get_request_url(request['request_uri'])
    request['parameters'] = get_request_params(request['request_uri'])
    request['guid']       = get_guid(request['request_uri'])
    request['resources']  = get_resources(request['url'])
    request['method']     = map_resources_to_api_method(request['resources'])
    request['access_key'] = get_access_key(request['request_uri'])
    
    return request

def is_valid_request_url(request_string):

    for url_pattern in valid_url_patterns:
        if search(url_pattern+r'\?', request_string): return True

    return False

def get_request_url(request_string):

    try: 
        return request_string.split('?')[0][1:]
    except Exception: 
        return None

def get_request_params(request_string):

    params = {}

    try: 
        parameters = request_string.split('?')[1].split('&')
    except IndexError: 
        return None

    for param in parameters:
        try:
            parts = param.split('=')
            #key   = parts[0]
            #value = parts[1]
            params[parts[0]] = parts[1]
        except IndexError:
            continue

    return params

def get_access_key(request_string):

    try: 

        param_string = request_string.split('?')[1]
        matches      = search(r'access_key=(?P<access_key>[a-zA-Z0-9]+)', param_string)
        access_key   = matches.groupdict()['access_key']

    except (IndexError, KeyError, AttributeError) :
        access_key = 'access_key'

    return access_key

def get_guid(request_string):

    guid = None
    
    for url_pattern_obj in valid_url_pattern_objects:
        matches = url_pattern_obj.match(request_string)

        if matches == None : 
            continue
        else : 
            result = matches.groupdict()
            try : 
                guid = result['guid']
            except KeyError: 
                break
    return guid

def get_resources(url):

    if url == None:
        return

    resources = {}

    #this is a special case, had to hard code it
    if search(r'^topics/related', url):

        resources['resource1'] = 'topics'
        resources['resource2'] = 'related'

    else:
        url_parts = url.split('/')
        resources['resource1'] = url_parts[0]
        try: 
            resources['resource2'] = url_parts[2]
        except IndexError: 
            resources['resource2'] = ''

    return resources

def map_resources_to_api_method(resources):
    api_method_info = {}

    for item in request_to_method_map:
        if item['resource1'] == resources['resource1']:
            api_method_info['module'] = item['module']
            api_method_info['method'] = item['map'][resources['resource2']]
    
    return api_method_info

if __name__ == "__main__":
    process_access_log()