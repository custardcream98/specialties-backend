from web3.auto import w3
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
import rest_framework.status as status
from eth_account.messages import SignableMessage
from eth_utils.curried import to_bytes
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
import users.models as userModels
from  core.modules.randomId import RandomIdGenerator
randomIdGenerator = RandomIdGenerator()


class VarifySignedMsgView(APIView):

    """
    signature를 이용해 Validate하는 View
    """

    """ 
    eth_account.messages.encode_defunct()를 참고해
    클레이튼에 맞게 코드를 작성했습니다.

    caver-js로 서명할 때는 prefix가 자동으로 들어가는데,
    그 부분에서 수정이 필요했습니다.
    (이를 통해 클레이튼의 고유 서명임을 나타냅니다.)
    """
    def post(self, request):
        try:
            data = JSONParser().parse(request)

            wallet_address = data['address']
            user = userModels.User.objects.get(wallet_address=wallet_address)
            sig = data['signature']

            message_bytes = to_bytes(text=f'Specialties 로그인을 위한 서명입니다.\n로그인을 위한 과정이니 걱정하지 마세요!\n\nnonce : {user.nonce}')
            msg_length = str(len(message_bytes)).encode('utf-8')
            msg = SignableMessage(
                b'K',
                b'laytn Signed Message:\n' + msg_length,
                message_bytes,
            )

            # nonce를 새로 발급합니다.
            user.nonce = randomIdGenerator.randomId(seed=sig,size=15)
            user.save()

            signed_address = (w3.eth.account.recover_message(signable_message=msg, signature=sig)).lower()
            if signed_address == wallet_address:
                # Validation을 통과한 경우입니다. 로그인 토큰을 발급합니다.
                token, _ = Token.objects.update_or_create(user=user)
                return Response({"token":token.key}, status=status.HTTP_200_OK)  
            else:
                raise ValidationError      
        except KeyError:
            return Response({"message": "INVALID_KEY"}, status=status.HTTP_400_BAD_REQUEST)
        except TypeError:
            return Response({"message": "INVALID_TYPE"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError:
            return Response({"message": "VALIDATION_ERROR"}, status=status.HTTP_400_BAD_REQUEST)