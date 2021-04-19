from flask import Flask, jsonify, request, render_template
import requests
import pandas as pd
import pickle

app = Flask(__name__)

def get_dummies(data):
    categorical_vars = ['sex' , 'smoker', 'region']
    for var in categorical_vars:
        one_hot = pd.get_dummies(data[var])
        data = data.drop(var,axis = 1)
        data = data.join(one_hot)
    print(data)
    return(data)
    
def load_model():
    """
    Loads model and data.
    """
    global columns
    global data
    
    model = pickle.load(open('MedCostModel.pkl', 'rb'))
    data = pd.read_csv('MedCosts.csv')
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
    inputs = request.form.to_dict(flat=False)
    """
    input = request.json
    query_df = pd.DataFrame(input, index =[0])
    print(query_df)
    combined_data = pd.concat([query_df, data])
    combined_dummies = get_dummies(combined_data)
    
    input_dummies = combined_dummies.iloc[0]
    print(input_dummies)
    prediction = model.predict(input_dummies)
    return render_template('index.html', prediction_text='Your Predicted Medical Costs Are $ {}'.format(output))


@app.route('/result', methods=['POST'])
def result():
    """
    inputs = request.form.to_dict(flat=False)
    """
    input = request.json
    query_df = pd.DataFrame(input, index =[0])
    prediction = model.predict(query_df)
    return jsonify({'prediction': list(prediction)})

    
if __name__ == '__main__':
     model = load_model()
     app.run(port=8080)