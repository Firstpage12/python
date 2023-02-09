from flask import Flask,render_template,url_for
from flask_restful import Api

from item import Item,ItemList

app = Flask(__name__)
api = Api(app)


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList,"/items")






if __name__=="__main__":
    app.run(debug=True)

