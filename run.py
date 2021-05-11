from api_service import app, api
from resources import(
		Login,
		Users		
		)


api.add_resource(Login, "/login")
api.add_resource(Users, "/users")


app.run(host='127.0.0.1', port='5000', debug=True)
