import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only once)
nltk.download('punkt')

# Large list of math Q&A pairs (truncated here for brevity, but keep full from before)
pairs = [
    # Greetings
    [r"hi|hello|hey",
     ["Hello! Ask me any math question or type 'calc' if you want to do some calculations."]],
     
    [r"what is addition ?",
     ["Addition is the process of finding the total or sum by combining two or more numbers."]],
    
    [r"what is subtraction ?",
     ["Subtraction is the operation of finding the difference between numbers by taking one away from another."]],

    [r"what is multiplication ?",
     ["Multiplication is repeated addition of the same number."]],

    [r"what is division ?",
     ["Division is splitting a number into equal parts or groups."]],


]

# Additional Q&A pairs for demo (you can add hundreds more)
extra_questions = {
    "what is an even number ?": ["An even number is an integer divisible by 2."],
    "what is an odd number ?": ["An odd number is an integer that is not divisible by 2."],
    "what is a prime number ?": ["A prime number is a number greater than 1 that has no divisors other than 1 and itself."],
    # Add all other questions you had...
}

for q, a in extra_questions.items():
    pattern = q.replace("?", r"\?")
    pairs.append([pattern, a])

# Fallback catch-all
pairs.append([r"(.*)", ["Sorry, I don't understand that. Can you try asking a different math question?"]])

# Calculator feature

def calculator():
    print("\nWelcome to the Calculator!")
    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit Calculator")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ").strip()
        if choice == '5':
            print("Exiting Calculator.\n")
            break
        if choice not in ['1','2','3','4']:
            print("Invalid choice, please select from 1-5.")
            continue
        
        try:
            num1 = float(input("Enter first number: ").strip())
            num2 = float(input("Enter second number: ").strip())
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {num1 + num2}\n")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {num1 - num2}\n")
        elif choice == '3':
            print(f"Result: {num1} * {num2} = {num1 * num2}\n")
        elif choice == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.\n")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}\n")

def chatbot():
    print("Hi! I'm CodTech Math Bot.")
    print("You can ask me math questions or type 'calc' to use the calculator.")
    print("Type 'quit' to exit.")

    chat = Chat(pairs, reflections)
    while True:
        user_input = input("> ").lower().strip()
        if user_input == 'quit':
            print("Goodbye! Have a great day.")
            break
        elif user_input == 'calc':
            calculator()
        else:
            response = chat.respond(user_input)
            if response:
                print(response)
            else:
                print("Sorry, I don't understand that. Try another math question or type 'calc'.")

if __name__ == "__main__":
    chatbot()

