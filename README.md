# 🔮 Specialties Backend README

누구나 쉽게 블록체인을 이용해 커뮤니티를 만들 수 있는 서비스입니다. w3에 걸맞게 모든 커뮤니티는 각각 하나의 DAO로서 활동할 수 있도록 하는 tool을 제공하는 것이 궁극적인 목표입니다.

**Klaytn Blockchain**을 사용합니다.

# Models

- core
- users
- chats
- communities
- agendas
- categories
- posts
- comments

# 채팅

[Django Channels](https://channels.readthedocs.io/en/latest/index.html#django-channels): WebSocket, chat protocol 등등을 사용할 수 있게 해주는 모듈입니다. (추후 공부 필요)

# API

## `/users`

- `users/checkuser` : 유저 존재 유무 확인 후 nonce를 제공
- `users/signup` : 유저 생성
- `users/auth` : Web3 로그인을 위해 Frontend에서 서명된 signature를 검증
- `users/checkpermission` : Token 유효성 검증
