from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


@app.route('/', methods=['GET'])
def index():
    return 'Hello'


@app.route('/initialize_db', methods=['GET'])
def init_db():
    from initialize_db import run
    run()
    return 'ok'


@app.route('/member', methods=['GET'])
def list_member():
    import ether
    from app.model import Member
    q = ether.query(Member)
    res = ''.join(f'<li>{m.member_id}: {m.member_name}</li>' for m in q.all())
    return res


@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    from app.model import Member
    member = Member.get_by_id(member_id)
    return jsonify(member.export_dict())


def main():
    app.run()


if __name__ == '__main__':
    main()
