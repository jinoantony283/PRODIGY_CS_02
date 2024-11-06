import re

def assess_password_strength(password):
    # Define password strength criteria
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@#$%^&+=]', password) is not None
    
    # Calculate strength score
    score = 0
    if length_criteria:
        score += 1
    if upper_criteria:
        score += 1
    if lower_criteria:
        score += 1
    if number_criteria:
        score += 1
    if special_char_criteria:
        score += 1
    
    # Determine password strength
    if score == 5:
        strength = "Very Strong"
        feedback = "Your password is very strong!"
    elif score == 4:
        strength = "Strong"
        feedback = "Your password is strong, but could be improved by adding a special character."
    elif score == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding a special character or a number."
    elif score == 2:
        strength = "Weak"
        feedback = "Your password is weak. Consider adding a mix of uppercase, lowercase, numbers, and special characters."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. Please make it at least 8 characters long, with a mix of uppercase, lowercase, numbers, and special characters."
    
    # Provide feedback on the password
    return {
        'password': password,
        'strength': strength,
        'feedback': feedback
    }

# Example usage
password = input("Enter a password to assess its strength: ")
assessment = assess_password_strength(password)

print(f"Password: {assessment['password']}")
print(f"Strength: {assessment['strength']}")
print(f"Feedback: {assessment['feedback']}")
