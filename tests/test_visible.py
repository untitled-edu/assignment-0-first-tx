"""
Visible tests - you can run them locally:
    pytest tests/test_visible.py -v
"""

from homework import get_wallet_data, STUDENT_DATA


def test_function_exists():
    """get_wallet_data must exist and be callable."""
    assert callable(get_wallet_data)


def test_student_data_has_required_fields():
    """STUDENT_DATA must contain all required keys."""
    required_keys = {"wallet_address", "tx_hash", "colleague_address", "tx_metainfo"}
    missing = required_keys - set(STUDENT_DATA.keys())
    assert not missing, f"Missing keys in STUDENT_DATA: {missing}"


def test_tx_metainfo_has_required_fields():
    """tx_metainfo must contain all required keys."""
    required_keys = {"recipient", "value_eth", "fee_eth", "block_number"}
    missing = required_keys - set(STUDENT_DATA.get("tx_metainfo", {}).keys())
    assert not missing, f"Missing keys in tx_metainfo: {missing}"


def test_get_wallet_data_returns_required_fields():
    """get_wallet_data result must contain all required keys."""
    from web3 import Web3

    w3 = Web3(Web3.HTTPProvider("https://rpc.sepolia.org"))
    result = get_wallet_data(w3, STUDENT_DATA)
    assert isinstance(result, dict), "get_wallet_data must return a dict"

    required_keys = {"balance_wei", "balance_eth", "tx", "tx_value_eth"}
    missing = required_keys - set(result.keys())
    assert not missing, f"Missing keys in result: {missing}"
