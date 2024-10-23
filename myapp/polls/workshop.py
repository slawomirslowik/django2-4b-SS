# kolekcja = ["mama", "tata", "babcia", "dziadek", "wujek", "ciocia"]
# gen = [x for x in kolekcja if x.__contains__('a')]

# # for x in kolekcja[2::2]:
# for i in gen:
#     print(i)


x = 10

try:
    y = 10/0
except ZeroDivisionError:
    print("Nie dziel przez zero!")