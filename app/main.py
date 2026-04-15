from flask import Flask, request, jsonify
import sys
import os

# Ensure Python can find the 'models' folder in the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.asset_store import AssetManager

app = Flask(__name__)

@app.route('/assets', methods=['GET'])
def view_assets():
    """Returns the list of assets as JSON"""
    return jsonify(AssetManager.get_all()), 200

@app.route('/assets', methods=['POST'])
def add_asset():
    """Adds a new asset via POST request"""
    data = request.get_json()
    if not data or 'name' not in data or 'amount' not in data:
        return jsonify({"error": "Invalid data. Name and amount are required."}), 400
    
    new_asset = AssetManager.add_asset(data['name'], data['amount'])
    return jsonify(new_asset), 201

@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    """Deletes an asset by ID"""
    if AssetManager.delete_asset(asset_id):
        return jsonify({"message": f"Asset {asset_id} deleted successfully"}), 200
    return jsonify({"error": "Asset not found"}), 404

if __name__ == '__main__':
    # host='0.0.0.0' allows Docker to route traffic to the container
    app.run(host='0.0.0.0', port=5000)