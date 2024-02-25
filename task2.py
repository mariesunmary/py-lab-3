def find_unique_letters(word1, word2):
    unique_letters = []
    for letter in word1:
        if letter not in word2 and word1.count(letter) == 1:
            unique_letters.append(letter)
    for letter in word2:
        if letter not in word1 and word2.count(letter) == 1:
            unique_letters.append(letter)
    return unique_letters

# Задання слів
word1 = input("Введіть перше слово: ")
word2 = input("Введіть друге слово: ")

# Знаходимо та виводимо унікальні літери
unique_letters = find_unique_letters(word1, word2)
print("Унікальні літери, які зустрічаються тільки один раз у обох словах:", unique_letters)
