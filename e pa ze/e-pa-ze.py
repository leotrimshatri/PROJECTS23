def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "w":
            if letter.isupper():
                translation = translation + "Ë"
            else:
                translation = translation + "ë"


        else:
            translation = translation + letter
    return translation


print(translate(input("Enter a phrase: ")))
