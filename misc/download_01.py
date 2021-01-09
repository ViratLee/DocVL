import urllib.request
import urllib.parse
url = 'https://www.google.com/'
prod_host = 'thadcplwcm11/logs/wcmapp11/SystemOut_18.05.21_10.50.09.log'
print('download...')
try:
	f = urllib.request.urlopen(url)
	print('read status send ')
	code = r.status_code
	print('status code'+code)
except urllib.request.exceptions.Timeout:
	    # Maybe set up for a retry, or continue in a retry loop
	print('timeout')
except urllib.request.exceptions.TooManyRedirects:
	    # Tell the user their URL was bad and try a different one
	print('too many redirect')
except urllib.request.exceptions.RequestException as e:
    # catastrophic error. bail.
    print(e)
#print(f.read().decode('utf-8'))
#import requests
#r = requests.get('https://github.com/timeline.json')
#code = r.status_code
#print(code)