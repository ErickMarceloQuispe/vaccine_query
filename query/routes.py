from query import app
from flask import render_template
from flask import request
import mysql.connector
from query.forms import Form
from flask_recaptcha import ReCaptcha
#from market.models import Item

DOCUMENT_TYPES={
    "DNI":8,
    "Carnet de Extranjería":9,
    "Certificado Nacido Vivo":9,
    "DIE":8,
    "Pasaporte":9,
    "Sin Documento":15,
}
recaptcha = ReCaptcha(app=app)
@app.route("/")
@app.route("/home")
def home_page():
    form=Form()
    return getHomePage()

@app.route("/query",methods=['POST'])
def market_page():
    #items=Item.query.all()
    obj=request.form.get("doc_opt")
    if(request.form.get("g-recaptcha-response")==""):
        print(str(request.form.get("birth")))
        return getHomePage("Porfavor, resuelva el Captcha")
    elif(length_validation(request.form)==False):
        return getHomePage("El número de documento no coincide con el tipo de documento")
    else:
        data=getInfoDatabase(request.form)
        if(data==None):
            return getHomePage("Coincidencia no encuentrada en la base de datos")
        else:
            return render_template("market.html",obj=data)

def getInfoDatabase(form_obj):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd = "1234",
        auth_plugin='mysql_native_password'
    )
    my_cursor = mydb.cursor()
    my_cursor.execute("SELECT nombres,apellido_paterno,apellido_materno FROM test.doc WHERE tipo_documento='{0}' AND numero_documento={1} AND fecha_nacimiento='{2}'".format(form_obj.get("doc_typ"),form_obj.get("doc_num"),str(form_obj.get("birth"))))

    for db in my_cursor:
        return db[0]+", "+db[1]+" "+db[2]

    return None

def length_validation(form_obj):
    correct_length=len(form_obj.get("doc_num"))==DOCUMENT_TYPES[form_obj.get("doc_typ")]
    return correct_length

def getHomePage(msg=""):
    form=Form()
    return render_template("home.html",type_map=DOCUMENT_TYPES,form=form,msg=msg)