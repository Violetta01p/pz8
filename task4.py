text = input("Введіть текст: ").strip()

if not text:
    print("Текст порожній. Спробуйте ще раз.")
else:
    lengths = [len(word) for word in text.split()]
    print("Довжини слів у рядку:")
    print(lengths)
