from flask import Flask, render_template, request
#import pickle
import numpy as np
from joblib import dump, load

model = model = load('selected_model.joblib')

app = Flask(__name__)



@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data = request.form['a']
    #pred = model.predict(data)
    pred_industry = model.predict([data])
    return render_template('predict.html', data=pred_industry)

@app.route('/predict', methods=['POST'])
def api_prediction(url, form_data):
    r = requests.post(url, data=form_data)
    htmlText = r.text
    soup = BeautifulSoup(htmlText, 'html.parser')
    print(soup.find('h2').text)
    print(soup.find_all('h1')[-1].text)

def main():
    """Run the app."""
    app.run(host='0.0.0.0', port=8000)  # nosec
    
if __name__ == "__main__":
    app.run(debug=True)
    

    

