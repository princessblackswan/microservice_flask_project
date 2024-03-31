from koneksi import db, cursor, cekDBOpen
import pymysql

class User:
    def tambahUser(nama, email, password, telp, foto, hobi):
        cekDBOpen()
        sql = f"INSERT INTO users (nama, email, password, telp, foto, hobi) VALUES('{nama}','{email}', MD5('{password}'), '{telp}', '{foto}', '{hobi}')"
        try:
            cursor.execute(sql)
            db.commit()
            print(f"{nama} berhasil ditambah")
        except pymysql.Error as e:
            print(e)

    def loginUser(email, password):
        cekDBOpen()
        sql = f"SELECT * FROM users WHERE email='{email}' AND password=MD5('{password}')"
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
            if(results == None):
                return None
            else:
                return results
        except pymysql.Error as e:
            print(e)
        
    def cekEmail(email):
        cekDBOpen()
        sql = f"SELECT * FROM users WHERE email = '{email}' "
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
            if results != None:
                return False
            else:
                return True
        except pymysql.Error as e:
            print(e)
        
    def listUser():
        cekDBOpen()
        sql = f"SELECT * from users"
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            return results
        
        except pymysql.Error as e:
            print(e)

    def detailUser(id):
        cekDBOpen()
        sql = f"SELECT * FROM users WHERE id_user = {id}"
        print(sql)
        try:
            cursor.execute(sql)
            results = cursor.fetchone()
            return results
        except pymysql.Error as e:
            print(e)

    def ubahUser(id, nama, telp, foto, hobi):
        if foto is None:
            sql = f"UPDATE users SET nama = '{nama}', telp = '{telp}', hobi = '{hobi}' WHERE id_user = {id}" 
        else:
            sql = f"UPDATE users SET nama = '{nama}', telp = '{telp}', hobi = '{hobi}', foto = '{foto}' WHERE id_user = {id}" 
        try:
            cursor.execute(sql)
            db.commit()
            print(f"{nama} berhasil diubah")
        except pymysql.Error as e:
            print(e)


    def hapusUser(id):
        sql = f"DELETE FROM users WHERE id_user={id}"
        try:
            cursor.execute(sql)
            db.commit()
            print(f"User berhasil dihapus")
        except pymysql.Error as e:
            print(e)

        