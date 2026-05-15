print("***********************************")
print("Stock trading expert system.")
print("***********************************")

def ask_question(question):
    return input(question+" ")

def evaluate(trend,fundamentals,indicators):
    return(trend.lower() == 'upward' and fundamentals.lower() == 'strong' and indicators.lower() == 'positive')

def print_result(should_buy):
    print("*******Result*********")
    if should_buy:

        print("Recommendation:Should buy the stock.")

    else:
        print("Recommendation:Should not buy the stock.")

trend = ask_question("What is the current market trend?(upward/downward):""\n")
fundamentals = ask_question("How are the company fundamentals?(strong/weak):""\n")
indicators = ask_question("What do technical indicators suggest?(positive/negative):""\n")

should_buy = evaluate(trend,fundamentals,indicators)
print_result(should_buy)