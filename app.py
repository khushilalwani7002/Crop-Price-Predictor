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

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    
    # 1. Convert text to numbers using the encoders
    try:
        s_num = le_state.transform([data['state']])[0]
        d_num = le_dist.transform([data['district']])[0]
        c_num = le_comm.transform([data['commodity']])[0]
        
        inputs = [[s_num, d_num, c_num]]

        # 2. Get 3 different predictions
        val_min = m_min.predict(inputs)[0]
        val_max = m_max.predict(inputs)[0]
        val_modal = m_modal.predict(inputs)[0]

        return jsonify({
            "min_price": m_min,
            "max_price": m_max
            "modal_price": m_modal
        })
    except Exception as e:
        return jsonify({"error": f"Value not recognized: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)