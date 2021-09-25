from flask_restful import Resource, reqparse
from models.match_stats import MatchStatsModel

class MatchStats(Resource):
    def get(self, _id):
        match_stats = MatchStatsModel.find_by_id(_id)
        if match_stats:
            return match_stats.json()
        return {"message": "Match stats not found."}, 404
