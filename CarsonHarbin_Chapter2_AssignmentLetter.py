'''
Carson Harbin
This program is written for "Programming Exercise 2"
This Program scans user inputted emails for potential spam score using a list of common spam words or phrases
and then gives the potential risk depending on how many of the words/phrases the email included.
'''

# List of common spam words/phrases
SPAM_WORDS = [
    "Opt in", "Best price", "Big bucks", "Get Yours", "Cash",
    "Order now", "Income", "Money", "No catch", "Password",
    "Free", "Bonus", "Get paid", "Giveaway", "Guaranteed",
    "Deal", "Discount", "Miracle", "Terms and conditions", "One time",
    "Prize", "Promise", "Risk-free", "Special promotion", "Act now",
    "Click here", "Instant", "Enter now", "Trial", "Winner"
]

def calculate_spam_score(email_message):
    # Checks the email message for spam words and calculates the spam score.
    spam_score = 0
    detected_words = []

    # Convert email message to lowercase for case-insensitive matching
    email_message_lower = email_message.lower()

    for word in SPAM_WORDS:
        if word.lower() in email_message_lower:
            spam_score += 1
            detected_words.append(word)

    return spam_score, detected_words

def determine_spam_likelihood(score):
    # Determines the likelihood of spam based on the spam score.
    if score == 0:
        return "Not Spam"
    elif 1 <= score <= 3:
        return "Low Risk of Spam"
    elif 4 <= score <= 6:
        return "Moderate Risk of Spam"
    elif 7 <= score <= 10:
        return "High Risk of Spam"
    else:
        return "Very High Risk of Spam"

# Main program
def main():
    email_message = input("Enter your email message: ")

    # Calculate spam score
    spam_score, detected_words = calculate_spam_score(email_message)

    # Determine spam likelihood
    spam_likelihood = determine_spam_likelihood(spam_score)

    # Display results
    print("\n--- Spam Analysis Result ---")
    print(f"Spam Score: {spam_score}")
    print(f"Likelihood: {spam_likelihood}")

    if detected_words:
        print("Spam Triggers Found:", ", ".join(detected_words))
    else:
        print("No spam words detected.")

# Run the program
if __name__ == "__main__":
    main()
