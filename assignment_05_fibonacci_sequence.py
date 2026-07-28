# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_fibonacci_terms():
    """Part A — Print the first N terms of the Fibonacci sequence."""
    try:
        n = int(input("How many terms? "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    a, b = 0, 1
    terms = []
    for _ in range(n):
        terms.append(a)
        a, b = b, a + b

    print("Fibonacci sequence:", " ".join(str(t) for t in terms))

   
def check_fibonacci_number():
    """Part B — Check if a given number belongs to the Fibonacci sequence."""
    try:
        num = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: please enter a valid integer.")
        return

    if num < 0:
        print(f"{num} is NOT a Fibonacci number.")
        return

    a, b = 0, 1
    is_fib = False
    # Generate terms up to (and including) num using a loop
    while a <= num:
        if a == num:
            is_fib = True
            break
        a, b = b, a + b

    if is_fib:
        print(f"{num} is a Fibonacci number.")
    else:
     print(f"{num} is NOT a Fibonacci number.")


def main():
    print_fibonacci_terms()
    print()
    check_fibonacci_number()


if __name__ == "__main__":
    main()

    def print_single_table(num):
    """Part A — Print the multiplication table for a single number, 1 to 12."""
    print(f"Multiplication Table for {num}:")
    for i in range(1, 13):
        print(f"{num}  x  {i:<2} =  {num * i}")


def print_tables_up_to_n(n):
    """Part B — Print multiplication tables for every number from 1 to N."""
    for num in range(1, n + 1):
        print_single_table(num)
        print("-" * 29)

def get_positive_int(prompt):
    """Helper — ask for input and validate it's a positive integer."""
    try:
        value = int(input(prompt))
    except ValueError:
        print("Error: please enter a valid integer.")
        return None

    if value <= 0:
        print("Error: the number must be a positive integer.")
        return None

    return value