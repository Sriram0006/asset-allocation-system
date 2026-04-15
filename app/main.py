from flask import Flask, request, jsonify
from models.asset_store import AssetManager

app = Flask(__name__)

@app.route('/assets', methods=['GET'])
def view_assets():
    return jsonify(AssetManager.get_all()), 200

@app.route('/assets', methods=['POST'])
def add_asset():
    data = request.get_json()
    if not data or 'name' not in data or 'amount' not in data:
        return jsonify({"error": "Missing name or amount"}), 400
    
    new_asset = AssetManager.add_asset(data['name'], data['amount'])
    return jsonify(new_asset), 201

@app.route('/assets/<int:asset_id>', methods=['DELETE'])
def delete_asset(asset_id):
    success = AssetManager.delete_asset(asset_id)
    if success:
        return jsonify({"message": f"Asset {asset_id} deleted"}), 200
    return jsonify({"error": "Asset not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)