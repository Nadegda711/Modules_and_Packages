import true_math as tm
import fake_math as fm

f_d = fm.divide
t_d = tm.divide

result1 = f_d(69, 3)
result2 = f_d(3, 0)
result3 = t_d(49, 7)
result4 = t_d(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)
