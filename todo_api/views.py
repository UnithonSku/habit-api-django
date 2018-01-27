from rest_framework.views import APIView
from django.http.response import JsonResponse


class TodoView(APIView):
    def post(self, request):
        print(request.POST)
        return JsonResponse({'status': 'method POST not implemented!'})


class TodoCreateView(APIView):
    def post(self, request):
        pass


class TodoUpdateView(APIView):
    def post(self, request):
        pass


class TodoDeleteView(APIView):
    def post(self, request):
        pass
