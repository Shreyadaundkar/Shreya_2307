# Elementary Customer Support Chatbot

print("====================================")
print("Welcome to ShopBot")
print("Type 'bye' to exit the chatbot")
print("====================================")

while True:

    user = input("\nYou: ").lower()

    # Greeting
    if user in ['hii','hi' ,'hello', 'hey']:
        print("Bot: Hello! How can I help you today?")

    # Order Tracking
    elif 'order' in user or 'track' in user:
        order_id = input("Bot: Please enter your Order ID: ")
        print(f"Bot: Your order {order_id} is currently out for delivery.")

    # Refund or Return
    elif 'refund' in user or 'return' in user:
        print("Bot: Products can be returned within 30 days of delivery.")

    # Product Information
    elif 'product' in user or 'item' in user:
        product = input("Bot: Enter product name: ")
        print(f"Bot: {product} is available in stock.")

    # Delivery Information
    elif 'delivery' in user or 'shipping' in user:
        print("Bot: Delivery usually takes 3 to 5 business days.")

    # Payment Query
    elif 'payment' in user:
        print("Bot: Please check your payment status in the Orders section.")

    # Price Query
    elif 'price' in user or 'cost' in user:
        print("Bot: Please visit our website for latest product prices.")

    # Discount Query
    elif 'discount' in user or 'offer' in user:
        print("Bot: Special discounts are available on selected products.")

    # Customer Support
    elif 'support' in user or 'help' in user:
        print("Bot: Our customer support team is available 24x7.")

    # Thank You Message
    elif 'thank' in user:
        print("Bot: You're welcome! Happy to help.")

    # Unknown Query
    elif user != 'bye':
        print("Bot: Sorry, I could not understand your query.")

    # Exit Condition
    else:
        print("Bot: Thank you for visiting ShopBot!")
        print("Bot: Have a nice day.")
        break