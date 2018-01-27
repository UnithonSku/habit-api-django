from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def api_route(request):
    if request.method == 'GET':
        response = {
            'message': 'welcome to habit api!',
            'routes': {
                'user api': [
                    '/users'
                ],
                'todo api': [
                    '/todos',
                    '/todos/create',
                    '/todos/update',
                    '/todos/delete',
                ],
                'collections api': [
                    '/collections',
                    '/collections/create',
                    '/collections/update',
                    '/collections/delete'
                ]
            }
        }
        return Response(response, status=200)
