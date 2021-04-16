from flask import Flask, jsonify, request
import requests
import pandas as pd
import pickle

app = Flask(__name__)
def load_model():
    """
    Loads model
    """
    model = pickle.load(open('MedCostModel.pkl', 'rb'))
    return(model)

@app.route("/")
def home():
    """
    Homepage for site
    """
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
     input = request.json
     query_df = pd.DataFrame(input, index =[0])
     prediction = model.predict(query_df)
     return jsonify({'prediction': list(prediction)})
    
if __name__ == '__main__':
     model = load_model()
     app.run(port=8080)