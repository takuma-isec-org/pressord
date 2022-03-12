from flask import (Blueprint, Flask)

bp = Blueprint('article', __name__, url_prefix='/article')

@bp.route('/<postId>', methods=['GET'])
def show_article(postId):
    # 記事を表示する
    return ''

