import requests
import os
import time

ACCESS_TOKEN = None
CERBY_SUBDOMAIN = None
INPUT_METHOD = None
CONFIGURED = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def set_access_token():
    global ACCESS_TOKEN
    while ACCESS_TOKEN is None or len(ACCESS_TOKEN) < 1:
        print(f"\n{emoji.emojize(':key:')} Access token:")
        ACCESS_TOKEN = input()
        if len(ACCESS_TOKEN) < 0:
            print("\nThat's empty. Try again.")

def set_cerby_subdomain():
    global CERBY_SUBDOMAIN
    while CERBY_SUBDOMAIN is None or len(CERBY_SUBDOMAIN) < 1:
        print(f"\n{emoji.emojize(':globe_with_meridians:')} Cerby subdomain (e.g., 'mycompany':")
        CERBY_SUBDOMAIN = input()
        if len(CERBY_SUBDOMAIN) < 1:
            print("\nThat's empty. Try again.")

def set_input_method():
    global INPUT_METHOD
    while INPUT_METHOD is None or INPUT_METHOD not in ['id', 'file']:
        print(f"\n{emoji.emojize(':file_folder:')} Input method (type 'id' for direct input or 'file' for a text file):")
        INPUT_METHOD = input().strip().lower()
        if INPUT_METHOD not in ['id', 'file']:
            print("\nThat's not right. Choose 'id' or 'file'.")
            INPUT_METHOD = None

def is_configured():
    global ACCESS_TOKEN, CERBY_SUBDOMAIN, INPUT_METHOD
    return ACCESS_TOKEN is not None and CERBY_SUBDOMAIN is not None and INPUT_METHOD is not None

def remove_account(account_id, access_token, cerby_subdomain):
    try:
        response = requests.delete(f"https://api.cerby.com/v1/accounts/{account_id}?password=&reason=other&turnOffMfa=false", 
            headers={
                "Authorization": f"Bearer {access_token}", 
                "Cerby-Workspace": f"{cerby_subdomain}"})
        if response.status_code == 401:
            print(f"\n{emoji.emojize(':red_exclamation_mark:')} Unauthorized: Invalid access token. Please check your token and try again.")
            set_access_token()
        elif response.status_code == 404:
            print(f"\n{emoji.emojize(':white_question_mark:')} Account with ID {account_id} not found. Please check the account ID and try again.")
        elif response.status_code == 204 or response.status_code == 200:
            print(f"{emoji.emojize(':check_mark_button')} {account_id} removed successfully. Status code: {response.status_code}")
        else:
            print(f"\nFailed to remove account. Status code: {response.status_code}, Message: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"\nAn error occurred while trying to remove the account: {e}")

if __name__ == "__main__":
    print("----- Cerby Account Removal Tool -----")
    print(f"This tool allows you to remove accounts from Cerby using the API import emoji {emoji.emojize(':rocket:')}")

    while not is_configured():
        set_access_token()
        set_cerby_subdomain()
        set_input_method()

    print(f"\n{emoji.emojize(':sparkle:')} Configuration complete!")
    time.sleep(2)
    clear_console()

    if INPUT_METHOD == 'id':
        while True:
            account_id = input("\nEnter an account ID to remove:")
            remove_account(account_id, ACCESS_TOKEN, CERBY_SUBDOMAIN)
    elif INPUT_METHOD == 'file':
        print(f"\n {emoji.emojize(':ok')} Great choice! Ensure your text file contains one account ID per line.")
        file_path = input("\nEnter the path to the text file: ")
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    account_id = line.strip()
                    if account_id:
                        remove_account(account_id, ACCESS_TOKEN, CERBY_SUBDOMAIN)
        except FileNotFoundError:
            print(f"\text file not found: {file_path}")
        except Exception as e:
            print(f"\nAn error occurred while processing the text file: {e}")
    else:
        print("\nInvalid input method. Please type 'id' or 'file'.")
