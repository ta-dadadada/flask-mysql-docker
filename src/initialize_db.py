from ether import engine, Base
from app.model import Member


def create_table(drop_first=True):
    if drop_first:
        Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def add_initialize_data():
    import json
    from ether import add
    with open('init.json', 'r') as f:
        data = json.load(f)
    for member_info in data['member']:
        m = Member.import_dict(member_info)
        add(m)

def run():
    create_table()
    add_initialize_data()

if __name__ == '__main__':
    run()