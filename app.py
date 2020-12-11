import pandas as pd
from flask import Flask, jsonify, request, render_template
import pickle

# load model
model = pickle.load(open('model.pkl', 'rb'))

# app
app = Flask(__name__)

@app.route("/register", methods=["GET"])
def get_register():
    # flask loads register.html from templates directory
    return render_template('inputform.html')

@app.route("/register", methods=["POST"])
def post_register():
    Pclass_2 = 0
    Pclass_3 = 0
    Embarked_Q = 0
    Embarked_S = 0
    Age = request.form.get("Age")
    SibSp = request.form.get("SibSp")
    Parch = request.form.get("Parch")
    Fare = request.form.get("Fare")
    Sex_male = request.form.get("Sex_male")
    Pclass = request.form.get("Pclass")
    # Pclass_2 = request.form.get("Pclass_2")
    # Pclass_3 = request.form.get("Pclass_3")
    Embarked = request.form.get('Embarked')
    # Embarked_Q = request.form.get("Embarked_Q")
    # Embarked_S = request.form.get("Embarked_S")

    if Pclass == '2':
        Pclass_2 = 1
    elif Pclass == '3':
        Pclass_3 = 1

    if Embarked == 'Q':
        Embarked_Q = 1
    elif Embarked == 'S':
        Embarked_S = 1

    data_df = pd.DataFrame(data = [[Age,SibSp,Parch,Fare,Sex_male,Pclass_2,Pclass_3,Embarked_Q,Embarked_S]],  columns= ['Age',  'SibSp',  'Parch',  'Fare',  'Sex_male',  'Pclass_2',  'Pclass_3',  'Embarked_Q', 'Embarked_S'] )
    print(data_df)

    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)




if __name__ == '__main__':
    app.run(port = 5000, debug=True)