from pymongo import MongoClient
coneccion=MongoClient("localhost")
db = coneccion["RGB-computer"]
col1=db["motores"] 
col2=db["clientes"]
col3=db["parches"]
col4=db["Desarrolladores"]
print(db.list_collection_names())
class desarrollador:
    def __init__(self,rut,clave,nombre):
        self.rut=rut
        self.clave=clave
        self.nombre=nombre
    def agregar_desarrollador(self):
        self.rut=str(input("Ingrese el rut del desarollador"))
        a=str(input("ingrece Nueva clave"))
        
        self.clave=a
        self.nombre=str(input("Ingrese nombre del desarrollador"))
class motor:
    def __init__(self,Version,Dimension,Precio):
        self.Version=Version
        self.Dimension=Dimension
        self.Precio=Precio
    
    def agregar_motor(self):
        self.Version=str(input(" Ingrese Version del motor grafico "))
        self.Dimension=str(input(" Ingrese Dimensionalidad del motor grafico "))
        self.Precio=int(input(" Ingrese Precio del motor grafico "))  
class Parche:
    def __init__(self,version,mejoras,precio):
        self.version=version
        self.mejoras=mejoras
        self.precio=precio
    
    def agregar_parche(self):
        self.version=str(input(" Ingresa version del parche " ))
        a=int(input("cuantas mejoras tiene el parche"))
        self.mejoras=[]
        for i in range(0,a):
            print("Ingrese la mejora numero ",int(i + 1) )
            x=input()
            self.mejoras.append(x)
            print(" Mejora ingresada ")
        self.precio=int(input("Ingrece el precio del el parche"))
class cliente:
    def __init__(self,rut,nombre_usuario,metodo_de_pago,carrito):
        self.rut=rut
        self.nombre_usuario=nombre_usuario
        self.metodo_de_pago=metodo_de_pago
        self.carrito=carrito
    
       
    def agregar_cliente(self):
        self.rut= str(input("ingrese rut del cliente "))
        self.nombre_usuario = str(input("ingrese el Nombre de usuario"))
        t=int(input("ingrese la cantidad de medios de pago"))
        self.metodo_de_pago=[]
        for i in range(0,t):
            y=str(input(" ingrese  metodo de pago "))
            self.metodo_de_pago.append(y)
        self.carrito=[]
motor1=motor("","",0)
parche1=Parche("",[],0)
cliente1=cliente("","",[],[])
desarrollador1=desarrollador("","","")
def agregar():
    print("***********")
    print(0 ," Motor ")
    print(1 ," Parche")
    print(2 ," Cliente" )
    print(3, " Desarrollador")
    print("***********")
    
    opcion= str(input("ingrese su opcion "))
    if opcion== "0":
        motor1.agregar_motor()
        a=motor1.__dict__
        col1.insert_one(a)
    elif opcion=="1":
        parche1.agregar_parche()
        a=parche1.__dict__
        col3.insert_one(a)
    elif opcion=="2":
        cliente1.agregar_cliente()
        a=cliente1.__dict__
        col2.insert_one(a)
    elif opcion=="3":
        desarrollador1.agregar_desarrollador()
        a=desarrollador1.__dict__
        col4.insert_one(a)
    else:
        print("Error De tipeo, Intentelo nuevamente mas tarde")
def eliminar_motores():
    for i in col1.find({},{"_id":0}):
        
        print(i)
    x=str(input("Ingrese la version del Motor Grafico a eliminar "))
    col1.delete_one({"Version":x})
def eliminar_parches():
    for i in col3.find({},{"_id":0}):
        print(i)
    x=str(input("Ingrese Version del parche "))
    col3.delete_one({"version":x})
def eliminar_Clientes():
    for i in col2.find({},{"_id":0}):
        print(i)
    x=str(input("ingrese El rut del cliente a eliminar "))
    col2.delete_one({"rut":x})
def eliminar_desarrollador():
    for i in col4.find({},{"_id":0}):
        print(i)
    x=str(input("ingrese El rut del Desarrollador a eliminar "))
    col4.delete_one({"rut":x})
def mostrar():
    print("***********")
    print(0 ," Motor ")
    print(1 ," Parche")
    print(2 ," Cliente" )
    print(3 ," Desarrollador")
    print("***********") 
    opcion= str(input("ingrese su opcion "))
    if opcion== "0":
       for i in col1.find({},{"_id":0}):
           print(i)
    elif opcion=="1":
        for i in col3.find({},{"_id":0}):
            print(i)
    elif opcion=="2":
        for i in col2.find({},{"_id":0}):
            print(i)
    elif opcion=="3":
        for i in col4.find({},{"_id":0}):
            print(i)
    else:
        print("Error De tipeo, Intentelo nuevamente mas tarde")
