# ๐ฎ Specialties Backend README

๋๊ตฌ๋ ์ฝ๊ฒ ๋ธ๋ก์ฒด์ธ์ ์ด์ฉํด ์ปค๋ฎค๋ํฐ๋ฅผ ๋ง๋ค ์ ์๋ ์๋น์ค์๋๋ค. w3์ ๊ฑธ๋ง๊ฒ ๋ชจ๋  ์ปค๋ฎค๋ํฐ๋ ๊ฐ๊ฐ ํ๋์ DAO๋ก์ ํ๋ํ  ์ ์๋๋ก ํ๋ tool์ ์ ๊ณตํ๋ ๊ฒ์ด ๊ถ๊ทน์ ์ธ ๋ชฉํ์๋๋ค.

**Klaytn Blockchain**์ ์ฌ์ฉํฉ๋๋ค.

# Models

- core
- users : username์ ์ง๊ฐ ์ฃผ์๋ก ๊ฐ์ฃผํฉ๋๋ค.
- chats
- communities
- agendas
- categories
- posts
- comments

# ์ฑํ

[Django Channels](https://channels.readthedocs.io/en/latest/index.html#django-channels): WebSocket, chat protocol ๋ฑ๋ฑ์ ์ฌ์ฉํ  ์ ์๊ฒ ํด์ฃผ๋ ๋ชจ๋์๋๋ค. (์ถํ ๊ณต๋ถ ํ์)

# API

## `/users`

- `users/checkuser` : ์ ์  ์กด์ฌ ์ ๋ฌด ํ์ธ ํ nonce๋ฅผ ์ ๊ณต
- `users/signup` : ์ ์  ์์ฑ
- `users/auth` : Web3 ๋ก๊ทธ์ธ์ ์ํด Frontend์์ ์๋ช๋ signature๋ฅผ ๊ฒ์ฆ
- `users/checkpermission` : Token ์ ํจ์ฑ ๊ฒ์ฆ
