from flask import jsonify, make_response


def create_response(status=200, data=None, msg="", errors={}, meta=None):
    response = jsonify({
        "data": data,
        "msg": msg,
        "errors": errors,
        "meta": meta
    })
    return make_response(response, status)
