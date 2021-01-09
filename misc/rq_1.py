import redis
print(redis.__version__) #2.10.6
r = redis.Redis(host='localhost', port=6379, db=0)
r.set('foo', 'bar')
r.get('foo')