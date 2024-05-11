# from django.http import HttpResponse
#
#
# def image_validation(get_response):
#     def middleware(request):
#
#         if request.path == '/product/add/':
#
#             images = request.FILES.getlist('images')
#             for image in images:
#                 if not image.lower().endswith(('jpeg', 'jpg', 'png')):
#                     return HttpResponse('wrong format image')
#         response = get_response(request)
#         return response
#
#     return middleware
