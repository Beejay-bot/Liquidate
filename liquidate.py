import os
from data import walletDetails, sample_expected_data_for_full_wallet_details, sample_transfer_funds_data
from utils import request_helper

payment_processor_fee = 25
recipient_bank_code = os.getenv('RECIPIENT_BANK_CODE')
recipient_account_number = os.getenv('RECIPIENT_ACCOUNT_NUMBER')

def main():
    liquidated_wallets = []
    #store wallets ids that couldn't be liquidated due one issue or the other.
    unliquidated_wallets = []
    for data in walletDetails:
        ''' check if remaining balance is great 25, if yes transfer remanining money after 25 is deducted. This is due to the processors
        charges which is 25 naira. 
        '''
        wallet_detail = getWalletFullDetails(data['wallet_id'])
        if wallet_detail is None:
            print(f"=====> Wallet with the ID of {data['wallet_id']}  does not exist.")
            print('-----------------------------')
            unliquidated_wallets.append(data['wallet_id'])
            continue
        remainder = int(wallet_detail['wallet_amount']) - payment_processor_fee
        if wallet_detail['wallet_amount'] > payment_processor_fee and remainder > 5:
            transfer_fund(amount=remainder,
                bank_code=recipient_bank_code, 
                acct_number=recipient_account_number, 
                wallet_id=data['wallet_id']
            )
            liquidated_wallets.append(wallet_detail)
        else: 
            print(f"This wallet with the ID of {data['wallet_id']} doesn't have enough cash for it to be liquidated.")
            print('-----------------------------')
            unliquidated_wallets.append(data['wallet_id'])
    print('<==========================>')
    print(f"The total of {len(liquidated_wallets)} wallets have been liquidated.")
    print("======================")
    print(f"{len(unliquidated_wallets)} wallets IDs were not liquidated due to some issues, e.g wallet id is invalid")

    
def getWalletFullDetails(wallet_id):
    path = f'/api/v1/wallet/ngn/retrieve?wallet_id={wallet_id}'
    req = request_helper(path=path, 
    request_type='GET', 
    expected_response=sample_expected_data_for_full_wallet_details, 
    multiple_keys=True)
    return req

# create func to transfer funds
def transfer_fund(amount:int, bank_code, acct_number, wallet_id, note=None):
    path = '/api/v1/wallet/ngn/transfer'
    payload = {
        "amount": amount,
        "wallet_id": wallet_id,
        "recipient_bank_code": bank_code,
        "recipient_account_number": acct_number,
        "note": note,
    }
    req = request_helper(path=path, 
            payload=payload, 
            request_type="POST", 
            multiple_keys=False,
            expected_response=sample_transfer_funds_data)
    return req


main()

