import os
from flask import Flask,render_template
from flask import request
from flask import redirect
from flask import jsonify
from models import *
import csv


app = Flask(__name__,
            template_folder = "./templates")

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:123@localhost:5432/swift'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/sgsidepost',methods=['POST'])
def sgSide():
    with open('/home/saurabh/upwork/work/myProject/SgOneToOneMatchingSampleData/sg.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            A = row[0]
            B = row[1]
            C = row[2]
            D = row[3]
            E = row[4]
            F = row[5]
            G = row[6]
            H = row[7]
            I = row[8]
            J = row[9]
            K = row[10]
            L = row[11]
            M = row[12]
            N = row[13]
            O = row[14]
            P = row[15]
            Q = row[16]
            sgSideModel.insert(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q)
    return "good"

@app.route('/cpsidepost',methods=['POST'])
def cpSide():
    with open('/home/saurabh/upwork/work/myProject/SgOneToOneMatchingSampleData/cp.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        count=0
        for row in reader:
            A = row[0]
            B = row[1]
            C = row[2]
            D = row[3]
            E = row[4]
            F = row[5]
            G = row[6]
            H = row[7]
            I = row[8]
            J = row[9]
            K = row[10]
            L = row[11]
            M = row[12]
            N = row[13]
            O = row[14]
            P = row[15]
            Q = row[16]
            cpSideModel.insert(A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q)
            count = count+1
    return str(count)

@app.route('/matchcase',methods=['GET'])
def matchCase():
    # import pdb;pdb.set_trace()
    data = sgSideModel.query.all()
    data1 = cpSideModel.query.all()
    count=0
    for i in range(len(data)):
        if(data[i].partyA==data1[i].partyB and data[i].partyB==data1[i].partyA and 
            data[i].isdaDate==data1[i].isdaDate and data[i].contractdate==data1[i].contractdate and 
            data[i].valueDate==data1[i].valueDate and data[i].exchangeRate==data1[i].exchangeRate and
            data[i].buyQuant==data1[i].sellQuant and data[i].sellQuant==data1[i].buyQuant and data[i].settlement1==data1[i].settlement2
            and data[i].settlement2==data1[i].settlement1):
                    count = count+1
    
    return str(count)

if __name__ == "__main__":
    app.run()
