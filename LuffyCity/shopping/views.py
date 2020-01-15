from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import redis
import json
from utils.my_auth import LoginAuth
from utils.base_response import BaseResponse
from utils.redis_pool import Pool
from Course import models

# 前端传过来 course_id   price_policy_id
# 把购物车的数据放入redis
"""
{
    SHOPPINGCAR_USERID_COURSEID:{
        'id',
        'title',
        'course_img',
        'price_policy_dict:{
            price_policy_id1:{valid_period,price}
            price_policy_id2:{valid_period,price}
            price_policy_id3:{valid_period,price}
        },
        'default_price_policy_id'
    }
}
"""

SHOPINGCAR_KEY = "SHOPINGCAR_%s_%s"
conn = redis.Redis(connection_pool=Pool)


class ShoppingCarView(APIView):
    authentication_classes = [LoginAuth, ]

    def post(self, request):
        res = BaseResponse()
        # 1. 获取前端传过来的数据以及user_id
        course_id = request.data.get('course_id', '')
        price_policy_id = request.data.get('price_policy_id', '')
        user_id = request.user
        # 2. 校验数据的合法性
        #   2.1 校验课程ID的合法性
        course_obj = models.Course.objects.filter(id=course_id).first()
        if not course_obj:
            res.code = 1040
            res.error = '课程ID不合法'
            return Response(res.dict)
        #   2.2 校验价格策略ID的合法性
        price_policy_queryset = course_obj.price_policy.all()
        price_policy_dict = {}
        for price_policy in price_policy_queryset:
            price_policy_dict[price_policy.id] = {
                "price": price_policy.price,
                "valid_period": price_policy.valid_period,
                "valid_period_display": price_policy.get_valid_period_display()
            }
        # 3. 构建redis的key
        key = SHOPINGCAR_KEY % (user_id, course_id)
        # 4. 构建数据结构
        course_info = {
            'id': course_obj.id,
            'title': course_obj.title,
            'course_img': str(course_obj.course_img),
            'price_policy_dict': json.dumps(price_policy_dict, ensure_ascii=False),
            'default_price_policy_id': price_policy_id
        }
        # 5. 写入redis
        conn.hmset(key, course_info)
        res.data = '加入购物车成功'
        return Response(res.dict)

    def get(self, request):
        res = BaseResponse()
        # 1. 拼接redis的key
        user_id = request.user
        shopping_car_key = SHOPINGCAR_KEY % (user_id, '*')
        # 2. 去redis读取数据
        # 3. 构建前端的数据结构
        all_keys = conn.scan_iter(shopping_car_key)
        ret = []
        for key in all_keys:
            ret.append(conn.hgetall(key))
        res.data = ret
        return Response(res.data)

    def put(self, request):
        # 前端    course_id   price_policy_id
        res = BaseResponse()
        # 1. 获取前端传过来的数据以及user_id
        course_id = request.data.get('course_id', '')
        price_policy_id = request.data.get('price_policy_id', '')
        user_id = request.user
        # 2. redis校验数据的合法性
        #   2.1 course_id是否合法
        key = SHOPINGCAR_KEY % (user_id, course_id)
        if not conn.exists(key):
            res.code = 1043
            res.error = '课程id不合法'
            return Response(res.dict)
        #   2.2 price_policy_id是否合法
        price_policy_dict = json.loads(conn.hget(key, 'price_policy_dict'))
        if str(price_policy_id) not in price_policy_dict:
            res.code = 1044
            res.error = '价格策略不合法'
            return Response(res.dict)
        # 3. 更新redis
        conn.hset(key, 'default_price_policy_id', price_policy_id)
        res.data = '更新成功'
        return Response(res.dict)

    def delete(self, request):
        res = BaseResponse()
        # 1. 获取前端传来的数据
        course_list = request.data.get('course_list', '')
        user_id = request.user
        # 2. 校验course_id是否合法
        for course_id in course_list:
            key = SHOPINGCAR_KEY % (user_id, course_id)
            if not conn.exists(key):
                res.code = 1045
                res.error = '课程ID不合法'
                return Response(res.dict)
            # 3. 删除redis数据
            conn.delete(key)
            print(key)
        res.data = '删除成功'
        return Response(res.dict)


