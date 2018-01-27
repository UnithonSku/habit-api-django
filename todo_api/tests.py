from django.test import TestCase
from rest_framework.test import APIRequestFactory
from todo_api.views import *


class TodoViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TodoView.as_view()

        self.sample_user = UserModel(id='sampleid')
        self.sample_user.save()

    def test_with_user_that_does_not_exist(self):
        request = self.factory.post('/todos/', data={'user': 'asdfasdf'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'User does not exist'})

    def test_with_user_that_does_exist(self):
        request = self.factory.post('/todos/', data={'user': 'sampleid'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TodoCreateViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TodoCreateView.as_view()

        self.sample_user = UserModel(id='sampleid')
        self.sample_user.save()

    def test_with_user_that_does_not_exist(self):
        request = self.factory.post(
            '/todos/create/', data={'user': 'asdfasdf', 'todo': 'TODO'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'User does not exist'})

    def test_with_user_that_does_exist(self):
        request = self.factory.post(
            '/todos/create/', data={'user': 'sampleid', 'todo': 'TODO'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user'], 'sampleid')
        self.assertEqual(response.data['created']['title'], 'TODO')
        self.assertFalse(response.data['created']['done'])


class TodoUpdateViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TodoUpdateView.as_view()

        self.sample_user = UserModel(id='sampleid')
        self.sample_user.save()

        self.sample_todo = TodoModel(
            user=self.sample_user, title='SAMPLE TODO')
        self.sample_todo.save()

    def test_with_user_that_does_not_exist(self):
        request = self.factory.post(
            '/todos/update/', data={
                'user': 'user-token',
                'todo': 'SAMPLE TODO',
                'update': {
                    'done': True
                }
            }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'User does not exist'})

    def test_with_todo_that_does_not_exist(self):
        request = self.factory.post(
            '/todos/update/', data={
                'user': 'sampleid',
                'todo': 'SAMPLETODO',
                'update': {
                    'done': True
                }
            }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'Todo does not exist'})

    def test_update_title(self):
        request = self.factory.post(
            '/todos/update/', data={
                'user': 'sampleid',
                'todo': 'SAMPLE TODO',
                'update': {
                    'title': '배틀그라운드 치킨먹기'
                }
            }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'sampleid')
        self.assertEqual(response.data['updated'], {'title': '배틀그라운드 치킨먹기'})

    def test_update_done(self):
        request = self.factory.post(
            '/todos/update/', data={
                'user': 'sampleid',
                'todo': 'SAMPLE TODO',
                'update': {
                    'done': True
                }
            }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'sampleid')
        self.assertEqual(response.data['updated'], {'done': True})

    def test_update_both(self):
        request = self.factory.post(
            '/todos/update/', data={
                'user': 'sampleid',
                'todo': 'SAMPLE TODO',
                'update': {
                    'title': '배틀그라운드 치킨먹기',
                    'done': True
                }
            }, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'sampleid')
        self.assertEqual(response.data['updated'], {
                         'title': '배틀그라운드 치킨먹기', 'done': True})


class TodoDeleteViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = TodoDeleteView.as_view()

        self.sample_user = UserModel(id='sampleid')
        self.sample_user.save()

        self.sample_todo = TodoModel(
            user=self.sample_user, title='SAMPLE TODO')
        self.sample_todo.save()

    def test_with_user_that_does_not_exist(self):
        request = self.factory.post(
            '/todos/delete/', data={'user': 'asdfasf', 'todo': 'SAMPLE TODO'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'User does not exist'})

    def test_with_todo_that_does_not_exist(self):
        request = self.factory.post(
            '/todos/delete/', data={'user': 'sampleid', 'todo': 'SAMPLETODO'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.data, {'status': 400, 'error': 'Todo does not exist'})

    def test_with_valid_data(self):
        request = self.factory.post(
            '/todos/delete/', data={'user': 'sampleid', 'todo': 'SAMPLE TODO'})
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user'], 'sampleid')
        self.assertEqual(response.data['deleted']['title'], 'SAMPLE TODO')
        self.assertFalse(response.data['deleted']['done'])
