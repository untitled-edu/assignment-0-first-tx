from web3 import Web3
from typing import Dict, Any


# ============================================================
# TASK 1: FILL IN WITH YOUR DATA
# ============================================================
# 1. wallet_address      - your Sepolia address (MetaMask)
# 2. tx_hash             - hash of the transaction you sent to a colleague
# 3. colleague_address   - colleague's address (see README)
# 4. tx_metainfo         - dict with transaction details:
#      recipient          - recipient address from your transaction
#      value_eth          - ETH value sent in the transaction
#      fee_eth            - transaction fee in ETH
#      block_number       - block number the transaction was included in
# ============================================================

STUDENT_DATA = {
    "wallet_address": "0x...",
    "tx_hash": "0x...",
    "colleague_address": "0x...",
    "tx_metainfo": {
        "recipient": "0x...",
        "value_eth": 0.0,
        "fee_eth": 0.0,
        "block_number": 0,
    },
}


# ============================================================
# TASK 2: IMPLEMENT THIS FUNCTION
# ============================================================

def get_wallet_data(w3: Web3, address: str) -> Dict[str, Any]:
    """
    Retrieve wallet balance for the given address.

    Args:
        w3      - connected Web3 instance (Sepolia)
        address - Ethereum address (e.g. from STUDENT_DATA["wallet_address"])

    Returns a dict with keys:
        balance_wei  (int)   - wallet balance in wei
        balance_eth  (float) - wallet balance in ETH
    """
    # Default answer (replace with your implementation)
    return {
        "balance_wei": 0,
        "balance_eth": 0.0,
    }
