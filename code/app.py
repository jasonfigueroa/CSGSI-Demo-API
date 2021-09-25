from flask import Flask, jsonify
from flask_restful import Api
from flask_cors import CORS

from blacklist import BLACKLIST
from resources.user import UserSteamId
from resources.match import Match, MatchList
from resources.match_stats import MatchStats

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'test' # omit this line if publishing this source code to a 
						# public location
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/*": {"origins": ["https://csgsistattrakr.jasonfigueroa.io", "http://localhost:5000"]}})
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

api.add_resource(UserSteamId, '/user/steamid')
api.add_resource(Match, '/match', '/match/<_id>')
api.add_resource(MatchList, '/match/list')
api.add_resource(MatchStats, '/matchstats', '/matchstats/<_id>')

if __name__ == '__main__':
	from db import db # Should I move this to the top of this file?
	db.init_app(app)
	app.run(host="localhost", port=3000, debug=True)