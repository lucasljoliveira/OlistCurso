def soma (n1:float, n2:float) -> float:
	if valida_float(n1) and valida_float(n2):
		resultado = n1 + n2
		return resultado

def subtracao (n1:float, n2:float) -> float:
	if valida_float(n1) and valida_float(n2):
		resultado = n1 - n2
		return resultado

def divisao (n1:float, n2:float) -> float:
	if valida_float(n1) and valida_float(n2) and valida_zero(n2):
		resultado = n1 / n2
		return resultado

def multiplicacao (n1:float, n2:float) -> float:
	if valida_float(n1) and valida_float(n2):
		resultado = n1 * n2
		return resultado
	
def valida_float(n:float) -> bool:
	if isinstance(n, float):
		return True
	raise ValueError(f"O valor informado {n} deve ser um número.")

def valida_zero(n:float) -> bool:
	if n > 0:
		return True
	raise ValueError("Não é possível divisão por zero.")



