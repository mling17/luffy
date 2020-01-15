# -*- coding:utf-8 -*-
import redis
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from utils.redis_pool import Pool
from Course.models import Account

conn = redis.Redis(connection_pool=Pool)


class LoginAuth(BaseAuthentication):
    def authenticate(self, request):
        # 从请求头中获取前端带来的token
        token = request.META.get('HTTP_AUTHENTICATION', '')
        if not token:
            raise AuthenticationFailed('没有携带token')
        # 去redis中比对token
        user_id = conn.get(str(token))
        if not user_id:
            raise AuthenticationFailed('token已过期')
        user_obj = Account.objects.filter(id=user_id).first()
        return user_id, token
