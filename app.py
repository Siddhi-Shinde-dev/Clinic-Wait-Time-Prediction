from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
# Load the pre-trained pipeline
import joblib

model = joblib.load('wait_time_model.pkl')
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        # Create DataFrame - keys must match exactly what you trained with
        df = pd.DataFrame(data)
        
        # Get prediction
        prediction = model.predict(df)
        return jsonify({'predicted_wait_time': round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(port=5001, debug=True)