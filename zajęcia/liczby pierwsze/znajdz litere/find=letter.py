# all_text = open('miejscowosci.txt', 'r', encoding = 'utf-8').read().split('\n')

# letter = input('Wprowadź literę: ')
# how_many = 0
# for i in all_text:
#     if i[0] == letter.upper():
#         print(i, end = ' ')
#         how_many += 1
# print(f"\nIlość słów na literę {letter}: {how_many}")

all_text = open('miejscowosci.txt', 'r', encoding = 'utf-8').read().split('\n')

letters = (
    "A", "Ą", "B", "C", "Ć", "D", "E", "Ę",
    "F", "G", "H", "I", "J", "K", "L", "Ł",
    "M", "N", "Ń", "O", "Ó", "P", "R", "S",
    "Ś", "T", "U", "W", "Y", "Z", "Ź", "Ż"
)
letter_index = 0
for i in letters:
    print(i, end = ': ')
    how_many = 0
    for j in range(letter_index,len(all_text)):
        if all_text[j][0] == i:
            how_many = how_many + 1
        else:
            letter_index = j
            break
    print(how_many)