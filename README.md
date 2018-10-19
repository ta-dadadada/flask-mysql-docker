# flask-mysql-docker

flask と sqlalchemy と mysql で動くサービスの雛形

## How to Use

docker, docker-compose のインストールは前提とします。

build

```sh
cd <your-path>/flask-mysql-docker
sudo docker-compose build
```

起動

```sh
sudo docker-compose up -d
```

DB の確認

```sh
sudo docker-compose exec db mysql -uapp -papp app
```

## アプリケーション

url: http://0.0.0.0:5001

### DB の初期化

起動したらはじめにアクセスしておく

* http://0.0.0.0:5001/initialize_db

### GET

* http;//0.0.0.0:5001/member
* http;//0.0.0.0:5001/member/1
