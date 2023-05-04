a = 'A'
b = 'B'
c = 1.1

q = 'HBSF'
w = 'Rose'
e = 1500.2

formato = 'a = {} - b = {} - c = {:.2f}'.format(a, b, c)
formato_2 = 'e = {nome3:,.2f} - w = {nome2} - q = {nome1}'.format(
   nome1 = q,
   nome2 = w,
   nome3 = e
)
print(formato)
print(formato_2)