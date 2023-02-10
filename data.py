'''
Source of the inactive wallets. It must contain the wallet ID with the key of "wallet_id". Source could be from a DB such as 
POSTGRES, MYSQL, mongoDB etc or can even be an hardcoded thingy. e.g
walletDetails = [
     {
        'wallet_id': '339ddjjdkdkdkdkkckckc99330040'
    },
]
'''
walletDetails = []

sample_expected_data_for_full_wallet_details = {
    "entity": {
        "account_name": " ",
        "wallet_id": "string",
        "wallet_amount": int,
        "account_number": "string",
        "phone_number": "string",
        "bank_name": "bank name",
        "date_created": "timestamp",
        "account_numbers": [
            {
                "account_id": "uuid",
                "wallet_id": "string",
                "account_number": "string",
                "last_name": None,
                "first_name": None,
                "bank_name": "bank name",
                "date_created": "timestamp"
            }
        ]
    }
} 


sample_transfer_funds_data = {
    "entity": {
        "wallet_id": "uuid",
        "transaction_amount": int,
        "transaction_type": "transfer",
        "recipient_account_number": "string of uint64",
        "sender_account_number": "string of uint64",
        "transaction_remarks": "",
        "transaction_reason": None,
        "transaction_id": "uuid",
        "transaction_status": "PROCESSING",
        "date_created": "timestamp",
    }
}