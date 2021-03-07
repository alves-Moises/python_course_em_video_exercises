#calculo de sendo, cosseno e tangente
import math

an = float(input("Angle: "))
sen = math.sin(math.radians(an))
print(f'The angle of {an} have\'s {sen:.2f} how seno')
coss = math.cos(math.radians((an)))
print(f'This is the cos: {coss:.2f}')
tang = math.tan((math.radians(an)))
print(f'Tang: {tang:.2f}')