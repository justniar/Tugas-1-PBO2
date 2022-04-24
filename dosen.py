from db import DBConnection as mydb

class Dosen:
    def __init__(self):
        self.__iddosen= None
        self.__nidn= None
        self.__nama= None
        self.__email= None
        self.__fakultas= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "NIDN:" + self.__nidn + "\n" + "Nama:" + self.__nama + "\n" + "Email" + self.__email + "\n" + "Fakultas:" + self.__fakultas 
        else:
            return self.__info

    @property
    def id(self):
        return self.__iddosen
    
    @property
    def nidn(self):
        return self.__nidn

    @nidn.setter
    def nidn(self, value):
        self.__nidn = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
    
    @property
    def fakultas(self):
        return self.__fakultas

    @fakultas.setter
    def fakultas(self, value):
        self.__fakultas = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__nidn,self.__nama,self.__email,self.__fakultas)
        sql="INSERT INTO dosen (nidn,nama,email,fakultas) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nidn,self.__nama,self.__email,self.__fakultas, id)
        sql="UPDATE dosen SET nidn=%s, nama=%s, email=%s, fakultas=%s WHERE iddosen=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBynidn(self, nidn):
        self.conn = mydb()
        val = (self.__nidn,self.__nama,self.__email,self.__fakultas, nidn)
        sql="UPDATE dosen SET nidn=%s, nama=%s, email=%s, fakultas=%s WHERE nidn=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE iddosen='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBynidn(self, nidn):
        self.conn = mydb()
        sql="DELETE FROM dosen WHERE nidn='" + str(nidn) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE iddosen='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nidn = self.result[1]                   
        self.__nama = self.result[2]                   
        self.__email = str(self.result[3])                   
        self.__fakultas = self.result[4]                 
        self.conn.disconnect
        return self.result
        
    def getBynidn(self, nidn):
        a=str(nidn)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM dosen WHERE nidn='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nidn = self.result[1]                   
            self.__nama = self.result[2]                   
            self.__email = str(self.result[3])                   
            self.__fakultas = self.result[4]                   
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nidn = ''                  
            self.__nama = ''                  
            self.__email = ''                  
            self.__fakultas = ''                 
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM dosen"
        self.result = self.conn.findAll(sql)
        return self.result

dsn = Dosen() 

# Tampilkan semua data
'''result = dsn.getAllData()
print(result)'''

# Entri data
'''dsn.nidn = '329088867'
dsn.nama = 'Supriyono'
dsn.email = 'supri@umc.ac.id'
dsn.fakultas= 'Teknik'
hasil = dsn.simpan()
print(hasil)
result = dsn.getAllData()
print(result)'''

# Cari data
'''nidn = '32908675'
hasil = dsn.getBynidn(nidn)
print(hasil)'''

# Update Data
'''nidn = '32908675'
dsn.nama = 'Dian N'
dsn.email= 'diann@umc.ac.id'
dsn.fakultas='Teknik'
hasil = dsn.updateBynidn(nidn)
print(hasil)'''

# delete data
'''nidn = '32908675'
hasil = dsn.deleteBynidn(nidn)
print(hasil)'''