import tkinter as tk
from web3 import Web3
from web3.middleware import geth_poa_middleware,construct_sign_and_send_raw_middleware
import json
from configparser import ConfigParser
import customtkinter 

customtkinter.set_appearance_mode('dark')

config = ConfigParser()
config.read('dapp\config.ini')

coin = ""
web3 = Web3(Web3.HTTPProvider("https://polygon-mumbai-pokt.nodies.app"))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
web3.middleware_onion.add(construct_sign_and_send_raw_middleware("53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"))
#abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')


abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"patientAddress","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"age","type":"uint256"},{"indexed":false,"internalType":"string","name":"medicalHistory","type":"string"},{"indexed":false,"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isActive","type":"bool"}],"name":"PatientAdded","type":"event"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_age","type":"uint256"},{"internalType":"string","name":"_medicalHistory","type":"string"},{"internalType":"uint256","name":"_lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"_isActive","type":"bool"}],"name":"addPatient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"}],"name":"getPatientData","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"patients","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"medicalHistory","type":"string"},{"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"}]')
contract_address = web3.to_checksum_address('0x666fD2bd94fE82a6bC585238Df49619056972bF8')
contract = web3.eth.contract(address=contract_address, abi=abi)

def wallet_transfer():

    def send_trasaction_xdc(to_add,private_key,value):
        nonce = web3.eth.get_transaction_count(account_xdc)

        tx = {
        'nonce': nonce,
        'to': to_add,
        'value': web3.to_wei(value, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.to_wei('50', 'gwei'),
        'chainId': 3
        }


        signed_tx = web3.eth.account.sign_transaction(tx,private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)

        try:
            re = tx_hash
        except Exception as e:
            re = e

        return e
    
    input_box = customtkinter.CTkEntry(r)
    input_box.pack()

    input_box_value = customtkinter.CTkEntry(r)
    input_box_value.pack()

    user_input = input_box.get()
    web3_xdc = Web3(Web3.HTTPProvider("https://rpc.apothem.network"))
    account_xdc = "0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd"
    private_key_xdc = "53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"

    def submit():
        customtkinter.CTkLabel(text=send_trasaction_xdc("0x38987063F38adEe8d558cE388Fee0F31D1eA893c",private_key_xdc,input_box_value.get()))
        customtkinter.CTkLabel(text=web3_xdc.eth.get_balance(account_xdc))
        customtkinter.CTkLabel(text="Transaction Successful")
    submit = customtkinter.CTkButton(r, text='Submit', width=25, command=submit)
    submit.pack()
    


def main_button():
# Create a Label object and add it to the Tk object
    label = customtkinter.CTkLabel(r, text=f'Med Life Insurance Database System')
    label.pack()
    
    coin_label = customtkinter.CTkLabel(r, text="Coin: ")
    coin_label.pack()

    def update_coin(value):
        global web3, contract ,gpp
        coin = value
        coin_label.configure(text="Current Chain: " + coin)
        if coin=="Polygon":
            print("Polyy")
            web3 = Web3(Web3.HTTPProvider("https://polygon-mumbai-pokt.nodies.app"))
            web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            web3.middleware_onion.add(construct_sign_and_send_raw_middleware("53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"))
            #abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')


            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"patientAddress","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"age","type":"uint256"},{"indexed":false,"internalType":"string","name":"medicalHistory","type":"string"},{"indexed":false,"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isActive","type":"bool"}],"name":"PatientAdded","type":"event"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_age","type":"uint256"},{"internalType":"string","name":"_medicalHistory","type":"string"},{"internalType":"uint256","name":"_lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"_isActive","type":"bool"}],"name":"addPatient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"}],"name":"getPatientData","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"patients","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"medicalHistory","type":"string"},{"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"}]')
            contract_address = web3.to_checksum_address('0x666fD2bd94fE82a6bC585238Df49619056972bF8')
            contract = web3.eth.contract(address=contract_address, abi=abi)
            gpp =  web3.to_wei('10', 'gwei')
    
        elif coin=="CoinEx":
            print("coninnnn")
            web3 = Web3(Web3.HTTPProvider("https://testnet-rpc.coinex.net/"))
            web3.middleware_onion.inject(geth_poa_middleware, layer=0)
            web3.middleware_onion.add(construct_sign_and_send_raw_middleware("53a8ccb43b16c70d9b241af8af5887c42e2e3706552440e36af60d75423d4d33"))
            #abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"greet","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]')
            

            abi = json.loads('[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"patientAddress","type":"address"},{"indexed":false,"internalType":"string","name":"name","type":"string"},{"indexed":false,"internalType":"uint256","name":"age","type":"uint256"},{"indexed":false,"internalType":"string","name":"medicalHistory","type":"string"},{"indexed":false,"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"indexed":false,"internalType":"bool","name":"isActive","type":"bool"}],"name":"PatientAdded","type":"event"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"},{"internalType":"string","name":"_name","type":"string"},{"internalType":"uint256","name":"_age","type":"uint256"},{"internalType":"string","name":"_medicalHistory","type":"string"},{"internalType":"uint256","name":"_lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"_isActive","type":"bool"}],"name":"addPatient","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_patientAddress","type":"address"}],"name":"getPatientData","outputs":[{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"string","name":"","type":"string"},{"internalType":"uint256","name":"","type":"uint256"},{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"patients","outputs":[{"internalType":"string","name":"name","type":"string"},{"internalType":"uint256","name":"age","type":"uint256"},{"internalType":"string","name":"medicalHistory","type":"string"},{"internalType":"uint256","name":"lastCheckupTimestamp","type":"uint256"},{"internalType":"bool","name":"isActive","type":"bool"}],"stateMutability":"view","type":"function"}]')
            contract_address = web3.to_checksum_address('0x25Ace8Cc4050491dAb72b13061F8f696aA826437')
            contract = web3.eth.contract(address=contract_address, abi=abi)
            gpp= web3.to_wei('550', 'gwei')
    combobox = customtkinter.CTkComboBox(master=r,values=["Polygon", "CoinEx","XDC"], command=update_coin)
    combobox.pack()

    sidebar = tk.Canvas(r, height=50,width=200, bg='black', highlightthickness=0)
    sidebar.pack(side='left', fill='both')
    
    r.geometry('800x600')
    r.title('Counting Seconds')
    button = customtkinter.CTkButton(r, text='Stop', width=25, command=r.destroy)
    
    button_do = customtkinter.CTkButton(r, text='Do Wallet Transaction on XDC', width=25, command=wallet_transfer)
    sidebar.create_window(100, 30 + 1*60, window=button_do)

    show_form = customtkinter.CTkButton(r, text='Insert Data', width=25, command=form)
    sidebar.create_window(100, 30 + 2*60, window=show_form)

    fet_but = customtkinter.CTkButton(r, text='Fetch', width=25, command=fetch)
    sidebar.create_window(100, 30 + 3*60, window=fet_but)

    cl_bu = customtkinter.CTkButton(r, text='Clear', width=25, command=clear_frame)
    sidebar.create_window(100, 30 + 4*60, window=cl_bu)

    sidebar.create_window(100, 30 + 5*60, window=button)



account = config.get('Account_Details', 'account')
print('Account:', account)
private_key = config.get('Account_Details', 'private_key')  




entries = ["0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd"]

def clear_frame():
    for widgets in r.winfo_children():
        widgets.destroy()
    
    main_button()

def send_transaction(address,name,age,history,timestamp,active):
    
    
    tx_hash = contract.functions.addPatient(address,name,int(age),history,int(timestamp),bool(active)).transact({
        'from': "0xeA1Cc8A9C7C3b4d23F2d27fC2c0b8CFE28cc66Bd",
        'gas': 3000000,
        'gasPrice': gpp,
    })
    print("Transaction Hash:", web3.to_hex(tx_hash))
    lb = customtkinter.CTkLabel(r, text="Transaction Hash: " + web3.to_hex(tx_hash))
    lb.pack()
    lb.bind('<Control-c>', lambda _:'break')
    #print(contract.functions.greeting().call())
    try:
        tradone = customtkinter.CTkLabel(r,text=contract.functions.getPatientData(address).call())
        tradone.pack()
    except Exception as e:
        tradone = customtkinter.CTkLabel(r,text=e)
        tradone.pack()

def form():
 
    address_label = customtkinter.CTkLabel(r, text="address")
    address_label.pack()
    address_entry = customtkinter.CTkEntry(r)
    address_entry.pack()

    name_label = customtkinter.CTkLabel(r, text="name")
    name_label.pack()
    name_entry = customtkinter.CTkEntry(r)
    name_entry.pack()

    age_label = customtkinter.CTkLabel(r, text="age")
    age_label.pack()
    age_entry = customtkinter.CTkEntry(r)
    age_entry.pack()

    history_label = customtkinter.CTkLabel(r, text="history")
    history_label.pack()
    history_entry = customtkinter.CTkEntry(r)
    history_entry.pack()

    timestamp_label = customtkinter.CTkLabel(r, text="timestamp")
    timestamp_label.pack()
    timestamp_entry = customtkinter.CTkEntry(r)
    timestamp_entry.pack()

    active_label = customtkinter.CTkLabel(r, text="active")
    active_label.pack()
    active_entry = customtkinter.CTkEntry(r)
    active_entry.pack()

    entries.append(address_entry)

    def submit():
        send_transaction(address_entry.get(),name_entry.get(),age_entry.get(),history_entry.get(),timestamp_entry.get(),active_entry.get(),)
    submit = customtkinter.CTkButton(r, text='Submit', width=25, command=submit)
    submit.pack()
    #print(entries["address"].get(),entries["name"].get(),entries["age"].get(),entries["history"].get(),entries["timestamp"].get(),entries["active"].get())

def fetch():    
    for entry in entries:
        print(entry)
        result = contract.functions.getPatientData(entry).call()
        label = customtkinter.CTkLabel(r, text=result)
        label.pack()
    
r = customtkinter.CTk()




main_button()
r.mainloop()