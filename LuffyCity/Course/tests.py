from django.test import TestCase

# Create your tests here.
import redis

conn = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

conn.set('n1', 'v1')
conn.hset('n2', 'k2', 'v2')
conn.hmset('n3', {'k3': 'v3', 'k4': 'v4'})
print(conn.get('n1'))
print(conn.hget('n2', 'k2'))
print(conn.hgetall('n3'))
