from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import ChangePasswordSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse

@extend_schema(
        request=ChangePasswordSerializer,
        responses={200: OpenApiResponse(description='Password Update successfully')}
)
#este agrega el cambio de contraseña en el login 
@api_view(['post'])
@permission_classes([IsAuthenticated])
def change_password(request):
    user = request.user
    serializer = ChangePasswordSerializer(data= request.data)
    serializer.is_valid(raise_exception=True)

    current_password = serializer.validated_data['current_password']
    new_password = serializer.validated_data['new_password']

    #verifica que la contraseña sea correcta
    if not user.check_password(current_password):
        return Response({'detail':'You current password is incorrect'})
    
    user.set_password(new_password)
    user.save()
    return Response({'detail':'Password changed successfully'})

#**************************************************
'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailTokenObtainSerializer
from drf_spectacular.utils import extend_schema, OpenApiResponse


class EmailTokenObtainView(APIView):
    @extend_schema(
        request=EmailTokenObtainSerializer,
        responses={
            200: OpenApiResponse(description='Token obtenido exitosamente'),
            400: OpenApiResponse(description='Error de validación'),
        }
    )

    def post(self, request):
        serializer= EmailTokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)
'''