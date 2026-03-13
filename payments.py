# am_labs Financial Bridge v1.0
import json

def generate_payment_link(amount, service):
    # This logic will connect to your Razorpay/Stripe API
    payload = {
        "entity": "am_labs",
        "beneficiary": "amohite95@gmail.com",
        "amount": amount,
        "currency": "INR",
        "service_tag": service,
        "payout_schedule": "Immediate to Canara Bank"
    }
    return f"https://api.am_labs.io/pay?data={json.dumps(payload)}"

print("==================================================")
print("     am_labs // GLOBAL PAYMENT GATEWAY READY     ")
print("==================================================")
print(f"SAMPLE LINK: {generate_payment_link(50000, 'Cloud_Migration')}")
