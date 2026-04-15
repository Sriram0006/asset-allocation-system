from flask import Flask, request, jsonify
import sys
import os

# Adds the current directory to path so imports work inside Docker
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.asset_store import AssetManager

app = Flask(__name__)

@app.route('/assets', methods=['GET'])
def view_assets():
    return jsonify(AssetManager.get_all()), 200

@app.route('/assets', methods=['POST'])
def add_asset():
    data = request.get_json()
    if not data: return jsonify({"error": "No data"}), 400
    new_asset = AssetManager.add_asset(data['name'], data['amount'])
    return jsonify(new_asset), 201

@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    if AssetManager.delete_asset(asset_id):
        return jsonify({"message": "Deleted"}), 200
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)