from flask import Flask,render_template,request,send_file,send_from_directory,jsonify
import pickle
import numpy as np


app = Flask(__name__,static_folder='static',template_folder='templates')
model=pickle.load(open('model.pkl','rb+'))


@app.route('/',methods=['POST','GET'])
def main():
  if request.method=='GET':
    return render_template('index.html')



@app.route('/predict',methods=['POST','GET'])
def predict():
  if request.method=='GET':
    return render_template('index.html')
  if request.method=='POST':
    features=[float(x) for x in request.form.values()]
    print(features)
    labels=model.predict([features])
    print(labels)
    species=labels[0]
    if species==0:
    	s="It is Iris Setosa"
    elif species==1:
    	s="It is Iris VersiColor"
    else:
    	s="It is Iris Virginica"
    return s
if __name__=='__main__':
    app.run(host='0.0.0.0',port=8080)