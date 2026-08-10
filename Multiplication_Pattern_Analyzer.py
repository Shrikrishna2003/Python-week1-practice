def multiplication_pattern_analyzer():
    try:
        n = int(input("Enter number: "))
        
        even_count = 0
        odd_count = 0

        print()
        for i in range(1, 11):
            result = n * i
            if result % 2 == 0:
                parity = "Even"
                even_count += 1
            else:
                parity = "Odd"
                odd_count += 1
            
            print(f"{n} x {i} = {result} - {parity}")

        print("\nAt the end, display:")
        print(f"Even Results: {even_count}")
        print(f"Odd Results: {odd_count}")

    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    multiplication_pattern_analyzer()