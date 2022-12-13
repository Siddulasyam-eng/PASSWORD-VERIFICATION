from flask import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
print("*")
users=[]
passw=[]
email=[]
app=Flask(__name__,template_folder='templates')
@app.route('/')
def funn():
    return render_template("login.html")
@app.route('/login', methods=['POST','GET']) 
def fun():
     print("*")
     usr=request.form['Usr']  
     pas=request.form['pas']
     ur=users
     ps=passw
     if usr in ur:
         if pas in ps:
             print(pas,usr,ur,ps)
             if(ps[ur.index(usr)]==pas):
                 return render_template("welcome.html",name=pas)
             else:
                 return render_template("paserror.html")
         else:
             return render_template("paserror.html")
     else:
        return render_template("usrerror.html")
emaill=''
otp=''
genotp=''
@app.route("/emailop",methods=["POST","GET"])
def eeee():
    return render_template("emailvrf.html")
@app.route("/email",methods=["POST","GET"])
def ffff():
  print("*")
  try:
    global emaill
    global otp
    global email
    emaill=request.form['mail']
    if(1):       
              
            otp=str(random.randint(1111,9999))
           
            print('Mail Sent',otp)
            return render_template("otpvrf.html")
            
  except:
      print("*")
      return render_template("emailnotfound.html")
@app.route("/otpvv",methods=["POST","GET"])
def ooo():
    
    global otp
    genotp=request.form['o1']+request.form['o2']+request.form['o3']+request.form['o4']
    if(otp==genotp):
         return render_template("signup.html")
    else:
        return render_template("emailerror.html")
@app.route('/signupp', methods=['POST','GET']) 
def ee():
       return render_template("signup.html")
@app.route('/err', methods=['POST','GET']) 
def fun1():
       return render_template("login.html")
@app.route('/er', methods=['POST','GET']) 
def f():
       return render_template("signup.html")
@app.route('/signup',methods=['POST','GET'])
def fun2():
     global emaill
     usr=request.form['Usr']  
     pas=request.form['pas']
     con=request.form['con']
     ur=users
     ps=passw
     if usr=="":
         return render_template("EntterUN.html")
     if usr not in ur:
         if con=='8':
              users.append(usr)
              passw.append(pas)
              return render_template("welcome.html")
         else:
             return render_template("passentry.html")
     else:
         return render_template("exist.html") 
app.run()
