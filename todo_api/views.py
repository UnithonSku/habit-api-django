import datetime

from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, \
    DestroyModelMixin, UpdateModelMixin
from rest_framework.response import Response

from user_api.models import UserModel
from todo_api.models import TodoModel
from todo_api.serializers import TodoSerializer, TodoListRequestSerializer, \
    TodoCreateSerializer, TodoCreateRequestSerializer, TodoUpdateRequestSerializer


class TodoView(ListModelMixin, GenericAPIView):
    def __str__(self):
        return 'TODO read view. Allowed Method : POST'

    serializer_class = TodoListRequestSerializer

    def list(self, request, *args, **kwargs):
        if 'user' not in kwargs:
            return Response({'error': 'User must be provided!'}, status=status.HTTP_400_BAD_REQUEST)

        queryset = self.filter_queryset(self.get_queryset())
        todo_lists = [self.get_serializer(query).data for query in queryset]
        return Response({'user': kwargs['user'], 'todos': todo_lists})

    def post(self, request):
        user = get_object_or_404(UserModel, id=request.data['user'])
        month = request.data['month']

        self.queryset = TodoModel.objects.filter(user=user).filter(
            date__month=month).filter(date__lte=datetime.date.today())

        self.serializer_class = TodoSerializer
        return self.list(request, user=user.id)


class TodoCreateView(CreateModelMixin, GenericAPIView):
    def __str__(self):
        return 'TODO create view. Allowed Method : POST'

    serializer_class = TodoCreateRequestSerializer

    def create(self, request, *args, **kwargs):
        if 'end_date' not in kwargs:
            return Response({'error': 'End date must be provided!'}, status=status.HTTP_400_BAD_REQUEST)

        start_date = datetime.date.today()
        current_date = start_date
        while current_date <= kwargs['end_date']:
            data = {
                'user': request.data['user'],
                'title': request.data['todo'],
                'date': current_date,
                'order': request.data['order']
            }
            new_todo_serializer = self.get_serializer(data=data)
            new_todo_serializer.is_valid(raise_exception=True)
            self.perform_create(new_todo_serializer)

            current_date += datetime.timedelta(days=1)

        result = {
            'user': request.data['user'],
            'title': request.data['todo'],
            'start_date': start_date,
            'end_date': kwargs['end_date'],
            'order': request.data['order']
        }
        self.serializer_class = TodoCreateSerializer
        result_serializer = self.get_serializer(data=result)
        result_serializer.is_valid(raise_exception=True)
        return Response(result_serializer.data, status=status.HTTP_201_CREATED)

    def post(self, request):
        end_year, end_month, end_day = request.data['until'].values()
        end_date = datetime.date(end_year, end_month, end_day)

        self.serializer_class = TodoSerializer
        return self.create(request, end_date=end_date)


class TodoUpdateView(UpdateModelMixin, GenericAPIView):
    def __str__(self):
        return 'TODO update view. Allowed Method : POST'

    serializer_class = TodoUpdateRequestSerializer

    def update(self, request, *args, **kwargs):
        if 'user' not in kwargs:
            return Response({'error': 'User must be provided!'}, status=status.HTTP_400_BAD_REQUEST)

        if 'title' in request.data['update']:
            self.get_queryset().update(title=request.data['update']['title'])
        if 'done' in request.data['update']:
            self.get_queryset().update(done=request.data['update']['done'])

        return Response(request.data)

    def post(self, request):
        user = get_object_or_404(UserModel, id=request.data['user'])
        self.queryset = TodoModel.objects.filter(user=user).filter(
            title=request.data['todo']).filter(date=datetime.date.today())

        return self.update(request, user=user)


class TodoDeleteView(DestroyModelMixin, GenericAPIView):
    def __str__(self):
        return 'TODO delete view. Allowed Method : POST'

    serializer_class = TodoSerializer

    def destroy(self, request, *args, **kwargs):
        if 'user' not in kwargs:
            return Response({'error': 'User must be provided!'}, status=status.HTTP_400_BAD_REQUEST)

        model = get_object_or_404(self.get_queryset())
        response = {
            'user': kwargs['user'].id,
            'deleted': self.get_serializer(model).data
        }

        model.delete()
        return Response(response, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        user = get_object_or_404(UserModel, id=request.data['user'])

        try:
            self.queryset = TodoModel.objects.filter(user=user).filter(
                title=request.data['title']).get(date=datetime.date.today())
        except TodoModel.DoesNotExist:
            raise Http404('Provided todo model does not exist.')

        return self.destroy(request, user=user)
