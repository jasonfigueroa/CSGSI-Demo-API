from flask_restful import Resource, reqparse
from models.user import UserModel

class UserSteamId(Resource):

	def get(self):
		current_user_id = 1
		user = UserModel.find_by_id(current_user_id)
		if user:
			return {"steam_id": user.steam_id}
		return {"message": "Steam id not found"}, 404
