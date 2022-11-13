# TODO решить с помощью list comprehension и распечатать его
from pprint import pprint

dict_ = [{'bin': bin(d), 'dec': d, 'hex': hex(d),
          'oct': oct(d)} for d in range(16)]
pprint(dict_)
