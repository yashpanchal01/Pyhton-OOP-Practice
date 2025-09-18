# The keys are in the order they were added
user_clicks = {
    '19:30:05': 'Clicked on Profile',
    '19:30:12': 'Viewed Photos',
    '19:30:18': 'Sent a Message' # Most recent click
}

print("--- Processing clicks from most recent to oldest ---")
# We loop through the KEYS in reverse order
for timestamp in reversed(user_clicks):
    action = user_clicks[timestamp] # Use the key to get the value
    print(f"{timestamp} -> {action}")