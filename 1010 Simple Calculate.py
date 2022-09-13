pro_1_code, pro_1_unit, pro_1_price = input().split( )
pro_2_code, pro_2_unit, pro_2_price = input().split( )
total = (int(pro_1_unit) * float(pro_1_price)) + (int(pro_2_unit) * float(pro_2_price))
print(f'VALOR A PAGAR: R$ {total:.2f}')