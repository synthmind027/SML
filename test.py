from sml_core import sml_core
import sml

a = sml_core()
a.get('a.b')
a.set('a.b.c','Hello, world!')
print(a.get('a.b.c'))
