from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse
import json
from users.functions import get_current_role


def role_required(roles):
    def _method_wrapper(view_method):
        def _arguments_wrapper(request, *args, **kwargs) :
            current_role = get_current_role(request)
            if not current_role in roles:
                if request.is_ajax():
                    response_data = {
                        "status" : "false",
                        "stable" : "true",
                        "title" : "Permission Denied",
                        "message" : "You have no permission to do this action."
                    }
                    return HttpResponse(json.dumps(response_data), content_type='application/javascript')
                else:
                    context = {
                        "title" : "Permission Denied"
                    }
                    return render(request, 'users/403.html', context)

            return view_method(request, *args, **kwargs)

        return _arguments_wrapper

    return _method_wrapper
