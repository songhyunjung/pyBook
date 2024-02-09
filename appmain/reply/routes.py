from flask import Blueprint, request, make_response, jsonify

import sqlite3

from appmain import app

from appmain.utils import verifyJWT, getJWTContent

reply = Blueprint('reply', __name__)


@reply.route('/api/reply/leave', methods=['POST'])
def leaveReply():
    headerData = request.headers
    data = request.form

    authToken = headerData.get("authtoken")

    payload = {"success": False}

    if authToken:
        isValid = verifyJWT(authToken)

        if isValid:
            token = getJWTContent(authToken)
            username = token["username"]

            articleNo = data.get("articleNo")
            reply = data.get("reply")

            conn = sqlite3.connect('pyBook.db')
            cursor = conn.cursor()

            if cursor:
                SQL = 'INSERT INTO replies (author, description, targetArticle) VALUES(?,?,?)'
                cursor.execute(SQL, (username, reply, articleNo))
                replyNo = cursor.lastrowid
                conn.commit()

                cursor.close()
            conn.close()

            payload = {"success": True, "replyNo": replyNo, "author": username, "desc": reply}
        else:
            pass
    else:
        pass
    return make_response(jsonify(payload), 200)