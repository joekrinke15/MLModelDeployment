from flask import Flask, jsonify, request, render_template
import requests
import pandas as pd
import pickle
import numpy as np

app = Flask(__name__, template_folder = 'templates')

def get_dummies(data):
    categorical_vars = ['sex' , 'smoker', 'region']
    for var in categorical_vars:
        one_hot = pd.get_dummies(data[var])
        data = data.drop(var,axis = 1)
        data = data.join(one_hot)
    return(data)
    
def load_model():
    """
    Loads model and data.
    """
    global columns
    global data
    
    model = pickle.load(open('MedCostModel.pkl', 'rb'))
    data = pd.read_csv('MedCosts.csv')
    data = data.drop(columns=['charges'])
    columns = data.columns
    return(model)

@app.route("/")
def home():
    """
    Homepage for site
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    """
    input = request.form.to_dict(flat=False)
    query_df = pd.DataFrame(input, index =[0])
    combined_data = pd.concat([query_df, data])
    combined_dummies = get_dummies(combined_data)
    input_dummies = combined_dummies.iloc[0]
    pred_input = input_dummies.to_numpy().reshape(-1,1).T
    prediction = np.round(model.predict(pred_input)[0],2)
    return render_template('prediction.html', prediction_text = 'Your Predicted Medical Costs Are: ${}'.format(prediction))


@app.route('/result', methods=['POST'])
def result():
    """
    """
    input = request.json
    query_df = pd.DataFrame(input, index =[0])
    prediction = model.predict(query_df)
    return jsonify({'prediction': list(prediction)})

    
if __name__ == '__main__':
     model = load_model()
     app.run(host = '0.0.0.0', port=8080)
    
    
