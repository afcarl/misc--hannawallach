foo = [] # list

for x in range(3):
    foo.append(x * x)

# foo is an iterable -- you can iterate over its items

for y in foo:
    print 'foo', y

bar = [x * x for x in range(3)] # list comprehension -- expression followed by a "for" clause followed by 0 or more "for" or "if" clauses (e.g., [(x, y) for x in range(3) for y in range(3) if x != y]) -- more concise notation

for y in bar:
    print 'bar', y

baz = (x * x for x in range(3)) # generator -- values are generated on the fly, can only read them once

for y in baz:
    print 'baz', y

# won't print anything if used a second time

for y in baz:
    print 'baz', y

def create_generator(): # this function returns a generator

    for x in range(3):
        yield x * x

tmp = create_generator() # tmp is a generator object that contains the code in the body of create_generator() -- even though create_generator() has been called, the code in its body has not yet been run

print tmp

# the code in the body of create_generator() will now be run -- see http://stackoverflow.com/questions/231767/the-python-yield-keyword-explained

for y in tmp:
    print 'tmp', y

# won't print anything if used a second time

for y in tmp:
    print 'tmp', y
