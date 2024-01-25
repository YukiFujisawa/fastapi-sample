# fastapi-sample

予約会議システムAPI

## DB設計

- users
  - id: int
    - ユーザーID
  - user_name: str
    - ユーザー名
- rooms
  - id: int
    - 会議室ID
  - room_name: str
    - 会議室名
  - capacity: int
    - 定員数
- bookings
  - id: int
    - 予約ID
  - user_id: int
    - ユーザーID(外部キー)
  - room_id: int
    - 会議室ID(外部キー)
  - reserved_num: int
    - 予約人数
    - rooms.capacityを上限とする
  - start_datetime: datetime
    - 開始時刻
    - 30分刻み
    - 09:00〜20:00
  - end_datetime: datetime
    - 終了時刻
    - 15分刻み
    - 09:00〜20:00

## 機能

- users(ユーザー)
  - 一覧  
  - 登録
  - 詳細
- rooms(会議室)
  - 一覧   
  - 登録
  - 詳細
- bookings(予約)
  - 一覧  
  - 登録
  - 詳細

## DB周り

```
python manage.py makemigrations db;
python manage.py migrate
```

1. makemigrations
    - マイグレーションファイルを作成する
2. migrateはモデルをデータベースに反映させる
    - マイグレーションファイルを元にDatabaseを変更する

### 参考

- [Django ORM Standalone](https://github.com/dancaron/Django-ORM)
- [MakemigrationsとMigrateについて](https://qiita.com/frosty/items/8c715a53d7920c9cd1eb)
- [Django Models](https://docs.djangoproject.com/en/5.0/topics/db/models/)
