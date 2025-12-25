# Define function
def email_slicer():
    
    while True:
        email = input("Enter your email:").strip()
        
        # Extract username before @
        username = email[: email.index("@")]
        # Extract domain after @ (+1 means after @)
        domain = email[email.index("@")+1:]
        
        print(f"Username:{username}")
        print(f"Domain:{domain}")

# Call the function
email_slicer()

