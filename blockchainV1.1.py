# Initiatize Blockchain and related parameters

blockchain = []
open_transactions = []
owner = 'Nimel'

# Get last block of block chain

def get_last_blockchain_value():
    '''Returns the last value of the current blockchain.'''
    return blockchain[-1]

# Create function which updates/appends transactions to the blockchain.
# Required argument which is the transaction value
# The second argument is optional based on if there are any values currently in the blockchain.

def add_value(transaction_amount,last_transaction = [1]):
    """Append a new value as well as the last blockchain value to blockchain
    transaction_amount : The amount that should be added.
    last_transaction : The last blockchain transaction - default [[1]]
    """
    blockchain.append([last_transaction,transaction_amount])


def get_user_input(type):
    """Returns user input as a floating integer"""
    recipient = ''
    user_input = ''
    amount = 0
    if type == 'Choice':
        user_input = input('Please enter your choice : ')
    elif type == 'Tx':
        recipient = input('Please enter recipient name : ')
        amount = float(input('Please enter transaction amount : '))
    return user_input,recipient,amount

def add_trx_open(recipient,amount,owner = owner):
    trx_dict = {'sender':owner,'recipient':recipient,'amount':amount}
    open_transactions.append(trx_dict)

def verify_blockchain(blockchain):
    bc_length = len(blockchain)
    if bc_length == 0:
        message = 'Blockchain is empty'
        return message
    bc_valid = True
    for i in range(1,bc_length):
        block_index = bc_length - i
        if blockchain[block_index][0] != blockchain[block_index - 1]:
            bc_valid = False
    if bc_valid:
        message = 'Blockchain is legit'
    else:
        message = 'Blockchain has been hacked!'
    return message
        

# Add code to get user input
while True:
    print('Please provide your choice :')
    print('0 to create the first transaction in a blockchain')
    print('1 for adding a transaction to the open transactions list')
    print('2 for printing out current blockchain,block by block')
    print('Full for printing out whole blockchain')
    print('OpenTrans to print list of open transactions')
    print('Verify for verifying blockchain')
    print('3 to exit')
    user_input = get_user_input('Choice')[0]
    if user_input == '1':
        #Adding transaction
        user_input,recipient,tx_amount = get_user_input('Tx')
        add_trx_open(recipient,tx_amount)
        #add_value(tx_amount, get_last_blockchain_value())
    elif user_input == '0':
        if len(blockchain) == 0 :
            tx_amount = get_user_input('Tx')
            add_value(tx_amount)
        else:
            print('Blockchain exists. Please choose one of the other options')
    elif user_input == '2':
        for block in blockchain:
            print(block)
    elif user_input == '3':
        break
    elif user_input == 'Full':
        print(blockchain)
    elif user_input == 'Verify':
         print(verify_blockchain(blockchain))
    elif user_input == 'OpenTrans':
        print(open_transactions)
    
    if not verify_blockchain(blockchain):
        print('Block has been corrupted')
        break
