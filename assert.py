# These two work the same with different syntax
a = 4
if not (a > 5):
    raise AssertionError("a is too small, get bigger a")

b = 6
assert b < 5, "b is too big, get smaller b"
