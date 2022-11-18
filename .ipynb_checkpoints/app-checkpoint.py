
import numpy as np
import pickle
from flask import Flask, render_template, request

# with open(r'D:\Python\Python Programming\My practice\Project\proj_DT\artifacts\dt_model.pkl','rb') as file:
#     model1 = pickle.load(file)

model = pickle.load(open('dt_model.pkl','rb'))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods= ['GET','POST'])
def predict():

    data = np.zeros(4) 

    data[0] =request.form['outlook']
    data[1] =request.form['temp']
    data[2] =request.form['humidity']
    data[3] =request.form['windy']

    result = model.predict([data])

    if result[0]==1:
        res = "Play"
    else:
        res = "Dont Play"

    return render_template('index.html',pred =res)

       
if __name__=='__main__':
    app.run()