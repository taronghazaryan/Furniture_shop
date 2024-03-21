def request_data(get_response):
    def middleware(request):
        request.meta.user_agent = request.META['HTTP_USER_AGENT']
        request.meta.user_ip = request.META['REMOTE_ADDR']
        request.meta.user_name = request.META['LOGNAME']
        response = get_response(request)
        return response
    return middleware



