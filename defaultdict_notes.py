from collections import defaultdict

foobar = defaultdict(int)

# initially key 1 doesn't exist
assert 1 not in foobar

print foobar

# looking up this absent key gives the default value of 0, but an
# unintentional side effect occurs...
assert foobar[1] == 0

print foobar

# ... the key now exists despite not explicitly adding it
assert 1 in foobar

# prevent this from happening
baz = dict(foobar)

# assert KeyError
try:
    print baz[0]
except KeyError:
    pass
else:
    assert False

foobar[0] = 0

# test for existence of key
assert 0 in foobar, "this won't be printed: key 0 doesn't exist"

# test for truth value
assert not foobar[0], "this won't be printed: key 0's value is 0"


