# Stock Market Trading Expert System

print("==================================")
print(" STOCK MARKET TRADING SYSTEM ")
print("==================================")

# Function to ask questions
def ask_question(question):
    return input(question + " ")

# Function to evaluate conditions
def evaluate(trend, fundamentals, indicators):

    return (trend.lower() == "upward" and
            fundamentals.lower() == "strong" and
            indicators.lower() == "positive")

# Function to print result
def print_result(should_buy):

    print("\n========== RESULT ==========")
  
    if should_buy:
        print("Recommendation: BUY the stock.")
    else:
        print("Recommendation: DO NOT BUY the stock.")

# Main Program
trend = ask_question(
    "What is the current market trend? (Upward/Downward):")

fundamentals = ask_question(
    "How are the company fundamentals? (Strong/Weak):")

indicators = ask_question(
    "What do technical indicators suggest? (Positive/Negative):")

should_buy = evaluate(trend, fundamentals, indicators)

print_result(should_buy)