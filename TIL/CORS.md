# Cross Origin Resource Sharing

보안상 이유로 웹 페이지 상의 제한된 리소스를 최초 자원이 서비스된 도메인 밖의 다른 도메인으로부터 요청할 수 없게 돼있는데, 이걸 Django에서 `django-cors-headers` 모듈 설치로 해결할 수 있습니다.

이걸 몰라서 `Dayplan.it`때 그렇게 해멨는데, 이제야 알았네요.

`settings.py`에 꼭 INSTALLED_APPS, MIDDLEWARE, CORS 관련 세팅 추가해줘야 합니다!

# Handle Klaytn Signature on python

Frontend에서 넘어오는 서명을 Validate 하기 위해 어떻게 해야 할 지 시행착오가 많았습니다.

python을 위한 Klaytn Caver 모듈이 없으므로 web3 모듈을 사용했으나, 메세지를 SignableMessage로 변환시 오류가 있어 시행착오가 있었습니다.

Caver 패키지를 이용해 서명을 할 경우 특정 문구("Klaytn Signed Message")가 삽입되는데, web3 패키지에서는 이 과정이 이더리움에 맞게 일어나고 있었기에 해당 부분을 수정해 해결했습니다.

자세한 코드는 [Validation View](../core/crypto/validation.py)를 참고해주세요!

# Web3에서의 로그인이 일어나는 과정

(추후 이미지 삽입 예정)

1. Frontend에서 User의 Address를 서버로 Post합니다.
2. Backend에서 Address를 이용해 유저의 존재 유무를 확인 후 nonce를 return합니다.
   - 만약 User가 없을 경우, 새로운 유저를 생성합니다. User 생성 순간 nonce가 자동으로 발급됩니다.
3. Frontend에서 메세지 `Specialties 로그인을 위한 서명입니다. 로그인을 위한 과정이니 걱정하지 마세요! nonce : (nonce)`를 서명합니다. 서명된 signature와 Address를 서버로 Post합니다.
4. Backend에서 signature와 Address를 이용해 Validate 후, 통과할 경우 로그인을 허용합니다.
   - Validate 과정에서 보안을 위해 유저의 nonce를 새로 발급합니다.
