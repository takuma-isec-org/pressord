from flask import (Blueprint, Flask)

bp = Blueprint('member', __name__, url_prefix='/m')

@bp.route('/login', methods=['GET'])
def login():
    # DiscordのOauth2.0にリダイレクトする
    return ''

@bp.route('/allocate', methods=['GET','POST'])
def allocate():
    # DiscordのOauth2.0のリダイレクト先。/m/allocate。ここでtakuma-isec.orgに参加しているかの確認と、firestore上にユーザ情報が入っているかの確認。ログインセッションの発行を行う。ここまでやったら/にリダイレクトする。
    return ''

@bp.route('/edit/name', methods=['POST'])
def edit_name():
    # 公開ユーザ名の変更。POSTで値が流れてくるので、firestoreの値を書き換えて/へリダイレクトする。
    return ''

    