# Test file for Contact Management System

def run_tests():
    print("========== TEST CASES ==========\n")

    print("Test Case 1")
    print("Input: Add contact with valid details")
    print("Expected Result: Contact added successfully\n")

    print("Test Case 2")
    print("Input: Search existing contact")
    print("Expected Result: Contact details displayed correctly\n")

    print("Test Case 3")
    print("Input: Update contact information")
    print("Expected Result: Contact updated successfully\n")

    print("Test Case 4")
    print("Input: Delete contact")
    print("Expected Result: Contact removed from system\n")

    print("Test Case 5")
    print("Input: View all contacts")
    print("Expected Result: All contacts displayed in formatted output\n")

    print("----------------------------------------\n")

    print("Edge Case 1")
    print("Input: Empty name")
    print("Expected Result: Program asks to re-enter name\n")

    print("Edge Case 2")
    print("Input: Invalid phone (letters/symbols)")
    print("Expected Result: Program rejects input\n")

    print("Edge Case 3")
    print("Input: Invalid email format")
    print("Expected Result: Program asks for valid email\n")

    print("Edge Case 4")
    print("Input: Searching non-existing contact")
    print("Expected Result: No contact found message\n")


if __name__ == "__main__":
    run_tests()
