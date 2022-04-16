import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='template')
model = pickle.load(open('model.pkl', 'rb'))   ## model.pkl / model11.pkl

@app.route('/')
def home():
    return render_template('CANCER.html')    ## Directly Redirect to html // wine.html/ cancer.html

@app.route('/predict',methods=['POST'])
def predict():                             ## sending X features on this
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]    ## int(X) we can provide float(x)  also
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('CANCER.html', prediction_text='predict {}'.format(output))  #Sending y featurename 'target'/'quality' or Cancer.html/wine.html



@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)