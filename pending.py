from flask import (Blueprint, Flask)

bp = Blueprint('pending', __name__, url_prefix='/pending')

@bp.route('/preview/<pendingCode>', methods=['GET'])
def preview(pendingCode):
    # 記事のプレビューを表示する。
    return ''

@bp.route('/action/<pendingCode>', methods=['GET'])
def action(pendingCode):
    # プレビューサイト上で記事に対する操作を行うときに使用。Azure DirectoryのOauth2.0へリダイレクトする。パラメータがgrantだったらリダイレクトURLをgrantにする。rejectだったらrejectを設定する。
    return ''

@bp.route('/grant/<pendingCode>', methods=['GET'])
def grant(pendingCode):
    # AD認証の返り値の検証。その後、登録されている承認者であれば、firestore上に登録して公開。
    return ''

@bp.route('/reject/<pendingCode>', methods=['GET'])
def reject(pendingCode):
    # AD認証の返り値の検証。その後、登録されている認証者であれば、firestore上にrejectとreasonを登録。
    return ''

    