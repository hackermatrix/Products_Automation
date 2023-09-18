
from flask import Flask, request, Response,jsonify
from utils.scrapper import scrap_amazon



app = Flask(__name__)

@app.route("/amazon",methods=['GET'])
def amazon():
    args = request.args
    cat =  args.get('category')

    res = scrap_amazon(cat)

   
    return jsonify({"prod_list":res})