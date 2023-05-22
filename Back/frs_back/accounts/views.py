from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProfileChangeSerializer
from rest_framework import status

User = get_user_model()

@api_view(['GET', 'PUT'])  # GET과 PUT 메서드 허용
def profile_change(request):
    if not request.user.is_authenticated:
        return Response("Authentication required", status=status.HTTP_401_UNAUTHORIZED)
    
    user = request.user
    if request.method == 'PUT':  # PUT 요청 처리
        serializer = ProfileChangeSerializer(user, data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()  # 유효한 경우 데이터 저장
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET 요청 처리
    serializer = ProfileChangeSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)

