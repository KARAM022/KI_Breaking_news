from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with the API you want to call
API_URL = 'https://newsapi.org/v2/everything?apiKey=0e37605bf8f44250ab277b16806fc93f&q=dev'

@app.route('/', methods=['GET'])
def fetch_data():
        # Call the external API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the JSON response
        data = response.json()

        # Render the data in an HTML template
        return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
