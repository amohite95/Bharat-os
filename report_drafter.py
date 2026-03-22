# 🏛️ AMLABSIN PRIVATE LIMITED: AUTO-REPORT GENERATOR
# TARGET: FAST-PAY VDPs 2026

def generate_subdomain_takeover_report(target_url, poc_url):
    report = f"""
    TITLE: Subdomain Takeover on {target_url}
    
    SUMMARY:
    The subdomain {target_url} is pointing to an unclaimed service. 
    I have successfully claimed this subdomain at {poc_url}.
    
    IMPACT:
    An attacker could host phishing pages, steal session cookies, 
    or bypass CSP policies on the main domain.
    
    STEPS TO REPRODUCE:
    1. Navigate to {target_url}
    2. Observe the service 'Not Found' error.
    3. Proof of possession is hosted at {poc_url}
    
    RECOMMENDED FIX:
    Remove the DNS CNAME record for {target_url} if not in use.
    
    REWARD CLAIMANT: amohite95@gmail.com
    ENTITY: AMLABSIN PRIVATE LIMITED
    """
    return report

if __name__ == "__main__":
    # Test the drafter
    print(generate_subdomain_takeover_report("dev-test.netflix.com", "http://amlabsin-poc.github.io"))
