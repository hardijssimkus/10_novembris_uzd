# Izveidot programmu, kura prasa lietotâjam ievadît cilindra râdiusu un tâ augstumu, tiek aprçíinâts cilindra laukums un tilpums. Rezultâts tiek parâdîts konsolç.
# tilpums = 3.14 * râdiuss * râdiuss * augstums
# laukums = 2 * (3.14 * râdiuss * râdiuss) + augstums * (2 * 3.14 * râdiuss)

rādiuss = float(input("Ievadiet cilindra rādiusu: "))
augstums = float(input("Ievadiet cilindra augstumu: "))

tilpums = 3.14 * rādiuss * rādiuss * augstums

laukums = 2 * (3.14 * rādiuss * rādiuss) + augstums * (2 * 3.14 * rādiuss)

print("Cilindra tilpums ir:", round(tilpums, 2), "kubiskie metri")
print("Cilindra laukums ir:", round(laukums, 2), "kvadrātmetri")

