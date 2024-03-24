# Заменить символ в строке

# str1 = Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования.
# str2 = Я изучаю Puthon. Мне нравиться Puthon. Puthon очень интересный язык программирования.
"""Воспользуемся методом replace. С помощью этого метода можно заменить как целое слово, так и букву. Так как в задании
требовалось заменить букву, лучшем решением будет решение2, но по заданию также требовалось создать пустую строку внутри
функции, пройтись в цикле по всем элементам str1 и проверить: если элемент текущий строки имеет значение буквы "N",
то мы его заменим на "P", иначе перезапишем новую строку, затем из функции вернуть новую строку. Верно решение3"""


# test1
# str1 = "Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования."
# str2 = str1.replace("Nuthon", "Puthon")
# print(str2)

# # решение2
# str1 = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
# str2 = str1.replace("N", "P")
# print(str2)
# # str3 = str2.replace("u", "y")
# # print(str3)

def replace_char(str1, old_char, new_char):
    new_str = ""
    for char in str1:
        if char == old_char:
            new_str += new_char
        else:
            new_str += char
    return new_str


str1 = "Я изучаю Nuthon. Мне нравиться Nuthon. Nuthon очень интересный язык программирования."
str2 = replace_char(str1, "N", "P")
# str3 = replace_char(str2, "u", "y")
print(str2)
# print(str3) # довожу "до ума"
