people= {
		'alice':{'phone': '2434',
			'addr': 'foo drive 34'
			},
		'beth':{'phone': '3333',
			'addr': 'baz stree 22'
			}
		}

labels = {'phone':'phone number',
	  'addr': 'address'

		}

name = input('name:')

request = input('phone number (p) or addrss (a)')

if request == 'p' :
	key = 'phone'
if request == 'a':
	key = 'addr'

if name in people:
	print ("%s 's %s is %s" %(name, labels[key], people[name][key]))
