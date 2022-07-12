from django.core.exceptions import ValidationError
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import rest_framework.status as status
import users.models as userModels


class CheckUserView(APIView):        
    def post(self, request):
        try:
            data = JSONParser().parse(request)
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
    def post(self, request):
        try:
            data = JSONParser().parse(request)
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

