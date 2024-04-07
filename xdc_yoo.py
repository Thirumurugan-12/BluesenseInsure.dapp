import json
from web3 import Web3
from web3.middleware import geth_poa_middleware,construct_sign_and_send_raw_middleware

web3 = Web3(Web3.HTTPProvider("https://rpc.apothem.network"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3.middleware_onion.add(construct_sign_and_send_raw_middleware("53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"))
#abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')

abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"address","name":"_insured","type":"address"},{"internalType":"uint256","name":"_claimAmount","type":"uint256"}],"name":"approveClaim","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_claimAmount","type":"uint256"}],"name":"claimInsurance","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_insured","type":"address"},{"internalType":"uint256","name":"_premiumAmount","type":"uint256"},{"internalType":"uint256","name":"_coverageAmount","type":"uint256"},{"internalType":"uint256","name":"_premiumDueDate","type":"uint256"},{"internalType":"uint256","name":"_claimCooldownPeriod","type":"uint256"}],"name":"enrollPolicy","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getContractBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_insured","type":"address"}],"name":"getPolicyDetails","outputs":[{"internalType":"bool","name":"","type":"bool"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"insurer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"payPremium","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"policies","outputs":[{"internalType":"bool","name":"isActive","type":"bool"},{"internalType":"uint256","name":"premiumAmount","type":"uint256"},{"internalType":"uint256","name":"coverageAmount","type":"uint256"},{"internalType":"uint256","name":"premiumDueDate","type":"uint256"},{"internalType":"uint256","name":"lastClaimDate","type":"uint256"},{"internalType":"uint256","name":"claimCooldownPeriod","type":"uint256"}],"stateMutability":"view","type":"function"},{"stateMutability":"payable","type":"receive"}]')
contract_address = web3.to_checksum_address('0x89aF5e435d7f68DC049E0319417e82a085F03F36')
contract = web3.eth.contract(address=contract_address, abi=abi)

tx_hash = contract.functions.enrollPolicy("0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd",1,1,1,1).transact({
    'from': "0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd",
    'gas': 2000000,
    'gasPrice': web3.to_wei('1000', 'gwei'),
})

print("Transaction Hash:", web3.to_hex(tx_hash))
print("Transaction Receipt:", web3.eth.wait_for_transaction_receipt(web3.to_hex(tx_hash)))
#print(contract.functions.greeting().call())
#print(contract.functions.getPatientData("0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd").call())
print(contract.functions.getPolicyDetails("0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd").call())

