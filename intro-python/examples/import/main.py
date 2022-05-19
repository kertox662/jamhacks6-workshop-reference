import foo

print(foo.foo(5))

import bar

import sub.baz
sub.baz.baz(bar.x)

# or alternatively
# import sub.baz as baz
# baz.baz(bar.x)