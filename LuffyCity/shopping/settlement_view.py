# -*- coding:utf-8 -*-
import redis
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.redis_pool import Pool
from utils.base_response import BaseResponse
from utils.my_auth import LoginAuth
from .views import SHOPINGCAR_KEY

conn = redis.Redis(connection_pool=Pool)


class SettlementView(APIView):
    authentication_classes = [LoginAuth, ]
    """
    前端传过来的数据 course_list
    redis={
        settlement_userid_courseid:{
        课程id,
        title,
        course_img,
        valid_period_display,
        price,
        course_coupon_dict:{
                coupon_id:{优惠券信息}
                coupon_id2:{优惠券信息}
                coupon_id3:{优惠券信息}
           }
           # 默认不给选, 这个字段只有更新的时候才添加
           default_coupon_id:1
        }
        global_coupon_userid:{
            coupon_id3:{优惠券信息}
            default_global_coupon_id:1
        }
    }
    """

    def post(self, request, pk):
        res = BaseResponse()
        # 获取前端传过来的数据和user_id
        course_list = request.data.get('course_list', '')
        user_id = request.user
        # 校验数据合法性
        for course_id in course_list:
            # 2.1 判断course_id是否在购物车中
            shopping_car_key = SHOPINGCAR_KEY % (user_id, course_id)
            if not conn.exists(shopping_car_key):
                res.code = 1050
                res.error = '课程id不合法'
                return Response(res.dict)
        # 构建redis数据结构
        # 3.1 获取用户该课程的所有合法优惠券
        # 写入redis
