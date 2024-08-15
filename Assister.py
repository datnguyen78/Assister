import requests
import time
import random

API_URL = 'https://api.assisterr.ai/incentive/users/me/daily_points/'
BEARER_TOKEN_FILE = 'assis.txt'

def get_tokens():
    with open(BEARER_TOKEN_FILE, 'r') as file:
        tokens = [line.strip() for line in file]
    return [(f"Account {i+1}", token) for i, token in enumerate(tokens)]

def claim_daily_points(account, token):
    headers = {
        'Authorization': token
    }
    try:
        response = requests.post(API_URL, headers=headers)
        response.raise_for_status()
        print(f"\n✅ Daily points claimed successfully for {account}:")
        print(f"- Points: {response.json()['points']}")
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Error claiming daily points for {account}:")
        print(f"- Error: {e}")

def process_accounts():
    accounts = get_tokens()
    for account, token in accounts:
        claim_daily_points(account, token)
    delay = random.uniform(1, 600)  # Random delay between 1 and 600 seconds
    print(f"Waiting for {delay:.2f} seconds before processing the next account...")
    time.sleep(delay)

process_accounts()
