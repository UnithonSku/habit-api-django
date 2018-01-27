import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user_api.models import UserModel
from todo_api.models import TodoModel
from todo_api.serializers import TodoSerializer


class TodoView(APIView):
    def __str__(self):
        return 'TODO read view. Allowed Method : POST'

    def post(self, request):
        try:
            user = UserModel.objects.get(id=request.data['user'])
        except UserModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            todos = TodoModel.objects.filter(user=user).filter(
                date__month=request.data['month']).filter(date__lte=datetime.date.today()).order_by('date')
            response = {
                'user': user.id,
                'todos': list()
            }

            for todo in todos:
                found_todo = TodoSerializer(todo)
                response['todos'].append(found_todo.data)

            return Response(response, status=status.HTTP_200_OK)
        except KeyError:
            return Response({
                'error': 'Month must be specified'
            }, status=status.HTTP_400_BAD_REQUEST)


class TodoCreateView(APIView):
    def __str__(self):
        return 'TODO create view. Allowed Method : POST'

    def post(self, request):
        try:
            user = UserModel.objects.get(id=request.data['user'])
        except UserModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)

        if 'until' not in request.data:
            new_todo = TodoModel(user=user, title=request.data['todo'], order=request.data['order'])
            new_todo.save()

            new_todo_serializer = TodoSerializer(new_todo)

            response = {
                'user': user.id,
                'created': new_todo_serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            year, month, day = request.data['until'].values()
            date = datetime.date.today()
            until = datetime.date(year, month, day)

            response = {
                'user': user.id,
                'created': list()
            }

            while date <= until:
                new_todo = TodoModel(
                    user=user, title=request.data['todo'], date=date, order=request.data['order'])
                new_todo.save()
                new_todo_serializer = TodoSerializer(new_todo)
                response['created'].append(new_todo_serializer.data)
                date += datetime.timedelta(days=1)

            return Response(response, status=status.HTTP_201_CREATED)


class TodoUpdateView(APIView):
    def __str__(self):
        return 'TODO update view. Allowed Method : POST'

    def post(self, request):
        token = request.data['user']
        todo_title = request.data['todo']

        try:
            user = UserModel.objects.get(id=token)
        except UserModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
        user_id = user.id

        try:
            todo_model = TodoModel.objects.get(
                title=todo_title, user=user_id, date=datetime.date.today())
        except TodoModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'Todo does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)

        response = {
            'user': user_id,
            'updated': dict()
        }

        try:
            updated_title = request.data['update']['title']
            todo_model.title = updated_title
            response['updated']['title'] = updated_title
        except KeyError:
            pass

        try:
            updated_done = request.data['update']['done']
            todo_model.done = updated_done
            response['updated']['done'] = updated_done
        except KeyError:
            pass

        todo_model.save()
        return Response(response, status=status.HTTP_200_OK)


class TodoDeleteView(APIView):
    def __str__(self):
        return 'TODO delete view. Allowed Method : POST'

    def post(self, request):
        token = request.data['user']
        todo_title = request.data['todo']

        try:
            user = UserModel.objects.get(id=token)
        except UserModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'User does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)
        user_id = user.id

        try:
            todo_model = TodoModel.objects.get(
                title=todo_title, user=user_id, date=datetime.date.today())
        except TodoModel.DoesNotExist:
            return Response({
                'status': 400,
                'error': 'Todo does not exist'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(todo_model)
        response = {
            'user': user_id,
            'deleted': serializer.data
        }

        todo_model.delete()

        return Response(response, status=status.HTTP_200_OK)
