import redis
import uuid
import hashlib
from rest_framework.views import APIView
from rest_framework.response import Response
from utils.base_response import BaseResponse
from utils.redis_pool import Pool
from utils.my_auth import LoginAuth
from .serializers import RegisterSerializer
from Course.models import Account


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        res = BaseResponse()
        # 用序列化器做校验
        ser_obj = RegisterSerializer(data=request.data)
        if ser_obj.is_valid():
            ser_obj.save()
            res.data = ser_obj.data
        else:
            res.code = 1020
            res.error = ser_obj.errors
        return Response(res.dict)


class LoginView(APIView):
    def post(self, request):
        res = BaseResponse()
        username = request.data.get('username', '')
        pwd = request.data.get('password', '')
        pwd_salt = 'luffy_password' + pwd
        pwd = hashlib.md5(pwd_salt.encode()).hexdigest()
        print(pwd)
        user_obj = Account.objects.filter(username=username, pwd=pwd).first()
        if not user_obj:
            res.code = 1030
            res.error = '用户名或密码错误'
        # 用户登陆成功生成一个token写入redis
        # 写入 redis  token:user_id
        conn = redis.Redis(connection_pool=Pool)
        try:
            token = str(uuid.uuid4())
            # conn.set(token, user_obj.id, ex=30)
            conn.set(token, user_obj.id)
            res.data = token
        except Exception as e:
            res.code = 1031
            res.error = '创建令牌失败'
        return Response(res.dict)


class TestView(APIView):
    authentication_classes = [LoginAuth, ]

    def get(self, request):
        return Response('test')
