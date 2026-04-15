# Simple in-memory storage for demonstration
assets = []

class AssetManager:
    @staticmethod
    def add_asset(name, value):
        asset = {"id": len(assets) + 1, "name": name, "value": value}
        assets.append(asset)
        return asset

    @staticmethod
    def get_all():
        return assets

    @staticmethod
    def delete_asset(asset_id):
        global assets
        assets = [a for a in assets if a['id'] != asset_id]