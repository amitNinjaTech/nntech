from flask import Flask, render_template, jsonify, request
import requests
import yaml
import logging

app = Flask(__name__)

# Load OpenAPI spec from YAML file
with open('openapi/spec.yaml', 'r') as file:
    openapi_spec = yaml.safe_load(file)

# Set up logging
logging.basicConfig(filename='app.log', level=logging.ERROR)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    starts_at = request.form.get('starts_at')
    ends_at = request.form.get('ends_at')

    if not starts_at or not ends_at:
        return jsonify({'error': 'Both start and end dates are required'}), 400

    try:
        formatted_data = retrieve_data_from_swaggerhub(starts_at, ends_at)
        return jsonify(formatted_data)
    except Exception as e:
        error_message = f'Error retrieving data: {str(e)}'
        logging.error(error_message)
        return jsonify({'error': 'An error occurred while processing your request. Please try again later.'}), 500

def retrieve_data_from_swaggerhub(starts_at, ends_at):
    url = f'https://virtserver.swaggerhub.com/luis-pintado-feverup/backend-test/1.0.0/search?starts_at={starts_at}&ends_at={ends_at}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == '__main__':
    app.run(debug=True)
