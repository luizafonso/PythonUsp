def formaTriangulo(n):
	lado1 = 0
	lado2 = 0
	lado3 = 0
	for a in range(1, n):
		for b in range (1, n - a ):
			c = n - a - b
			print("lado a:", a, end="")
			print(" lado b:", b, end="")
			print(" lado c:",c, end="")
			if((a < b+c ) and (b < a+c) and (c < a+b)):
				print("--------> é triângulo!")
			else:
				print()
	
	
	
	
		
	


x = int(input("informe um valor: "))
formaTriangulo(x)

