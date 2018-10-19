

def entity_to_dict(data,
                   list_entities=None,
                   skip_failed_item=True,
                   ):
    """
    エンティティ・カラムの一覧を dict 化する

    :param data:　エンティティ・カラムの実体
    :param list list_entities: 吐き出すエンティティ・カラム
    :param skip_failed_item: 読み込みに失敗したものはスキップ
    :return dict:
    """
    result = []
    if not isinstance(data, list):
        data = [data]
    for dat in data:
        dic = {}
        for i, d in enumerate(dat):
            try:
                dic.update(d.export_dict())
            except AttributeError:
                if list_entities:
                    dic[list_entities[i].name] = d
                elif skip_failed_item:
                    pass
                else:
                    raise ValueError(f'parseできません: {d}')
        result.append(dic)
    return result
