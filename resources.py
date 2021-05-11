from flask_restful import Resource, reqparse



class Login(Resource):
	def get(self):
		return {"message": "get login"}
		

class Users(Resource):
	def get(self):
		return {"message": "get users"}

