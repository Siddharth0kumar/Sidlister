import sublist3r
import requests
from bs4 import BeautifulSoup
import pyfiglet
import sys
from tabulate import tabulate  # Import the tabulate library

def show_intro():
    intro_message = pyfiglet.figlet_format("Tool By Siddharth Kumar", font="mini", justify="center")
    intro_message = f"\033[91m{intro_message}\033[0m"
    print(intro_message)

def find_subdomains(domain):
    subdomains = set()

    try:
        url = f'https://crt.sh/?q=%.{domain}&output=json'
        response = requests.get(url)
        data = response.json()

        for entry in data:
            subdomain = entry['name_value']
            subdomains.add(subdomain)
    except Exception as e:
        print(f"Error: {e}")

    return subdomains

def main():
    try:
        show_intro()
        domain = input("Enter the domain name without protocol names (http/https): ")

        subdomains1 = sublist3r.main(domain, 40, None, None, False, False, False, None)
        subdomains2 = find_subdomains(domain)

        subdomains_combined = subdomains1.union(subdomains2)

        # Convert subdomains to a list for tabulation
        subdomains_list = [[f"{i + 1}.", subdomain] for i, subdomain in enumerate(sorted(subdomains_combined))]

        # Display subdomains in a tabular format
        print(tabulate(subdomains_list, headers=["#", "Subdomain"], tablefmt="grid"))

    except KeyboardInterrupt:
        print("\033[91mGoodbye\033[0m")
        sys.exit(0)

if __name__ == "__main__":
    main()
