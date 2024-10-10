from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_metrics():
    # Gather system metrics
    cpu_usage = psutil.cpu_percent(interval=1)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Create a dictionary with the metrics
    metrics = {
        'cpu_usage': f"{cpu_usage}%",
        'ram_usage': f"{ram_usage}%",
        'disk_usage': f"{disk_usage}%"
    }

    # Return the metrics as JSON
    return jsonify(metrics)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
