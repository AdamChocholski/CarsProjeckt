from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask(__name__)
api = Api(app)
cars = [
    {
        "id":1,
        "brand": "Ford",
        "name": "Focus"
    },
    {
        "id":2,
        "brand": "BMW",
        "name": "SecurityPlus"
    },
    {
        "id":3,
        "brand": "Nissan",
        "name": "June"
    }
]

class Car(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(cars), 200
        for name in cars:
            if(name["id"] == id):
                return name, 200
        return "Nie znaleziono auta", 404

    def post(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("brand")
      parser.add_argument("name")
      params = parser.parse_args()
      for name in cars:
          if(id == name["id"]):
              return f"Samochod o id {id} już istnieje", 400
      name = {
          "id": int(id),
          "brand": params["brand"],
          "name": params["name"]
      }
      cars.append(name)
      return name, 201

    def put(self, id):
      parser = reqparse.RequestParser()
      parser.add_argument("brand")
      parser.add_argument("name")
      params = parser.parse_args()
      for name in cars:
          if(id == name["id"]):
              name["brand"] = params["brand"]
              name["name"] = params["name"]
              return name, 200
      name = {
          "id": id,
          "brand": params["brand"],
          "name": params["name"]
      }
      cars.append(name)
      return name, 201

    def delete(self, id):
      global cars
      cars = [qoute for qoute in cars if qoute["id"] != id]
      return f"Usunięto samochod o id {id}.", 200

api.add_resource(Car, "/cars", "/cars/", "/cars/<int:id>")

if __name__ == '__main__':
    app.run(debug=True) 