from service import ask


def pretty_print(result):
    if not isinstance(result, dict):
        print(result)
        return

    for key, value in result.items():
        print(f"\n{key.upper()}:")

        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                print(f"  {sub_key}: {sub_value}")

        elif isinstance(value, list):
            for item in value:
                print(f"  - {item}")

        else:
            print(f"  {value}")


def main():
    print("Welcome to the BMW engine&transmission database! Type 'exit' to quit.")

    while True:
        query = input("\nAsk: ")

        if query.lower().strip() == "exit":
            break

        result = ask(query)

        print("\nResult:")
        pretty_print(result)


if __name__ == "__main__":