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

def get_wallet_data(w3: Web3, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Retrieve wallet balance and transaction details.

    Args:
        w3   - connected Web3 instance (Sepolia)
        data - STUDENT_DATA dictionary

    Returns a dict with keys:
        balance_wei   (int)   - wallet balance in wei
        balance_eth   (float) - wallet balance in ETH
        tx            (dict)  - full transaction data (result of w3.eth.get_transaction)
        tx_value_eth  (float) - transaction value in ETH
    """
    # YOUR CODE HERE
    pass
