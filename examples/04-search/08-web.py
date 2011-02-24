import os, sys; sys.path.append(os.path.join("..", "..", ".."))

from pattern.web    import Yahoo, plaintext
from pattern.en     import Sentence, parse
from pattern.search import Pattern
from pattern.table  import Table, pprint

# "X IS MORE IMPORTANT THAN Y"
# Here is a rough example of how to build a web miner.
# It mines comparative statements from Yahoo! and stores the results in a table,
# which can be saved as a text file for further processing later on.

# Pattern matching also works with Sentence objects from the MBSP module.
# MBSP's parser is much more robust (but also slower).
#from MBSP import Sentence, parse

q = '"more important than"'          # Yahoo search query
p = "NP (VP) more important than NP" # Search pattern.
p = Pattern.fromstring(p)
t = Table()

engine = Yahoo(license=None)
for i in range(1): # max=10
    for result in engine.search(q, start=i+1, count=100, cached=True):
        s = result.description
        s = plaintext(s)
        s = Sentence(parse(s))
        for m in p.search(s):
            a = m.constituents(constraint=0)[-1] # Left NP.
            b = m.constituents(constraint=5)[ 0] # Right NP.
            t.append((
                a.string.lower(), 
                b.string.lower()))

pprint(t)

print
print len(t), "results."