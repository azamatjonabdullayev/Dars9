# class Kitob:
#     def __init__(self, nom: str, author: str, sahifalar: int):
#         self.nom = nom
#         self.author = author
#         self.pages = sahifalar
#
#     def chop_et(self):
#         return f"Nomi: {self.nom}, Muallif: {self.author}, Sahifalar soni: {self.pages}"
#
# book = Kitob("Ikki eshik orasi", "O'tkir Xoshimov", 250)
# print(book.chop_et())


"""*******************************************************************"""

# class Talaba():
#     def __init__(self, ism: str, kurs: int, ):
#         self.ism = ism
#         self.kurs = kurs
#         self.baxolar = dict()
#
#
#     def baxo_qosh(self, fan, baxo):
#         self.baxolar.update({fan: baxo})
#
#     def chop_et(self):
#         return f"Ism: {self.ism}, kurs: {self.kurs}, baxolari: {self.baxolar}"
#
# s1 = Talaba("Azamat", 3)
# s1.baxo_qosh("Matematika", 121)
# print(s1.chop_et())


"""***********************************************************************"""


# class Hisob():
#     def __init__(self, mijoz: str, hisob: float):
#         self.client = mijoz
#         self.hisob = hisob
#
#     def pul_qosh(self, miqdor: float):
#         self.hisob += miqdor
#
#     def pul_yech(self, miqdor):
#         if self.hisob - miqdor < 0:
#             return f"Hisobingizda mablag' yetarli emas. Sizning hisobingiz: {self.hisob}"
#         self.hisob -= miqdor
#
#     def chop_et(self):
#         print(f"Mijoz: {self.client}, Hisob: {self.hisob}")
#
#
#
#
# a = Hisob("Azamat", 2510.61)
# a.pul_qosh(604.21)
# a.pul_yech(604.21)
# a.chop_et()


"""**************************************************************************"""