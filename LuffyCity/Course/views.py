from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from .serializers import CategorySerializer, CourseSerializer, CourseDetailSerializer, CourseChapterSerializer, \
    CourseCommentSerializer, QuestionSerializer
from utils.base_response import BaseResponse


# Create your views here.

class CategoryView(APIView):
    def get(self, request):
        # 通过ORM操作获取所分类的数据
        queryset = models.Category.objects.all()
        # 利用序列化器序列化我们的数据
        ser_obj = CategorySerializer(queryset, many=True)
        # 返回
        return Response(ser_obj.data)


class CourseView(APIView):
    def get(self, request):
        # 获取过滤条件中的分类ID
        category_id = int(request.query_params.get('categoryId', 0))
        # 根据分类获取课程
        if category_id == 0:
            queryset = models.Course.objects.all().order_by('order')
        else:
            queryset = models.Course.objects.filter(category_id=category_id).all().order_by('order')
        # 序列化课程数据
        ser_obj = CourseSerializer(queryset, many=True)
        # 返回
        return Response(ser_obj.data)


class CourseDetailView(APIView):
    def get(self, request, pk):
        # 根据课程pk获取到课程详情
        course_detail_obj = models.CourseDetail.objects.filter(course__id=pk).first()
        if not course_detail_obj:
            return Response({'code': 1001, 'msg': '你查询的课程详情不存在'})
        # 序列化课程详情
        ser_obj = CourseDetailSerializer(course_detail_obj)
        # 返回
        return Response(ser_obj.data)


class CourseChapterView(APIView):
    def get(self, request, pk):
        queryset = models.CourseChapter.objects.filter(course_id=pk).all().order_by('chapter')
        ser_obj = CourseChapterSerializer(queryset, many=True)
        return Response(ser_obj.data)


class CourseCommentView(APIView):
    def get(self, request, pk):
        # 通过课程id找到课程所有的评论
        queryset = models.Course.objects.filter(id=pk).first().course_comments.all()
        # 序列化
        ser_obj = CourseCommentSerializer(queryset, many=True)
        # 返回
        return Response(ser_obj.data)


class QuestionView(APIView):
    def get(self, request, pk):
        queryset = models.Course.objects.filter(id=pk).first().often_ask_questions.all()
        ser_obj = QuestionSerializer(queryset, Many=True)
        return Response(ser_obj.data)
