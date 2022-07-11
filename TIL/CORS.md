# Cross Origin Resource Sharing

보안상 이유로 웹 페이지 상의 제한된 리소스를 최초 자원이 서비스된 도메인 밖의 다른 도메인으로부터 요청할 수 없게 돼있는데, 이걸 Django에서 `django-cors-headers` 모듈 설치로 해결할 수 있습니다.

이걸 몰라서 `Dayplan.it`때 그렇게 해멨는데, 이제야 알았네요.

`settings.py`에 꼭 INSTALLED_APPS, MIDDLEWARE, CORS 관련 세팅 추가해줘야 합니다!
