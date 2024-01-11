from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Load the matches data
matches = pd.read_csv("matches.csv", index_col=0)
matches["date"] = pd.to_datetime(matches["date"])

# Load the predictions data
predictions = pd.read_csv("merged.csv", index_col=0)
predictions["date"] = pd.to_datetime(predictions["date"])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/matches')
def matches_page():
    return render_template('matches.html', matches_data=matches.to_html())

@app.route('/predictions')
def predictions_page():
    return render_template('predictions.html', predictions_data=predictions.to_html())

if __name__ == '__main__':
    app.run(debug=True)
