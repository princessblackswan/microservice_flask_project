from flask import jsonify
from models.user import User
import re
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity


class UserController:
    def register(request):  
        errors = []
        email = request.form.get("email")
        password = request.form.get("password")
        telp = request.form.get('telp')
        nama = request.form.get('nama')
        reqHobi = request.form.getlist("hobi")
        if reqHobi:  
            hobi = ";".join(reqHobi)
            print(hobi)
        else:
            errors.append("Hobi wajib dipilih")

        if len(request.files) > 0:
            f = request.files['foto']
            foto = f.filename
            f.save(f"static/img/{foto}")
        else:
            errors.append("Foto wajib diisi")

        if not email:
            errors.append("Email wajib diisi")
        else:
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                errors.append("Format email tidak valid")

        if not password:
            errors.append("Password wajib diisi")
        if not nama:
            errors.append("Nama wajib diisi")
        
        if telp:
            if not str(telp).isnumeric() or not 8 <= len(telp) <= 12:
                errors.append("Telp wajib diisi antara 8 dan 12 angka")
        else:
            errors.append("Telp wajib diisi")

        if(len(errors)==0):
            User.tambahUser(nama=nama, email=email, password=password, hobi=hobi, telp=telp, foto=foto)
            response = {
                "sukses": 1,
                "pesan": f"{nama} berhasil didaftarkan"
            }
        else:
            response = {
                "sukses": 0,
                "pesan": errors
            }
        return jsonify(response)
    

    def listUser():
        data = User.listUser()
        response = {
            "sukses":1,
            "data": data
        }
        return jsonify(response)
    
    def detailUser(id):
        data = User.detailUser(id)
        response = {
            "sukses": 1,
            "data": data
        }
        return jsonify(response)
    
    def hapusUser(id):
        data = User.hapusUser(id)
        response = {
            "sukses": 1,
            "pesan": "User berhasil dihapus"
        }
        return jsonify(response)
    
    def loginUser(request):
        errors = []
        email = request.form.get("email")
        password = request.form.get("password")


        if not email:
            errors.append("Email wajib diisi")
        else:
            if not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b', email):
                errors.append("Format email tidak valid")


        if(password == "" or password == None):
            errors.append("Password wajib diisi")
        
        if(len(errors) == 0 ):
    
            dataLogin = User.loginUser(email = email, password=password)
            print(dataLogin)
            if(dataLogin==None):
                response = {
                    "sukses": 0,
                    "pesan": "Email atau password salah"
                }
            else:
                access_token = create_access_token(identity = email)
                nama = dataLogin['nama']
                response = {
                    "access_token" : access_token,
                    "sukses": 1,
                    "pesan": f"Selamat datang, {nama}",
                    "data": dataLogin
                }
        else:
            response = {
                "sukses": 0,
                "pesan": errors
            }
        return jsonify(response)
    
    def ubahUser(id, request):
        errors = []
        foto = ""
        telp = request.form.get('telp')
        nama = request.form.get('nama')
        reqHobi = request.form.getlist('hobi')  
        if reqHobi:
            hobi = ";".join(reqHobi)
            print(hobi)
        else:
            errors.append("Hobi wajib dipilih")
        
        if len(request.files) > 0:
            if 'foto' in request.files and request.files['foto'].filename != "":
                f = request.files['foto']
                foto = f.filename
                print(f"aa: {f.filename}")
                f.save(f"static/img/{foto}")
            else:
                foto = ""
        else:
            pass

        if not nama or nama == "":
            errors.append("Nama wajib diisi")

        if not telp or not str(telp).isnumeric() or not 8 <= len(telp) <= 12:
            errors.append("Telp wajib diisi antara 8 dan 12 angka")

        if not errors:
            User.ubahUser(nama=nama, hobi=hobi, telp=telp, foto=foto, id=id)
            response = {
                "sukses": 1,
                "pesan": f"{nama} berhasil diubah"
            }
        else:
            response = {
                "sukses": 0,
                "pesan": errors
            }
        return jsonify(response)
