from service import ask

def main():
    print("Welcome to the BMW engine&transmission database! Type 'exit' to quit.")
    while True:
        query = input("\nAsk:")
        if query.lower().strip() == "exit":
            break
        result = ask(query)
        print("\nResult:")
        print(result)
if __name__ == "__main__":
    main()