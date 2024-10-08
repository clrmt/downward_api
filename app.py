from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def get_pod_info():
    # Downward API에서 제공된 환경 변수들 가져오기
    pod_name = os.getenv('POD_NAME', 'Unknown Pod')
    node_name = os.getenv('NODE_NAME', 'Unknown Node')
    pod_namespace = os.getenv('POD_NAMESPACE', 'Unknown Namespace')
    
    return f'Pod Name: {pod_name}, Node Name: {node_name}, Pod Namespace: {pod_namespace}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

