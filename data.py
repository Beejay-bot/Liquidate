walletDetails = [
    {
        'wallet_id': 'c66a44bc-2d16-4ed7-b363-840175d977be'
    },
    {
        'wallet_id': '93ea705e-364d-460b-a931-90f866511969'
    },
    {
        'wallet_id': '9ada1ff7-3178-42fb-b842-2fce901caab5'
    },
    {
        'wallet_id': 'de80fe05-4e6b-4cfe-b2ca-009f0c68684c'
    },
    {
        'wallet_id': '1ca988e8-3677-4523-97bb-5760ae770baf'
    },
    {
        'wallet_id': '35eb89d2-71bd-4998-9451-e8803c6077ef'
    },
    {
        'wallet_id': '35eb89d2-71bd-4998-9451-e8803c6077ef'
    },
    {
        'wallet_id': '257529f1-bd84-4eb8-837d-425bdae59eb0'
    },
    {
        'wallet_id': 'c8a4ed30-5fb0-4e2f-8f77-bf3889e86dd0'
    },
    {
        'wallet_id': '45fe2c5c-bd59-4970-9cad-836e33217a7f'
    },
    {
        'wallet_id': '45fe2c5c-bd59-4970-9cad-836e33217a7f'
    },
    {
        'wallet_id': '806121e9-66ca-4e79-bf54-8c234f7fb3f2'
    },
    {
        'wallet_id': '4e9a6cff-b1f7-47f3-bd92-8d2636a91644'
    },
    {
        'wallet_id': '5930a8c0-87d5-46a8-8963-587787de15c7'
    },
    
]

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