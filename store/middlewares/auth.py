from django.shortcuts import redirect

def auth_middleware(get_reponse):


    def middleware(request):
        returnUrl = request.META['PATH_INFO']
        print(request.META['PATH_INFO'])
        if not request.session.get('customer'):
            return redirect(f'login?return_url={returnUrl}')

        response = get_reponse(request)
        return response

    return middleware