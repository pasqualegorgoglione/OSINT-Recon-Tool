import validators
import services
import os
from dotenv import load_dotenv

load_dotenv()  
api_key = os.getenv("VT_API_KEY")

def main():
    print("Welcome in the OSINT-Automation-Recon tool: ")
    try:
        target = input("Please enter a Domain: ")
        if validators.domain(target) == True:
            print("***Start scanning on domain: " +target + " ***")          
            result = services.checkDomain(target,api_key=api_key)
            #print(result)
            #my_json = '{"my_json" : "value"}'
            last_analysis_stats =result['data']['attributes']['last_analysis_stats']
            reputation = result['data']['attributes']['reputation']
            print(f"RESULTS OF THE SCAN FOR: {target}")
            print(f"Malicious: {last_analysis_stats['malicious']}")
            print(f"Suspicious: {last_analysis_stats['suspicious']}")
            print(f"Undetected: {last_analysis_stats['undetected']}")
            print(f"Harmless: {last_analysis_stats['harmless']}")
            print(f"The reputation is: {reputation}")
        else:
            raise ValueError(f"Invalid domain: {target}")
    except Exception as e:
        print(f"Error: {e}")
        #print("The input is not a domain, please enter a domain.\nExit program...")

if __name__ == "__main__":
    main()