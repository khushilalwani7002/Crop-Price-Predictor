from flask import Flask, request, jsonify
import pickle
import pandas as pd
from flask_cors import CORS # This allows your HTML to talk to this Python script

app = Flask(__name__)
CORS(app) # Vital for frontend-backend communication

# 1. Load the trained model (Ensure the .pkl file is in the same folder)
model = pickle.load(open('crop_price_model.pkl', 'rb'))

# 2. Define the API route
@app.route('/predict', methods=['POST'])
def predict():
    # Get data sent from the HTML frontend
    data = request.get_json()
    
    # Extract values
    state = data['state']
    district = data['district']
    commodity = data['commodity']
    
    # Transform data into the format your model expects (Dataframe)
    # Note: Your developer will need to handle LabelEncoding for text here
    input_data = pd.DataFrame([[state, district, commodity]], 
                              columns=['State', 'District', 'Commodity'])
    
    # 3. Make Prediction
    prediction = model.predict(input_data)
    
    # 4. Send the result back to the Frontend as JSON
    return jsonify({
        'min_price': round(prediction[0][0], 2),
        'max_price': round(prediction[0][1], 2),
        'modal_price': round(prediction[0][2], 2)
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)