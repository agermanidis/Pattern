import os, sys; sys.path.append(os.path.join("..", "..", ".."))

from pattern.web import Yahoo, Bing, asynchronous, plaintext
from pattern.web import SEARCH, IMAGE, NEWS

import time

# This example retrieves results from Yahoo based on a given query.
# Yahoo can retrieve up to a 1000 results (10x100) for a query,
# but the service is limited to 5000 requests per day.

# You should obtain your own license key at:
# https://developer.apps.yahoo.com/wsregapp/
# Otherwise you will be sharing the daily limit with all users of this module.
engine = Yahoo(license=None)

# Quote a query to match it exactly:
q = "\"is more important than\""

# When you execute a query, the script will halt until all results are downloaded.
# In applications with an event loop (e.g. a GUI or an interactive animation)
# it is more useful if the app keeps on running while the search is executed in the background.
# This can be achieved with the asynchronous() command.
# It takes any function and the function's arguments and keyword arguments:
request = asynchronous(engine.search, q, start=1, count=100, type=SEARCH, timeout=10)

# This while-loop simulates an application event loop.
# In a real-world example you would have an app.update() or similar
# in which you can check request.done every now and then.
while not request.done:
    time.sleep(0.01)
    print ".",

print
print

# An error occured in engine.search(), raise it.
if request.error:
    raise request.error

# Retrieve the list of search results.
for result in request.value:
    print result.description
    print result.url
    print
    