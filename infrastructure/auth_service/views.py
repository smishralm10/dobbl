from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from auth.adapters.repository import DjangoUserRepository
from auth.value_object.values import PasswordStrengthError
from auth.use_cases.use_cases import create_user, UserAlreadyExistError
from .models import User

# Create your views here.
class UserRegisterView(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        error = self._execute_usecase(serializer)
        if error:
            return Response(error, status=status.HTTP_400_BAB_REQUEST)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def _execute_usecase(self, serializer):
        repository = DjangoUserRepository(User)
        try:
            create_user(repository, serializer.data['username'], serializer.data['password'])
            return None
        except UserAlreadyExistError:
            return {'error': 'User already exists'}
        except PasswordStrengthError as e:
            return {'error': str(e)}
        