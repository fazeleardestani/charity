from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from charities.serializers import BenefactorSerializer, CharitySerializer
from .serializers import UserSerializer


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        request.user.auth_token.delete()
        return Response(
            data={'message': f'Bye {request.user.username}!'},
            status=status.HTTP_204_NO_CONTENT
        )


class UserRegistration(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response( serializer.data, status=status.HTTP_201_CREATED)



