print("\t")
print("\t\t\t===============================")
print("\t\t\t| Enhanced Money Denomination |")
print("\t\t\t===============================")
print("\t")

val_of_money = int(input("Please enter the money you have: "))

a_money = val_of_money % 1000
b_money = (val_of_money - a_money) / 1000

c_money = a_money % 500
d_money = (a_money - c_money) / 500

e_money = c_money % 200
f_money = (c_money - e_money) / 200

g_money = e_money % 100
h_money = (e_money - g_money) / 100

i_money = g_money % 50
j_money = (g_money - i_money) / 50

k_money = i_money % 20
l_money =(i_money - k_money) / 20

m_money = k_money % 10
n_money = (k_money - m_money) / 10

o_money = m_money % 5
p_money = (m_money - o_money) / 5

q_money = o_money % 1
r_money = (o_money - q_money) / 1

if b_money > 0:
	print(f"You have {b_money} in thousand peso bill")

if d_money > 0:
	print(f"You have {d_money} in five hundred peso bill")

if f_money > 0:
	print(f"You have {f_money} in two hundred peso bill")

if h_money > 0:
	print(f"You have {h_money} in one hundred peso bill")

if j_money > 0:
	print(f"You have {j_money} in fifty peso bill")

if l_money > 0:
	print(f"You have {l_money} in twenty peso bill")

if n_money > 0:
	print(f"You have {n_money} in ten peso")

if p_money > 0:
	print(f"You have {p_money} in five peso")

if r_money > 0:
	print(f"You have {r_money} in one peso")