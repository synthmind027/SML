from sml_core import sml_core
from sml import sml_globals

a = sml_core()
a.get('a.b')
a.set('a.b.c','Hello, world!')
print(a.get('a.b.c'))

func = sml_globals.get('**')
print(func)
print(func(12,2))
