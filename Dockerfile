# Python 3.8 이미지를 기반으로 빌드
FROM python:3.8-slim

RUN apt-get update && apt-get install -y curl

# 작업 디렉터리 설정
WORKDIR /app

ADD . /app

# Flask와 필요한 라이브러리 설치
RUN pip install -r requirements.txt

RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime && echo Asia/Seoul > /etc/timezone

EXPOSE 39999

# Flask 앱 실행
CMD ["python", "app.py"]

