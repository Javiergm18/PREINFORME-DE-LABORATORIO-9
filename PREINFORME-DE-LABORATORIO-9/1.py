xP1 = int(input("digite el valor en x del primer punto: "))
yP1 = int(input("digite el valor en Y del primer punto: ")) 
xP2 = int(input("digite el valor en x del segundo punto: "))
yP2 = int(input("digite el valor en Y del segundo punto: "))

d = abs(((xP2-xP1)*(xP2-xP1))*((yP2-yP1)*(yP2-yP1)))
print("la distancia entre los dos puntps es de: ",d)