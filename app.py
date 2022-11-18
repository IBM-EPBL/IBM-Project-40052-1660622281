from flask import Flask, render_template, request
import pickle


app=Flask(__name__)

@app.route('/')
def home():
   return render_template("home.html")

@app.route('/index')
def index():
   return render_template("index.html")



@app.route('/data_predict', methods=['GET','POST']) 
def predicted():
    if request.method == 'POST':
        age= request. form['age'] 
        gender = request.form['gender']
        tb = request.form['tb']
        db = request.form['db']
        ap = request.form['ap'] 
        aa1 = request.form["aad"]
        aa2 = request.form["aa2"]
        tp = request.form["tp"]
        a = request.form['a']
        agr = request.form['agr']
        if gender =='Male':
            gender = 1
        gender = 0
        data = [[float(age),float(gender), float(tb), float(db), float(ap), float(aa1), float(aa2), float(tp),float(a),float(agr)]]
        model= pickle.load(open('liver.pkl', 'rb'))
        prediction=model.predict(data)[0]
        if (prediction==1):
            prediction='you have a liver disease problem,you must and should consult a doctor.Take care'
        else:
            prediction="you have a liver disease problem"
        return render_template ('index.html',prediction=prediction)

if __name__ == '__main__':
    app.run()