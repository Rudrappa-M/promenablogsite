import datetime
import jwt
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from .models import Token
from .serializers import TokenSerializer, SchemaView, GetSerializer


@swagger_auto_schema(methods=['get'], responses={200: GetSerializer(many=True)})
@api_view(['GET'])
def Login_List(request):
    token = Token.objects.all()
    serializer = TokenSerializer(token, many=True)
    return Response(serializer.data)


@swagger_auto_schema(methods=['post'], request_body=SchemaView)
@api_view(['POST'])
def User_Login(request):
    serializer = TokenSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@swagger_auto_schema(methods=['post'], request_body=SchemaView)
@api_view(['POST'])
def Token_Cookie(request):
    email = request.data['email']
    tokens = Token.objects.filter(email=email).first()
    if tokens is None:
        raise AuthenticationFailed("user not found")
    payload = {
        'id': tokens.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
        # 'iat': datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=Token)
    response.data = {
        'jwt': token
    }
    return response


@swagger_auto_schema(methods=['get'], responses={200: GetSerializer(many=True)})
@api_view(['GET'])
def View_User(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("Unauthenticated!")
    tokens = Token.objects.filter(id=payload['id']).first()
    serializer = TokenSerializer(tokens)
    return Response(serializer.data)

