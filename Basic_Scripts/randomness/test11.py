def get_text():
    text = input("enter the text you want to count how many vowels are there: \n")
    return text

def count(text):
    counter = 0
    vowels = 'aeiouy'
    for char in text:
        if char.lower() in vowels:
            counter += 1
    return counter

def main():
    text1 = get_text()
    print("Vowels: ",count(text1))


main()
