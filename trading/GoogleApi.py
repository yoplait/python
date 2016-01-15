#!/usr/bin/env python
'''
--------------------------------------------------------------------------------
Module Name:    GoogleApi.py
Author:         Juan Carlos Perez
Date:           1/24/2016
Description:    This module accesses stock quote data from Google's financial
                API.
--------------------------------------------------------------------------------
'''

# Imports
import urllib2
from dateutil import parser

#-------------------------------------------------------------------------------
#                               GoogleQuotes Class
#-------------------------------------------------------------------------------
class GoogleQuotes(object):

    kBaseURI = 'http://www.google.com/finance/info?infotype=infoquoteall&q=%s'

    #---------------------------------------------------------------------------
    #                               __init__
    #---------------------------------------------------------------------------
    def __init__(self):

        return

    #---------------------------------------------------------------------------
    #                               GetQuote
    #---------------------------------------------------------------------------
    def GetQuote(self, symbols=['AAPL','GOOG']):
        '''This method gets a real-time stock quote from the nasdaq website.'''
    
        # Make sure the quoteList is a list
        if type(symbols) != type([]):
            symbols = [symbols]
    
        # Create a string with the list of symbols
        symbolList = ','.join(symbols)
    
        # Create the full query
        url = self.kBaseURI % symbolList
    
        # Make sure the URL is formatted correctly
        self.url = urllib2.quote(url, safe="%/:=&?~#+!$,;'@()*[]")
        
        # Retrieve the data
        urlFile = urllib2.urlopen(self.url)
        self.urlData = urlFile.read() 
        urlFile.close()
        
        # Parse the returned data
        quotes = self._ParseData(self.urlData)

        return quotes


    #---------------------------------------------------------------------------
    #                             _ParseData
    #---------------------------------------------------------------------------
    def _ParseData(self, data):
        '''
        This is the set of data returned by Google.
        'el': '448.37',             - After. hours last quote (float)
        'eo': '',                   - Exchange Open (0 or 1)
        'eccol': 'chr',             - (unknown) (chars)
        'hi52': '705.07',           - 52 weeks high (float)
        'ec': '-2.13',              - After hours last change from close (float)
        'vo': '52.17M',             - Volume (float with multiplier)
        'eps': '44.10',             - Earnings per share (float)
        'beta': '1.21',             - Beta (float)
        'hi': '465.73',             - Price high (float)
        'inst_own': '67%',          - Institutional Ownership (float, percentage)
        'ecp': '-0.47',             - After hours last chage perc. from close (float)
        'yld': '2.35',              - Dividend Yield (float)
        'cp': '-12.35',             - Change perc. while open (float)
        'fwpe': '',                 - Forward PE ratio (float)
        'id': '22144',              - Company id (identifying number, int)
        'l_cur': '450.50',          - Last value at close
        'avvo': '19.72M',           - Average volume (float with multiplier)
        'c': '-63.51',              - Amount of change while open (float)
        'e': 'NASDAQ',              - Exchange (string)
        'name': 'Apple Inc.',       - Company Name (string)
        'mc': '423.04B',            - Market cap. (float with multiplier)
        'ltt': '4:00PM EST',        - Last trade time
        'lo': '450.25',             - Price low (float)
        'lo52': '443.14',           - 52 weeks low (float)
        'l': '450.50',              - Last value while open (float)
        'shares': '939.04M',        - Shares Outstanding (float with multiplier)
        'delay': '',                - (unknown)
        's': '2',                   - (unknown)
        'lt': 'Jan 24, 4:00PM EST', - Last value date/time
        't': 'AAPL',                - Ticker Symbol (string)
        'el_cur': '448.37',         - After hours current quote? (float)
        'pe': '10.22',              - P/E Ratio
        'div': '2.65',              - Dividend (float) 
        'ccol': 'chr',              - (unknown) (chars)
        'type': 'Company',          - Type (string)
        'elt': 'Jan 24, 7:59PM EST',- After hours last quote time 
        'op': '460.00'              - Open price (float)
        '''

        # Replace the // with an array name
        data = data.replace('//', 'rawQuotes = ')

        # Run the string as Python code
        exec(data)

        # Create a list to store the quotes
        quotes = []

        # Loop over all stock values
        for rawQuote in rawQuotes:
            quote = {}
            
            if rawQuote.has_key('lt') and len(rawQuote['lt']) > 0:
                quote['timestamp'] = parser.parse(rawQuote['lt'])

            quote['symbol'] = self._convert(rawQuote, 't', str)
            quote['price'] = self._convert(rawQuote, 'l', float)
            quote['exchangeOpen'] = self._convert(rawQuote, 'eo', bool)
            quote['52wkHigh'] = self._convert(rawQuote, 'hi52', float)
            quote['52wkLow'] = self._convert(rawQuote, 'lo52', float)
            quote['eps'] = self._convert(rawQuote, 'eps', float)
            quote['beta'] = self._convert(rawQuote, 'beta', float)
            quote['high'] = self._convert(rawQuote, 'hi', float)
            quote['low'] = self._convert(rawQuote, 'lo', float)
            quote['institutionalOwnership'] = self._convert(rawQuote, 'inst_own', str)
            quote['dividendYield'] = self._convert(rawQuote, 'yld', float)
            quote['percentChange'] = self._convert(rawQuote, 'cp', float)
            quote['lastClose'] = self._convert(rawQuote, 'l_cur', float)
            quote['change'] = self._convert(rawQuote, 'c', float)
            quote['exchange'] = self._convert(rawQuote, 'e', str)
            quote['name'] = self._convert(rawQuote, 'name', str)
            quote['pe'] = self._convert(rawQuote, 'pe', float)
            quote['dividend'] = self._convert(rawQuote, 'div', float)
            quote['type'] = self._convert(rawQuote, 'type', str)
            quote['open'] = self._convert(rawQuote, 'op', float)

            # Add to the list of quotes
            quotes.append(quote)
        
        return quotes

    
    #---------------------------------------------------------------------------
    #                              _convert
    #---------------------------------------------------------------------------    
    def _convert(self, quoteDict={}, key='', dtype=float):
        ''' Helper method to convert dictionary values to a datatype. '''
        if (quoteDict is not None) and \
           (type(quoteDict) == type({})) and \
           (quoteDict.has_key(key)):
            stringVal = quoteDict[key]
            # Get the value
            try:
                val = dtype(stringVal)
            except Exception as ex:
                # You might want to do some special error handling here
                val = None
        else:
            # There is a problem, tshe value should be None
            val = None
        return val


#-------------------------------------------------------------------------------
#                                    main
#-------------------------------------------------------------------------------
def main():

    # Create a GoogleQuote object
    gq = GoogleQuotes()

    # Get the quotes
    quotes = gq.GetQuote(['CY', 'AAPL', 'GOOG', 'YHOO', 'SBUX'])

    # Display the quotes
    print quotes

    return

if __name__ == '__main__':
    main()

# End of File
