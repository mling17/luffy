# -*- coding:utf-8 -*-
import redis

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, decode_responses=True, max_connections=10)
conn = redis.Redis(connection_pool=pool)
# 生成一个订阅者对象
pubsub = conn.pubsub()
# 订阅一个消息
pubsub.subscribe('gaoxin')
# 创建一个接收
while True:
    print('working~~~')
    msg = pubsub.parse_response()
    print(msg)
