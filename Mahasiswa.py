from db import DBConnection as mydb

class Mahasiswa:
    def __init__(self):
        self.__idmhs= None
        self.__nim= None
        self.__nama= None
        self.__fakultas= None
        self.__prodi= None
        self.__info = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def info(self):
        if(self.__info==None):
            return "NIM:" + self.__nim + "\n" + "Nama:" + self.__nama + "\n" + "Fakultas:" + self.__fakultas + "Prodi:" + self.__prodi
        else:
            return self.__info

    @property
    def id(self):
        return self.__idmhs
    
    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, value):
        self.__nim = value
    
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value
    
    @property
    def fakultas(self):
        return self.__fakultas

    @fakultas.setter
    def fakultas(self, value):
        self.__fakultas = value

    @property
    def prodi(self):
        return self.__prodi

    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
        
    def simpan(self):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__fakultas,self.__prodi)
        sql="INSERT INTO mahasiswa (nim,nama,fakultas,prodi) VALUES " + str(val) 
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
        
    def update(self, id):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__fakultas,self.__prodi, id)
        sql="UPDATE mahasiswa SET nim=%s, nama=%s, fakultas=%s, prodi=%s WHERE idmhs=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def updateBynim(self, nim):
        self.conn = mydb()
        val = (self.__nim,self.__nama,self.__fakultas,self.__prodi, nim)
        sql="UPDATE mahasiswa SET nim=%s, nama=%s, fakultas=%s prodi=%s WHERE nim=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE idmhs='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def deleteBynim(self, nim):
        self.conn = mydb()
        sql="DELETE FROM mahasiswa WHERE nim='" + str(nim) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
        
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE idmhs='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__nim = self.result[1]                   
        self.__nama = self.result[2]                                     
        self.__fakultas = self.result[3]
        self.__prodi = self.result[4]                    
        self.conn.disconnect
        return self.result
        
    def getBynim(self, nim):
        a=str(nim)
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa WHERE nim='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
            self.__nim = self.result[1]                   
            self.__nama = self.result[2]                                     
            self.__fakultas = self.result[3]
            self.__prodi = self.result[4]                
            self.affected = self.conn.cursor.rowcount
        else:
            self.__nim = ''                  
            self.__nama = ''                                   
            self.__fakultas = ''
            self.__prodi = ''                   
            self.affected = 0
            self.conn.disconnect
            return self.result

    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM mahasiswa"
        self.result = self.conn.findAll(sql)
        return self.result

mhs = Mahasiswa() 

# Tampilkan semua data
'''result = mhs.getAllData()
print(result)'''

# Entri data
'''mhs.nim = '200611152'
mhs.nama = 'Tiara Shinta Balqis'
mhs.fakultas = 'FKIP'
mhs.prodi= 'Matematika'
hasil = mhs.simpan()
print(hasil)
result = mhs.getAllData()
print(result)'''

# Cari data
'''nim = '200611152'
hasil = mhs.getBynim(nim)
print(hasil)'''

