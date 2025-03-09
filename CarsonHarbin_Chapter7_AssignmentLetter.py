"""
Carson Harbin
Programming Exercise 7
This program allows the user to input a paragraph,
and then counts the number of sentences in the paragraph.
"""

import re

def split_into_sentences(paragraph):
    #Splits a paragraph into sentences while keeping numbers at the start of sentences.
    sentences = re.split(r'(?<=[.!?])\s+', paragraph)
    return [s.strip() for s in sentences if s]


def main():
    #Main function to take user input, split sentences, and display results.
    paragraph = input("Enter a paragraph: ")
    sentences = split_into_sentences(paragraph)

    print("\nIndividual Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"{i}. {sentence}")

    print(f"\nTotal number of sentences: {len(sentences)}")


if __name__ == "__main__":
    main()
