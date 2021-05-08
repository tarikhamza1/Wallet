{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess \n",
    "import json\n",
    "from dotenv import load_dotenv\n",
    "import os\n",
    "from web3 import Web3\n",
    "from bit import *\n",
    "from eth_account import Account"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "import subprocess \n",
    "import json\n",
    "import os\n",
    "from dotenv import load_dotenv\n",
    "from constants import *\n",
    "from bit import Key, PrivateKey, PrivateKeyTestnet\n",
    "from bit.network import NetworkAPI\n",
    "from bit import *\n",
    "from web3 import Web3\n",
    "from eth_account import Account"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "from constants import *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [],
   "source": [
    "w3 = Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "load_dotenv()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "mnemonic = os.getenv('mnemonic')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cannon rifle wood empower fish sing address actual report hamster master sort glance vacuum build\n"
     ]
    }
   ],
   "source": [
    "print (mnemonic)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "def derive_wallets (mnemonic, coin, numderive):\n",
    "\n",
    "    command = 'php derive -g --mnemonic=\"'+str(mnemonic)+'\" --numderive='+str(numderive)+' --coin='+str(coin)+' --format=jsonpretty' \n",
    "    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)\n",
    "    (output, err) = p.communicate()\n",
    "    return json.loads(output)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "metadata": {},
   "outputs": [],
   "source": [
    "coins = {'eth':derive_wallets(mnemonic=mnemonic,coin=ETH,numderive=3),'btc-test': derive_wallets(mnemonic=mnemonic,coin=BTCTEST,numderive=3)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "keys = {}\n",
    "for coin in coins:\n",
    "    keys[coin]= derive_wallets(os.getenv('mnemonic'), coin, numderive=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\"0xc8f2d8128cb88f7cf065a49a0c22cee301f1dc381073de40681bbb381eb4c3de\"\n",
      "\"cVseDmPmf1hH1PaPjzWumctENcqr6dQRyh8q6zXi85TJ54V56tzc\"\n"
     ]
    }
   ],
   "source": [
    "eth_privatekey = coins['eth'][0]['privkey']\n",
    "btc_privatekey = coins['btc-test'][0]['privkey']\n",
    "\n",
    "print(json.dumps(eth_privatekey, indent=4, sort_keys=True))\n",
    "print(json.dumps(btc_privatekey, indent=4, sort_keys=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "    \"btc-test\": [\n",
      "        {\n",
      "            \"address\": \"myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR\",\n",
      "            \"index\": 0,\n",
      "            \"path\": \"m/44'/1'/0'/0/0\",\n",
      "            \"privkey\": \"cVseDmPmf1hH1PaPjzWumctENcqr6dQRyh8q6zXi85TJ54V56tzc\",\n",
      "            \"pubkey\": \"021009170bf75d4f77bee4727af2922a3552bc5907904c70d63b7e6ee2c0d2ada7\",\n",
      "            \"pubkeyhash\": \"c5d8f5cfa33ff5912ecf157667f86f20f78988d3\",\n",
      "            \"xprv\": \"tprv8k8QYFfJxbzMhWtMiQpwGXVQvkcaGCwsMunYQv67JMLQhn7LXn7RiR5mhhK9sbpgc3RUZMkPFg7aLnVsQNuS8DRnUQKjsxLxV5iN5w4xcow\",\n",
      "            \"xpub\": \"tpubDGpSgfhZ6yg2ayv9c4VXfw9XVn8WRY8mwDPKhS8Qid8oYGN7AAw1tuhdsnW9aNoLweiPJ3p29w7oVMKsF2imiAnhRoeAv4cnzPdnFgfyJRD\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"mzViQHWxB5gdoVCThWQ6vTxmMDca6BaVu8\",\n",
      "            \"index\": 1,\n",
      "            \"path\": \"m/44'/1'/0'/0/1\",\n",
      "            \"privkey\": \"cU22r46zjcZxRCuNSu48BiHiYPS4dXsQTZd2yUhoynW8bZtZ313Z\",\n",
      "            \"pubkey\": \"036a6561dadf561a7abe2a4d39c426a6a21090c9c46df0e6da2fd33119f5fce70f\",\n",
      "            \"pubkeyhash\": \"d02e60836ed34e695c10af18d89b8efbe69a59a3\",\n",
      "            \"xprv\": \"tprv8k8QYFfJxbzMk9eRGgCQisWpXB9XWCvoxNCdaZ11Ptk4YhxoPRJ9uTWXK9ZJHAcYAxq3jCDfmKEJySP6DAJpvgnZNdFYF3sawpnfkrwFEvX\",\n",
      "            \"xpub\": \"tpubDGpSgfhZ6yg2dcgDAKs18HAw6CfTfY7iXfoQs53JpAYTPCDa1p7k5x8PVHoDMk8QgAmfqQeGwp1pyfrjJg6KfXK7JhdkuBWpzXKoqnc54Na\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"n45Cn8JEvoFU2XQL7hBdZVQLboxq39rYJe\",\n",
      "            \"index\": 2,\n",
      "            \"path\": \"m/44'/1'/0'/0/2\",\n",
      "            \"privkey\": \"cPf4PtvXfKDzJCH28G5S86VtSiDWHSMUKYyrp6kkAo8KmP7NpZaT\",\n",
      "            \"pubkey\": \"0280992308e633c787b1d4365be727541478cccdc35f3462cfef26d53bd74760b3\",\n",
      "            \"pubkeyhash\": \"f76c2b2d8766baa3def9f4facc21aaf3e4925d52\",\n",
      "            \"xprv\": \"tprv8k8QYFfJxbzMmqDVMnPtGdQd9G9fDUhzZuF5bc7nCW2sDRYacH94ZzyCZQqruZRUy8fTGbaurVZ2eptU5LWd19FuxoxSuzvH9YhTCA7tNdN\",\n",
      "            \"xpub\": \"tpubDGpSgfhZ6yg2fJFHFS4Ug34jiHfbNotu9Cqrt8A5cmqG3uoMEfxekVb4jYJ8AJguJe8W1yGbmMAYf2ZQBJk5GK5dGvZyGvRTTi5vtx5oLTU\"\n",
      "        }\n",
      "    ],\n",
      "    \"eth\": [\n",
      "        {\n",
      "            \"address\": \"0xbc5A3C2eF27F87bf969036a38BDc326307821D85\",\n",
      "            \"index\": 0,\n",
      "            \"path\": \"m/44'/60'/0'/0/0\",\n",
      "            \"privkey\": \"0xc8f2d8128cb88f7cf065a49a0c22cee301f1dc381073de40681bbb381eb4c3de\",\n",
      "            \"pubkey\": \"03bad0e7ae14a3cabbc97505f93f45ab2fd5a3d55ed41821c0aac53cff338dc13d\",\n",
      "            \"pubkeyhash\": \"1414a13d0a5ae8272265adb119b36d23bcd2bdf8\",\n",
      "            \"xprv\": \"xprvA3oqpiLxkxypKHYjkKo6MewEswvvffSn2rhmggf13qPjuHH3c9fWyQWKMqL38KWYpzUvkKQuGHaz8hibrcYQAi2XWH9ZcG6PcvpGLVifjgx\",\n",
      "            \"xpub\": \"xpub6GoCEDsrbLY7XmdCrML6insyRymR58AdQ5dNV54ccAvin5cC9gymXCpoD8CKkKvxo1zekaBK72aUjES3DgbqQp1kYyxondqRCfNhozVjMyN\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"0x56A8fF9eD8476F34bba24c9F148AE2579E6C1349\",\n",
      "            \"index\": 1,\n",
      "            \"path\": \"m/44'/60'/0'/0/1\",\n",
      "            \"privkey\": \"0xd3a28fcc5e557d03653add82cf4b2ec3884cb4ab36d71b81fff2eb8b8a63561e\",\n",
      "            \"pubkey\": \"02ebf9ea470b9c97759ca17add4b9825cd7c6ad8487458f78109d30f3ad87ac8d9\",\n",
      "            \"pubkeyhash\": \"19642ddc6bc9b3a10b6e511554e870dd8eb9886b\",\n",
      "            \"xprv\": \"xprvA3oqpiLxkxypMdf9g1tH344gmyS7Bdj5gZdLh8ufCxetpntA6pLhagVhJ3hWSsNd5Jjg58AT64VwPcF9N92JojvjtTLc92CCtCHcdt8Ra7z\",\n",
      "            \"xpub\": \"xpub6GoCEDsrbLY7a7jcn3RHQC1RL1Gbb6Sw3nYwVXKGmJBshbDJeMex8UpB9JuzepCeZBceguZgpuChWr2VjCRhvb7u1Ebkapy6FRsLZQ9wya7\"\n",
      "        },\n",
      "        {\n",
      "            \"address\": \"0xa1c196331D1D972A39D1b69809D0E359a9B09A59\",\n",
      "            \"index\": 2,\n",
      "            \"path\": \"m/44'/60'/0'/0/2\",\n",
      "            \"privkey\": \"0x93cb6a296c5a526ecc2690a7033616fa1d056f4ab1c9d182ac9c6a6eeb27d044\",\n",
      "            \"pubkey\": \"02b5ddb0a48874470d2bb545dacefc631697108459cea2aa279ec506b6db22836c\",\n",
      "            \"pubkeyhash\": \"91b29c67b4ba228af06baed4fa1a106c882f43a1\",\n",
      "            \"xprv\": \"xprvA3oqpiLxkxypPwMyQMyj1hc4DD6TXZJbZnYPsRCwspmpTsWnBwCeUY8ibMBoC5wCNP675jvunEBAkxYMqZdtH6qndm86Qa1yURKZ3wyZ1cY\",\n",
      "            \"xpub\": \"xpub6GoCEDsrbLY7cRSSWPWjNqYnmEvww22Sw1TzfocZSAJoLfqvjUWu2LTCScUZwagH4tzxnAxxxNza6Pm6xDWZT1BF4bxVudcuYEvNsYnemYp\"\n",
      "        }\n",
      "    ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "print(json.dumps(keys, indent=4, sort_keys=True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [],
   "source": [
    "def priv_key_to_account (coin, priv_key):\n",
    "    if coin == ETH:\n",
    "        return Account.privateKeyToAccount(priv_key)\n",
    "    if coin == BTCTEST:\n",
    "        return PrivateKeyTestnet(priv_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [],
   "source": [
    "eth_account = priv_key_to_account(ETH,eth_privatekey)\n",
    "btc_account = priv_key_to_account(BTCTEST,btc_privatekey)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 75,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<eth_account.signers.local.LocalAccount object at 0x0000016E97B125C8>\n",
      "<PrivateKeyTestnet: myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR>\n"
     ]
    }
   ],
   "source": [
    "print(eth_account)\n",
    "print(btc_account)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [],
   "source": [
    "def create_tx(coin,account,recipient,amount):\n",
    "    if coin ==ETH:\n",
    "        gasEstimate = w3.eth.estimateGas(\n",
    "            {\"from\": account.address, \"to\": recipient, \"value\": amount}\n",
    "        )\n",
    "        return {\n",
    "            \"to\": recipient,\n",
    "            \"from\": account.address,\n",
    "            \"value\": amount,\n",
    "            \"gasPrice\": w3.eth.gasPrice,\n",
    "            \"gas\": gasEstimate,\n",
    "            \"nonce\": w3.eth.getTransactionCount(account.address)\n",
    "        }\n",
    "    elif coin == BTCTEST:\n",
    "        return PrivateKeyTestnet.prepare_transaction(account.address, [(recipient, amount, BTC)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_tx (coin, account, recipient, amount):\n",
    "    if coin =='eth':\n",
    "        trxns_eth = create_tx(coin,account, recipient, amount)\n",
    "        sign_trxns_eth = account.sign_transaction(trxns_eth)\n",
    "        result = w3.eth.sendRawTransaction(sign_trxns_eth.rawTransaction)\n",
    "        print(result.hex())\n",
    "        return result.hex()\n",
    "    else:\n",
    "        trxns_btctest= create_tx(coin,account,recipient,amount)\n",
    "        sign_trxns_btctest = account.sign_transaction(trxns_btctest)\n",
    "        from bit.network import NetworkAPI\n",
    "        NetworkAPI.broadcast_tx_testnet(sign_trxns_btctest)       \n",
    "        return sign_trxns_btctest"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### BTC TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'{\"unspents\":[{\"amount\":100000,\"confirmations\":0,\"script\":\"76a914c5d8f5cfa33ff5912ecf157667f86f20f78988d388ac\",\"txid\":\"bd43afc8b1de2b5e761ecfa7b9d44eff204cf8c988d7bfd58f385ad2300833ce\",\"txindex\":0,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false,\"sequence\":4294967295},{\"amount\":1198871,\"confirmations\":0,\"script\":\"76a914c5d8f5cfa33ff5912ecf157667f86f20f78988d388ac\",\"txid\":\"bd43afc8b1de2b5e761ecfa7b9d44eff204cf8c988d7bfd58f385ad2300833ce\",\"txindex\":1,\"type\":\"p2pkh\",\"vsize\":148,\"segwit\":false,\"sequence\":4294967295}],\"outputs\":[[\"myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR\",100000],[\"myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR\",1160723]]}'"
      ]
     },
     "execution_count": 92,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# create BTC transaction\n",
    "create_tx(BTCTEST,btc_account,\"myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR\", 0.001)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'0100000002ce330830d25a388fd5bfd788c9f84c20ff4ed4b9a7cf1e765e2bdeb1c8af43bd000000006b483045022100a2429043c221c1171778ce01e72131d9d962b4a8600ac9d7e5192544e01f32dc02202a1aebf2fe0ea11f6b2dc4f8ade48969efb7e4d7a961eef1f25198767a5ef5000121021009170bf75d4f77bee4727af2922a3552bc5907904c70d63b7e6ee2c0d2ada7ffffffffce330830d25a388fd5bfd788c9f84c20ff4ed4b9a7cf1e765e2bdeb1c8af43bd010000006a473044022047dee02bfcdceb190e5f689ce8facc3cec508b6f0db1b8fac8d5715d632d1a7502207f0e850558c0fb36627755352dc8022264a2a994fa57962d48eb0c9d083708d40121021009170bf75d4f77bee4727af2922a3552bc5907904c70d63b7e6ee2c0d2ada7ffffffff02a0860100000000001976a914c5d8f5cfa33ff5912ecf157667f86f20f78988d388ac13b61100000000001976a914c5d8f5cfa33ff5912ecf157667f86f20f78988d388ac00000000'"
      ]
     },
     "execution_count": 93,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#send BTC transaction\n",
    "send_tx(BTCTEST,btc_account,'myZ5KWADGjMnpfGQHGyZ9qU5MWqchdXhXR',0.001)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### ETH TEST"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "metadata": {},
   "outputs": [],
   "source": [
    "from web3.middleware import geth_poa_middleware\n",
    "\n",
    "w3.middleware_onion.inject(geth_poa_middleware, layer=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 95,
   "metadata": {},
   "outputs": [],
   "source": [
    "from web3 import Web3, HTTPProvider"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "w3 = Web3(Web3.HTTPProvider(\"http://127.0.0.1:8545/0x5619d0cce54919511eb9f3b678de07bd346044acee0bdd6cdf4497ba45e03f81\"))"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
