from src.services.service import ask

def pretty_print(result):
    if result.get("status") == "error":
        print(f"  ERROR: {result.get('message')}")
        return

    print(f"\nRESULTS FOR: {result.get('search_query', 'Unknown').upper()}")
    
    generations = result.get("generations", {})
    
    for gen, data in generations.items():
        print(f"\n" + "="*30)
        print(f" GENERATION: {gen}")
        print("="*30)

        print("\n ENGINES:")
        for eng in data.get("engines", []):
            print(f"  • {eng['model']} ({eng['engine']}) - {eng['power']} HP")

        print("\n TRANSMISSIONS:")
        trans = data.get("transmission", {})
        for t_type, t_list in trans.items():
            print(f"  [{t_type.capitalize()}]")
            for t in t_list:
                print(f"    - {t['type']} ({t['speeds']} speeds)")

        best = data.get("best_engine")
        if best:
            print("\n RECOMMENDATION:")
            if isinstance(best, dict) and "model" in best:
                print(f"  ★ {best['model']}: {best['reason']}")
            elif isinstance(best, dict): # Dla wielu paliw
                for fuel, info in best.items():
                    print(f"  ★ {fuel.upper()}: {info['model']} - {info['reason']}")

def main():
    print("Welcome to the BMW Technical Database!")
    print("You can search by model (E46), series (X5), or category (Series 3).")
    print("Type 'exit' to quit.")

    while True:
        query = input("\nAsk: ")
        if query.lower().strip() == "exit": break
        
        result = ask(query)
        pretty_print(result)

if __name__ == "__main__":
    main()