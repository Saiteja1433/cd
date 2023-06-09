def calculate_probability(P_A,P_B,P_B_given_A):
    P_A_given_B = (P_B_given_A*P_A)/P_B
    return P_A_given_B
P_A = 0.03
P_B = 0.20
P_B_given_A = 1.0
P_A_given_B = calculate_probability(P_A,P_B,P_B_given_A)
print(P_A_given_B)