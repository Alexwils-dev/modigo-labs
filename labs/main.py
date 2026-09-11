def create_greeting(recipient_name, sender_name="A Friend", closing="Best wishes"):
    return (f"Dear {recipient_name}, {closing}! From, {sender_name}.")

print(create_greeting("Ada"))