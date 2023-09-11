def dis(price, discount):
	discounted_price = price * (1 - discount * 0.01)
	return round(discounted_price, 2)

print(dis(100, 75))