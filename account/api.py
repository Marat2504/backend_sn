from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .forms import SignupForm


@api_view(['GET'])
def me(request):
    return JsonResponse(
        {
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
            'profile': request.user.user_profile.id
        }
    )


@api_view(['POST'])
@authentication_classes([])
@permission_classes([])
def signup(request):
    data = request.data
    message = 'success'
    print(request.data)
    form = SignupForm(
        {
            "email": data.get('email'),
            "username": data.get('username'),
            "password1": data.get('password1'),
            "password2": data.get('password2'),
        }
    )

    if form.is_valid():
        form.save()
        errors = []
    else:
        message = 'error'
        errors_dict = form.errors.as_data()
        errors = []
        for field_errors in errors_dict.values():
            for error in field_errors:
                errors.append(str(*error))

        print(errors)

    return JsonResponse({'status': message, 'errors': errors})