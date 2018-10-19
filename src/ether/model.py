from .core import query as ether_query


class ModelBase:
    exclude_columns = []

    @property
    def __tablename__(self):
        raise NotImplementedError

    @classmethod
    def columns(cls):
        """
        モデルのカラム一覧

        :return list[str]:
        """
        return cls.__table__.columns.keys()

    @classmethod
    def writable_columns(cls):
        """
        自動設定するカラムなど外から設定されたくないカラムを除外したカラム一覧

        :return list[str]:
        除外するカラム名はクラス変数 ``exclude_columns`` で定義する
        """
        return (col for col in cls.columns()
                if col not in cls.exclude_columns)

    @classmethod
    def primary_id(cls):
        """
        ``{__tablename__}_id`` はプライマリキーと仮定し、これを返す
        :return str:
        """
        return f'{cls.__tablename__}_id'

    @classmethod
    def get_by_id(cls, id_):
        """
        プライマリーキーを指定してエンティティを返す

        :param id_: プライマリーキー
        :return entity:
        """
        query = ether_query(cls).filter(
            getattr(cls, cls.primary_id()) == id_)
        return query.first()

    def export_dict(self):
        """
        エンティティを dict オブジェクト化する

        :return dict:
        """
        data = {}
        for col in self.columns():
            data[col] = getattr(self, col)
        return data

    @classmethod
    def import_dict(cls, dic):
        """
        dict オブジェクトを読み込んでエンティティ化する

        :param dict dic:
        :return entity:
        """
        data = {}
        for col in cls.writable_columns():
            data[col] = dic.get(col)
        return cls(**data)

    def update_from_dict(self, dic):
        """
        dict を読み込んで entity の情報を更新する

        :param dic:
        :return:
        """
        for col in self.writable_columns():
            try:
                value = dic[col]
            except KeyError:
                continue
            setattr(self, col, value)
