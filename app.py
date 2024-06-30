from flask import Flask, render_template, request
import requests

# app = Flask(__name__)
app=Flask(__name__,template_folder='template')

# Replace with the API you want to call
# API_URL = 'https://newsapi.org/v2/everything?apiKey=0e37605bf8f44250ab277b16806fc93f&q=today'
API_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=0e37605bf8f44250ab277b16806fc93f'
API_URL_today = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=0e37605bf8f44250ab277b16806fc93f&q=today'

def search_news(query):
        url = f'https://newsapi.org/v2/everything?q={query}&apiKey=0e37605bf8f44250ab277b16806fc93f'
        response = requests.get(url)
        return response.json()

def author_news(author):
        url = f'https://newsapi.org/v2/everything?q={author}&apiKey=0e37605bf8f44250ab277b16806fc93f'
        response = requests.get(url)
        return response.json()


@app.route('/', methods=['GET'])
def fetch_data():
        # Call the external API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the JSON response
        data = response.json()

        # Render the data in an HTML template
        return render_template('index.html', data=data, all_class='active')

@app.route('/today', methods=['GET'])
def today():
        # Call the external API
        response = requests.get(API_URL_today)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the JSON response
        data = response.json()

        # Render the data in an HTML template
        return render_template('index.html', data=data, today='active')

@app.route('/s', methods=['GET'])
def search():
        search = request.args.get('search')
        if search:
                news_data = search_news(search)
                return render_template('index.html', data=news_data)
        
@app.route('/authors', methods=['GET'])
def authors():
        # Call the external API
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the JSON response
        data = response.json()

        # Render the data in an HTML template
        return render_template('authors.html', data=data, authors='active')

@app.route('/author', methods=['GET'])
def author():
        author = request.args.get('author')
        if author:
                news_data = author_news(author)
                return render_template('index.html', data=news_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
