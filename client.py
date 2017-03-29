from pprint import pprint
from pyrpc import Client

client = Client()

method = client.reset
print('method: {}'.format(method))
obs = method()
print('observation:')
pprint(obs)

obs = client.reset()
pprint(obs)
a,b,c,d = client.step(0)
pprint(a)
pprint(b)
pprint(c)
pprint(d)
