from flask import Flask, render_template,url_for,redirect,request
import psycopg2 #not error

app=Flask(__name__)



conn = psycopg2.connect(
            host='database-1.cpa8i48eqilt.ap-south-1.rds.amazonaws.com',
            port='5432',
            dbname='stu_projects',
            user='postgres',
            password='postgres'
        )
cur=conn.cursor()
       
@app.route('/')
def first():
    return redirect(url_for("home"))

@app.route('/home')
def home():
    return render_template("home.html")
 
@app.route('/form', methods=['POST','GET'])
def form():
    if request.method == 'POST':
        try:
        
            name= request.form.get("sname")
            sphone_number= request.form.get("sphone_number")
            scity= request.form.get("scity")
            cur.execute("create table std_database(sid serial primary key,sname varchar(50),sphone_number varchar(12),scity varchar(50))")
            cur.execute("INSERT INTO std_database (sname, sphone_number, scity) VALUES (%s, %s, %s)", (name,sphone_number, scity))
           
            conn.commit()

        except Exception as ex:
            return str(ex)  
        return redirect(url_for('showRecord'))

@app.route('/deleteRecord', methods=['POST'])
def delete():
    id=request.form.get('id')
    cur.execute(f"delete from std_database where sid='{id}'")
    conn.commit()
    return redirect(url_for('showRecord'))

@app.route('/update', methods=['POST'])
def update():
     id=request.form.get('udid')
     cur.execute(f"SELECT *FROM std_database WHERE sid='{id}'")
     db1=cur.fetchall()
     conn.commit()
     return render_template('form.html',db1=db1)

@app.route('/profile_record', methods=['POST'])
def profile():
     id=request.form.get('udid')
     cur.execute(f"SELECT *FROM std_database WHERE sid='{id}'")
     db1=cur.fetchone()
     conn.commit()
     return render_template('profile.html',db1=db1)



@app.route('/updateRecord', methods=['POST'])
def updateRecord():

    id=request.form.get('udid')
    name= request.form.get("sname")
    sphone_number= request.form.get("sphone_number")
    scity= request.form.get("scity")
    cur.execute(f"UPDATE std_database set sname='{name}', sphone_number='{sphone_number}', scity='{scity}' WHERE sid='{id}';")
    return redirect(url_for('showRecord'))


@app.route('/showRecord')
def showRecord():
     cur.execute("SELECT*FROM std_database")
     db=cur.fetchall()
     return render_template('display.html',db=db)
	

if __name__=='__main__':  
    app.run(debug=True,host='0.0.0.0',port=5000)