def actualizar():
    print("***********")
    print(0 ," Motor ")
    print(1 ," Parche")
    print(2 ," Cliente")
    print(3 ," Desarrollador")
    print("***********") 
    opcion= str(input("ingrese su opcion "))
    if opcion== "0":
        for i in col1.find({},{"_id":0}):
           print(i)
        x=str(input("Ingrese la version del motor a actualizar "))
        print("si va a cambiar solo un parametro, el parametro original escribalo como originalmente esta")
        a=str(input("Ingrese el cambio en la Dimecionalidad"))
        b=int(input("Ingrese el nuevo precio"))
        col1.update_one({"Version":x},{"$set":{"Dimension":a,"Precio":b}})
    elif opcion=="1":
        for i in col3.find({},{"_id":0}):
            print(i)
        x=str(input("Ingrese a version del parche a actualizar"))
        print("si va a cambiar solo un parametro, el parametro original escribalo como originalmente esta")
        a=[]
        mejoras=int(input("ingrece la nueva cantidad de mejoras "))
        for j in range(0,mejoras,1):
            d=str(input(" ingrese la mejora "))
            a.append(d)
        b=int(input("Ingrese el nuevo precio"))
        col3.update_one({"Version":x},{"$set":{"mejoras":a,"precio":b}})
    elif opcion=="2":
        for i in col2.find({},{"_id":0}):
            print(i)
        x=(str(input("Ingrese el rut del cliente a actualizar")))
        print("si va a cambiar solo un parametro, el parametro original escribalo como originalmente esta")
        a=str(input("Ingrese Nuevo nombre de usuario"))
        b=[]
        M_pagos=int(input("ingrese la nueva cantidad de metodos de pago"))
        for j in range(0,M_pagos,1):
            d=str(input(" Ingrese Nuevo metodo de pago"))
            b.append(d)
        c=[]
        h=[]
        C_productos=int(input("ingrese la cantidad de producto que comprara el cliente "))
        for k in range(0,C_productos,1):
            g=str(input("ingrese el producto "))
            for i in col1.find({"Version":g},{"_id":0}):
                c.append(i)
            for j in col3.find({"version":g},{"_id":0}):
                h.append(j) 
        d=h+c
        col2.update_one({"rut":x},{"$set":{"nombre_usuario":a,"metodo_de_pago":b,"carrito":d}})
    elif opcion=="3":
        for i in col4.find({},{"_id":0}):
            print(i)
        x=(str(input("Ingrese el rut del Desarollador a actualizar")))
        print("si va a cambiar solo un parametro, el parametro original escribalo como originalmente esta")
        a=str(input("Ingrese Nuevo nombre del Desarrollador"))
        b=str(input("Ingrese la Nueva Clave"))
        
        col4.update_one({"rut":x},{"$set":{"nombre":a,"clave":b}})
    else:
        print("Error De tipeo, Intentelo nuevamente mas tarde")
def eliminar():
    print("***********")
    print(0 ," Motor ")
    print(1 ," Parche")
    print(2 ," Cliente")
    print(3 ," Desarrollador")
    print("***********") 
    opcion= str(input("ingrese su opcion "))
    if opcion=="0":
        eliminar_motores()
    elif opcion=="1":
        eliminar_parches()
    elif opcion=="2":
        eliminar_Clientes()
    elif opcion=="3":
        eliminar_desarrollador()
    else:
        print("Error De tipeo, Intentelo nuevamente mas tarde")
def main():
    
    eleccion="7"
    while eleccion!="10":
        print("**************")
        print(0, " agregar ")
        print(1, " mostrar ")
        print(2, " actualizar ")
        print(3, " eliminar")  
        print(9, " Salir")
        print("**************")
        eleccion=str(input(" INGRESE SU OPCION "))
        if eleccion== "0":
            agregar()
        elif eleccion=="1":
            mostrar()
        elif eleccion=="2":
            actualizar()
        elif eleccion=="3":
            eliminar()
        elif eleccion=="9":
            eleccion="10"
            print("Hasta pronto")
        else:
            print("intentelo nuevamente")
main()
