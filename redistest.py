# pip install redis
import redis

pool = redis.ConnectionPool(host='172.16.0.44', port=6379, db=0, password='1qazxsw2', decode_responses=True)

r = redis.Redis(connection_pool=pool)

r.set('testpython','测试')

print(r.get('testpython'))

