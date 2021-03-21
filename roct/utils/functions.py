from flask import jsonify

def paginate(query, page, per_page):
    page = query.paginate(page=page, per_page=per_page)
    items = [e.serialize() for e in page.items]
    info = {
        "page": page.page,
        "per_page": page.per_page,
        "total": page.total
    }

    return jsonify({
        'data': items,
        "info": info
    })