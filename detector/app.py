from flask import Flask, request, render_template
import joblib

# Load model from disk
loaded_pipeline = joblib.load('models/fake_body_SVM_model.sav')
loaded_pipeline

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['text']
    result = loaded_pipeline.predict([text])
    return f'HEADLINE: {text}\n-------------------------------\nPREDICTION: This article is probably {str(result[0]).upper()}!'

if __name__=='__main__':
    app.run(debug=True)
