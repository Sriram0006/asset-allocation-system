assets = []

class AssetManager:
    @staticmethod
    def add_asset(name, amount):
        asset = {"id": len(assets) + 1, "name": name, "amount": amount}
        assets.append(asset)
        return asset

    @staticmethod
    def get_all():
        return assets

    @staticmethod
    def delete_asset(asset_id):
        global assets
        original_len = len(assets)
        assets = [a for a in assets if a['id'] != asset_id]
        return len(assets) < original_len