from flask import Flask, request, jsonify
from summary import get_summary, get_recommendation
from controller.UserController import UserController
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = "1234"
jwt = JWTManager(app)


@app.route("/", methods=["GET"])
def home():
    return "Halo Dunia"

@app.route("/login", methods=["POST"])
def login():
    return UserController.loginUser(request=request)


@app.route("/users", methods=["GET"])
@jwt_required()
def listUsers():
    return UserController.listUser()

@app.route("/users/<id>", methods=["GET"])
@jwt_required()
def detailUser(id):
    return UserController.detailUser(id)


@app.route("/users/<id>", methods=["DELETE"])
@jwt_required()
def hapusUser(id):
    return UserController.hapusUser(id)

@app.route("/users/<id>", methods=["PUT"])
@jwt_required()
def ubahUser(id):
    return UserController.ubahUser(request=request, id=id)

@app.errorhandler(404)
def not_found(e):
    response = {
        "sukses": 404,
        "pesan": "Tidak ditemukan"
    }
    return jsonify(response)


@app.route("/register", methods=["POST"])
def register():
    return UserController.register(request=request)

@app.route("/product/<id>", methods=["POST"])
def detail_product(id):
    nama = request.form.get('nama')
    response = {
        "sukses": 1,
        "data": {
            "id": id,
            "nama": nama
        }
    }
    summary = get_summary(nama)
    output = jsonify({
        "response": response,
        "summary": summary
    })
    return output

@app.route("/product/<id>/recommendation", methods=["GET"])
def get_recommendation_route(id):
    nama = request.form.get('nama')
    response = {
        "sukses": 1,
        "data": {
            "id": id,
            "nama": nama
        }
    }
    recommendations = get_recommendation(nama)  
    output = jsonify({
        "response": response,
        "recommendation": recommendations
    })
    return output

@app.route("/product/<id>", methods=["PUT"])
def change_product(id):
    if request.files == None:
        f = request.files['foto']
        foto = f.filename
        f.save(f"static/img/{foto}")
    else:
        foto = "Tidak Pilih Foto"
        print("tidak pakai foto")
    print(request.files)
    response = {
        "sukses": 1,
        "data": {
            "email": request.form.get("email"),
            "nama": request.form.get("nama"),
            "telp": request.form.get('telp'),
            "foto": foto
        }
    }
    return jsonify(response)

@app.route("/product/<id>", methods=["DELETE"])
def delete_product(id):
    response = {
        "sukses": 1,
        "data": f'data pada id {id} berhasil dihapus'
    }
    return jsonify(response)

@app.route("/product", methods=["POST"])
def tambah_product():
    response = {
        "sukses": 1,
        "data": {
            "id": request.form.get("id"),
            "nama": request.form.get("nama")
        }
    }
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5173)
