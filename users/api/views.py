from django.core.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import rest_framework.status as status
import users.models as userModels


class CheckUserView(APIView):
    '''
    유저의 유무를 확인합니다.
    nonce를 리턴합니다. 없는 유저일 경우 nonce로 0을 리턴합니다.
    '''

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            wallet_address = data['address']

            user = userModels.User.objects.filter(wallet_address=wallet_address)
            return Response({"nonce":user.first().nonce} if user else {"nonce":0}, status=status.HTTP_200_OK)    
        except KeyError:
            return Response({"message": "INVALID_KEY"}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"message": "INVALID_TYPE"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({"message": "VALIDATION_ERROR"}, status=status.HTTP_400_BAD_REQUEST)

class SignUpView(APIView):    
    '''
    회원가입 API입니다.
    '''    

    permission_classes = [AllowAny]

    def post(self, request):
        try:
            data = request.data
            wallet_address = data['address']

            user = userModels.User.objects.filter(wallet_address=wallet_address)
            if user:
                raise ValidationError

            user = userModels.User.objects.create(username=wallet_address, wallet_address=wallet_address)

            return Response({"nonce":user.nonce}, status=status.HTTP_200_OK)        
        except KeyError:
            return Response({"message": "INVALID_KEY"}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"message": "INVALID_TYPE"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({"message": "VALIDATION_ERROR"}, status=status.HTTP_400_BAD_REQUEST)

class ValidateToken(APIView):
    '''
    Token을 Validate합니다.
    '''

    permission_classes=[IsAuthenticated]

    def get(self, request):
        token, _ = Token.objects.update_or_create(user=request.user)

        return Response({"message":"Permission Granted","token":token.key}, status=status.HTTP_200_OK) 