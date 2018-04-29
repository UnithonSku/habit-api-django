# Habit UP - API

Habit UP 의 API 입니다.

## 로컬에서 개발하기

1. 레포지토리 클론

```
$ git clone https://github.com/UnithonSku/habit-api-django
```

2. 가상환경 설정 및 패키지 설치

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### 각종 스크립트

- 로컬 서버 실행 : `run-dev-server.sh` (migration 포함)
- 테스트 : `test.sh`
- AWS 설정 : `setup-eb.sh`

## 배포

1. Elastic Beanstalk CLI 설치

```
$ pip install awsebcli --upgrade
```

2. Elastic Beanstalk 설정

```
$ ./setup_eb.sh
```

(만약 실행권한 없을시 `chmod 755` 먼저 수행)

3. CLI 를 통하여 배포

```
$ eb deploy
```

(`master` 브랜치에 머지 시 자동으로 배포됨)


## API Reference

- [Postman docs](https://documenter.getpostman.com/view/3135479/habit-api/RW1bmeWq)

