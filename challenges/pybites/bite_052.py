"""
Bite 52. Create a movie quote API with Flask 

https://codechalleng.es/bites/52
"""
 
from flask import Flask, jsonify, abort, request

app = Flask(__name__)

quotes = [
    {
        "id": 1,
        "quote": "I'm gonna make him an offer he can't refuse.",
        "movie": "The Godfather",
    },
    {
        "id": 2,
        "quote": "Get to the choppa!",
        "movie": "Predator",
    },
    {
        "id": 3,
        "quote": "Nobody's gonna hurt anybody. We're gonna be like three little Fonzies here.",  # noqa E501
        "movie": "Pulp Fiction",
    },
]

rr = []
def _get_quote(qid):
    """Recommended helper"""
    for q in quotes:
        if q["id"] == qid:
            return q
    return None


def _quote_exists(existing_quote):
    """Recommended helper"""
    for q in quotes:
        if q["quote"] == existing_quote:
            return True
    return False


@app.route('/api/quotes', methods=['GET'])
def get_quotes():
    return jsonify({"quotes":quotes})


@app.route('/api/quotes/<int:qid>', methods=['GET'])
def get_quote(qid):
    q = _get_quote(qid)
    if q is None:
        return abort(404)
    return jsonify({"quotes":[q]})


@app.route('/api/quotes', methods=['POST'])
def create_quote():
    r = request.get_json()
    try:
        quote = r["quote"]
        if _quote_exists(quote):
            return abort(400)
        movie = r["movie"]    
        qid = 4    
        new_quote={"id":qid, "quote":quote, "movie":movie}    
        quotes.append(new_quote)    
        return (jsonify({"quote":new_quote}), 201)
    except:
        return abort(400)


@app.route('/api/quotes/<int:qid>', methods=['PUT'])
def update_quote(qid):
    r = request.get_json()
    try:        
        for idx, q in enumerate(quotes):
            print(idx)
            if q["id"] == qid:
                quote = r["quote"]
                movie = r["movie"]
                if q["quote"] == r["quote"]:
                    new_quote = q #old
                else:                    
                    new_quote={"id":qid, "quote":quote, "movie":movie}  
                    quotes[idx] = new_quote
                return (jsonify({"quote":new_quote}), 200)
    except:
        return abort(400)
    return abort(404)
    


@app.route('/api/quotes/<int:qid>', methods=['DELETE'])
def delete_quote(qid):
    for idx, q in enumerate(quotes):
        if q["id"] == qid:
            quotes.pop(idx)
            return (jsonify({"quotes":[q]}), 204)
    return abort(404)
            


    