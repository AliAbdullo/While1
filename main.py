
#for nom in royxat:
 # print(nom.upper())

#e-bozor
maxsulotlar = {}
while True:
  nom = input("Maxsulot nomini kiriting: ")
  narx = int(input(f"{nom.title()}ning narxini kiriting: "))
  maxsulotlar[nom]=narx
  savol = input("Yana maxsulot qo'shasizmi? 'xa/yo'q'  ")
  if savol== 'yo\'q':
    break
#for nomi, narxi in maxsulotlar.items():
#  print(f"{nomi.title()}nimg narxi {narxi} so'm")
  
  #foydalanuvchi
royxat= []
while True:
  buyurtma = input('Maxsulot nomini qo\'shing: ')
  royxat.append(buyurtma)
  savol = input(' Davom etasizmi ha/yo\'q ')
  if savol=="yo'q":
    break
    
while royxat:
  aloxida = royxat.pop()
  if aloxida in maxsulotlar.keys():
    narh= maxsulotlar[aloxida]
    print(f"{aloxida.title()}-{narh} so'm")
  else:
    print(f"Bu  {aloxida} yo'q!!!")