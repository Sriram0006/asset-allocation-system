import pytest
from models.asset_store import AssetManager

def test_asset_operations():
    # Reset storage
    AssetManager.get_all().clear()
    
    # Test Add
    AssetManager.add_asset("Server", 5000)
    assert len(AssetManager.get_all()) == 1
    
    # Test Delete
    AssetManager.delete_asset(1)
    assert len(AssetManager.get_all()) == 0