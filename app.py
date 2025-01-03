#import library
from flask import Flask , request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiasi objek
app = Flask(__name__)

#inisiasi objek flask-restfull
api = Api(app)

#insisiasi objek flask-cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {
    
}   #variable global, dictionary = json

#membuat kelas resource
class ContohResource(Resource):
    # metode get and post
    def get(self):
        # response = {"msg":"Hallo dunia, ini app restful pertamaku"}
        return identitas #tadina return response

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg" : "Data berhasil cobian we hela"}
        return response
        
    
    
#setup resourcenya
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == '__main__':
    app.run(debug=True, port=5005)