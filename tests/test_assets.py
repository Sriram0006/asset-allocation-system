import pytest
from app.models.asset_store import AssetManager

def test_asset_operations():
    # Clear any existing assets for a clean test
    AssetManager.get_all().clear()
    
    # 1. Test Add
    AssetManager.add_asset("Laptop", 1200)
    assert len(AssetManager.get_all()) == 1
    
    # 2. Test View
    all_assets = AssetManager.get_all()
    assert all_assets[0]['name'] == "Laptop"
    
    # 3. Test Delete
    AssetManager.delete_asset(1)
    assert len(AssetManager.get_all()) == 0