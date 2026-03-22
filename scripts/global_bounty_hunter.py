import time, datetime, os, requests

log_path = os.path.expanduser("~/Bharat-os/vault/run_logs.txt")
eth_url = "https://eth.llamarpc.com"

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

def log_strike(action):
    try:
        with open(log_path, 'a') as f:
            f.write(f"\n[{datetime.datetime.now()}] {action}")
        print(f"[{datetime.datetime.now()}] {action}")
    except Exception as e:
        pass

log_strike("SYSTEM_UPGRADE: Contract Interception Matrix Active.")

while True:
    try:
        # Fetch Latest Block Number
        block_payload = {"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}
        latest_block_hex = requests.post(eth_url, json=block_payload, headers=headers).json().get('result')
        
        if latest_block_hex:
            latest_block = int(latest_block_hex, 16)
            
            # RIP OPEN THE BLOCK: Fetch all transactions inside it
            tx_payload = {"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":[latest_block_hex, True],"id":1}
            block_data = requests.post(eth_url, json=tx_payload, headers=headers).json().get('result', {})
            
            transactions = block_data.get('transactions', [])
            contract_creations = 0
            
            # Scan transactions for Contract Deployments (where 'to' is null)
            for tx in transactions:
                if tx.get('to') is None:
                    contract_creations += 1
                    # Future: Extract the 'input' bytecode here and scan for vulnerabilities
            
            log_strike(f"BLOCK {latest_block} INTERCEPTED | TXs Scanned: {len(transactions)} | New Contracts Found: {contract_creations}")
            
    except Exception as e:
        log_strike(f"CRITICAL_ERROR: {str(e)}")
            
    time.sleep(15) # Sped up loop: Scan every 15 seconds to match Ethereum block time
