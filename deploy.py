from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/vyshnavi-leaf')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/vyshnavi', methods=['POST', 'GET'])
def predict():
    Contrast = float(request.form['Contrast'])
    Homogeneity = float(request.form['Homogeneity'])
    Correlation = float(request.form['Correlation'])
    Entropy	 = float(request.form['Entropy'])
    result = model.predict([[Contrast,	Homogeneity, Correlation, Entropy]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)

    			