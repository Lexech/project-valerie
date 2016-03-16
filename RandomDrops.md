http://wiki.python.org/moin/PythonSpeed/PerformanceTips

### String Concatenation ###
Avoid:
```
out = "<html>" + head + prologue + query + tail + "</html>"
```
Instead, use
```
out = "<html>%s%s%s%s</html>" % (head, prologue, query, tail)
```
Even better, for readability (this has nothing to do with efficiency other than yours as a programmer), use dictionary substitution:
```
out = "<html>%(head)s%(prologue)s%(query)s%(tail)s</html>" % locals()
```

### Loops ###
Here's a straightforward example. Instead of looping over a list of words and converting them to upper case:
```
newlist = []
for word in oldlist:
    newlist.append(word.upper())
```
Generator expressions were added to Python in version 2.4. They function more-or-less like list comprehensions or map but avoid the overhead of generating the entire list at once. Instead, they return a generator object which can be iterated over bit-by-bit:
```
newlist = (s.upper() for s in oldlist)
```

### Import Statement Overhead ###
A good way to do lazy imports is:
```
email = None

def parse_email():
    global email
    if email is None:
        import email
```