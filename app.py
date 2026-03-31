import pickle
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# --- LOAD ENCODERS (The Translators) ---
le_state = pickle.load(open('le_state.pkl', 'rb'))
le_dist = pickle.load(open('le_district.pkl', 'rb'))
le_comm = pickle.load(open('le_commodity.pkl', 'rb'))

# --- LOAD MODELS (The Brains) ---
m_min = pickle.load(open('min_price.pkl', 'rb'))
m_max = pickle.load(open('max_price.pkl', 'rb'))
m_modal = pickle.load(open('modal_price.pkl', 'rb'))

@app.route('/')
def home():
    return "<h1>Crop Price Prediction API is Running!</h1><p>Send a POST request to /predict to get data.</p>"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # 1. Convert text to numbers using the encoders
    try:
        s_num = le_state.transform([data['state']])[0]
        d_num = le_dist.transform([data['district']])[0]
        c_num = le_comm.transform([data['commodity']])[0]

        market_dummy = 0 
        variety_dummy = 0
        min_p_dummy = 0
        max_p_dummy = 0
        
        inputs = [[s_num, d_num, market_dummy, c_num, variety_dummy, min_p_dummy, max_p_dummy]]

        # 2. Get 3 different predictions
        val_min = m_min.predict(inputs)[0]
        val_max = m_max.predict(inputs)[0]
        val_modal = m_modal.predict(inputs)[0]

        return jsonify({
            "min_price": val_min,
            "max_price": val_max,
            "modal_price": val_modal
        })
    except Exception as e:
        return jsonify({"error": f"Value not recognized: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)