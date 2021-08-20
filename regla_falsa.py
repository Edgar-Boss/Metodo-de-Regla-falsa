import math

expr = input('Ingrese funcion: ')#pide la expresion algebraica en terminos de x y la guarda en variable expr
a = float(input("a: "))
b = float(input("b: "))

itmax=100
tol=1.e-5
xr=100
error=100
it=0
while error>tol and it<itmax: 
	it +=1

	print("xa::",a)
	print("xb::",b)

	libres=dict(x=b) #evalua en b
	funcs = vars(math)
	fb = eval(expr, funcs,libres)
	
	print("fxb::",fb)
	
	libres=dict(x=a) #evalua en a
	funcs = vars(math)
	fa=eval(expr, funcs,libres)
	
	print("fxa::",fa)
	
	vxr=xr
	xr=b-((fb*(b-a))/(fb-fa))
	
	print("xr::",xr)
	
	libres=dict(x=xr) #evalua en xr
	funcs = vars(math)
	fxr=eval(expr, funcs,libres)	

	n_x=fa*fxr

	error=abs(((xr-vxr)/xr)*100)
	
	print("fxr::",fxr)
	print("mul::",n_x)
	print("error:",error)
	print("///////////////////////////",it)
	
	if n_x>0:
		a=xr
	if n_x<0:
		b=xr