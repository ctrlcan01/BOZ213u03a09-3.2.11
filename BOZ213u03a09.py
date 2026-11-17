kelime = input("Bir kelime giriniz: ")
kelime = kelime.upper()

sessiz_harfler = ""

for harf in kelime:
    if harf not in "AEIOU":
        sessiz_harfler += harf

print(sessiz_harfler)
