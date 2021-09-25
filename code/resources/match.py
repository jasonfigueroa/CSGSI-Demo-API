from flask_restful import Resource, reqparse
from models.match import MatchModel

class Match(Resource):
    def get(self, _id):
        match = MatchModel.find_by_id(_id)
        if match:
            return match.json()
        return {"message": "Match not found"}, 404

class MatchList(Resource):
    def get(self):
        matches = [match.json() for match in MatchModel.query.all() if match.user_id == 1]

        return {"matches": matches}
