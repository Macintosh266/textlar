# # # Scope of variable - o’zgaruvchining qamrovi
# # # Global Scope -
# a = 5  # global


# def d1():
#
#     print(a)
#
# d1()

# def d2():
#     global a
#     a += 1
#     print(a)
#
#
# #
# #
# d2()
#
#
# # print("a = ", a)
# #
# #
# # Local Scope -
# def f1():
#     global a
#     a = 4  # local
#     print("a = ", a)
# # #
# # #
# f1()
# print(a)
#
# #
# # Nonlocal Scope  - funksiya ichida yaratilgan o’zgaruvchi,
# # funksiya ichidagi boshqa funksiyalar(inner functions) uchun ham acessable bo’ladi
# def f1():
#     a = 4
#
#     def f2():  # inner function
#
#         print(a)  # nonlocal
#     return f2
#
# f1()
# # Global o’zgaruvchi funksiya ichida qayta yaratilsa u o’sha funksiya uchun local bo’ladi.
# a = 4
# #
# #
# # #
# #
# def f1():
#     global a
#     a = 5
#     print(a)  # local -> 5
# #
# #
# print(a)  # global -> 4
# f1()
# print(a)
# #
# # # Ichki funksiya nonlocal o’zgaruvchiga murojaat qila oladi, lekin o’zgartira olmaydi.
# # # Agar o’zgartirmoqchi bo’lsa, nonlocal so’zidan foydalanadi.
# #
def f1():
    a = 4

    def f2():  # inner function
        nonlocal a
        a += 2

    print("salom = ", a)  # -> 6
#
#
# #
# #
# f1()

#
# #
# #
# f2()  # -> ishlamaydi!
# #
# #
# # # Biz f2() ni f1() dan tashqarida chaqirsak u ishlamaydi.
# # # Agar ishlagan taqdirda ham u nonlocal bo’lgan a ni topa olmasdan xatolik berardi.
# # #
# # # Shu holatda bizga **Closures** yordamga keladi.
# # # Closures ichki funksiyani tashqaridan chaqirish imkonini va
# # # nonlocal o’zgaruvchilariga murojaat qilish imkonini beradi.
# #
# #
# # # Pythonda funksiyani biz o’zgaruvchiga tenglay olamiz,
# # # boshqa funksiyaga argument sifatida bera olamiz va funksiya ichida return qilib qaytara olamiz.
# #
# #
# def f(x):
#     def g(y):
#         return y + y
#
#     return g
# # print(f(2))
# # print(f())
# # print(f())
# #
# # #
# # #
# a = 5
# b = 1
#
# h = f(a)
# natija = h(b)
# print("natija",natija)
# #
# # # print(natija )  # Output is 1
# #
# # # yoki
# natija = f(a)(b)
# print("natija", natija)  # Output is 1
# # #
# # # Agar return g(y) desak bu ishlamaydi!
# # def f(x):
# #     def g(y):
# #         return y
# #     # return g(y)
# # # a = 5
# # # b = 1
# # # h = f(a)  # Xatolik beradi: NameError: name 'y' is not defined
# #
# # # Agar biz nonlocal o’zgaruvchidan foydalansakchi:
# def f(x):
#     z = 2
#     def g(y):
#         nonlocal z
#         z+=1
#         return z*x + y
#     return g
# a = 5
# b = 1
# h = f(a)
# print(h(b))  # Output is
# print(f(-1)(10))
# # # Chunki endi ichki funkisa g() -CLOSURE
# # # CLOSURE - tashqi funksiyaning nonlocal o’zgaruvchilarini
# ishlata olish imkoniyatiga ega ichki funksyadir.
# #
# #
def counter():
    count = 0  # Mahalliy o‘zgaruvchi (holat)

    def increment():
        nonlocal count
        count += 1
        return count



    return increment
#
# # print(counter())
# # Hisoblagich funksiyasini yaratamiz
counter1 = counter()
print("++++++",counter1())  # 1
print("++++++",counter1())  # 2
# #
counter2 = counter()
print("=========",counter2())  # 1 (yangi hisoblagich mustaqil ishlaydi)
print("=========",counter2())  # 1 (yangi hisoblagich mustaqil ishlaydi)
print("=========",counter2())  # 1 (yangi hisoblagich mustaqil ishlaydi)
print("=========",counter2())  # 1 (yangi hisoblagich mustaqil ishlaydi)
# #
# #
# #
# #
# #
# #
# #
# #
# # # Named Tuples’ning asosiy xususiyatlari
# # # Nomi bilan kirish: Har bir elementga nom orqali murojaat qilish mumkin (my_tuple.name).
# # # Tartiblangan: Tuple elementlari tartiblangan holda saqlanadi.
# # # O‘zgarmas (immutable): Named Tuples elementlarini o‘zgartirish mumkin emas.
# # # Qayta foydalanish: Strukturaviy ma’lumotlar bilan ishlash uchun moslashuvchan.
# #
# from collections import namedtuple
#
# # Named tuple yaratilishi
# Car = namedtuple('Car', ['make', 'model', 'year'])
#
# # Named tuple orqali obyekt yaratish
# my_car = Car(make='Toyota', model='Corolla', year=2020)
#
# # Elementlarga nom bilan kirish
# print(my_car.make)   # Toyota
# print(my_car.model)  # Corolla
# print(my_car.year)   # 2020
#
# # Elementlarga indeks orqali murojaat
# print(my_car[0])  # Toyota
