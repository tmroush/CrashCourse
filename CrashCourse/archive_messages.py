def send_messages(messages, sent_messages):
    """Send out a list of messages."""
    while messages:
        current_message = messages.pop()
        print(f"Sending message:\t{current_message}")
        sent_messages.append(current_message)


messages = ['How cool!', 'Well done!', "That's fantastic", 'You are a star!']
sent_messages = []
send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
