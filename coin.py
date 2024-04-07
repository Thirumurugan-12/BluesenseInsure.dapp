import json
from web3 import Web3
from web3.middleware import geth_poa_middleware,construct_sign_and_send_raw_middleware

web3 = Web3(Web3.HTTPProvider("https://testnet-rpc.coinex.net/"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3.middleware_onion.add(construct_sign_and_send_raw_middleware("53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"))
#abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')


abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"patientAddress","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"age","type":"uint256"},{"indexed":false,"internalType":"string","name":"medicalHistory","type":"string"},{"indexed":false,"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isActive","type":"bool"}],"name":"PatientAdded","type":"event"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_age","type":"uint256"},{"internalType":"string","name":"_medicalHistory","type":"string"},{"internalType":"uint256","name":"_lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"_isActive","type":"bool"}],"name":"addPatient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"}],"name":"getPatientData","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"patients","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"medicalHistory","type":"string"},{"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"}]')
contract_address = web3.to_checksum_address('0x25Ace8Cc4050491dAb72b13061F8f696aA826437')
contract = web3.eth.contract(address=contract_address, abi=abi)

tx_hash = contract.functions.addPatient("0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd","John Doe",18,'no history',2,True).transact({
    'from': "0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd",
    'gas': 2000000,
    'gasPrice': web3.to_wei('550', 'gwei'),
})

print("Transaction Hash:", web3.to_hex(tx_hash))
#print("Transaction Receipt:", web3.eth.wait_for_transaction_receipt(web3.to_hex(tx_hash)))
#print(contract.functions.greeting().call())
print(contract.functions.getPatientData("0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd").call())

