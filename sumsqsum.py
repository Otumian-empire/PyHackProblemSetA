# 12 - Find the sum of the square of the first 20 even numbers and the square of the sum of the first 20 even numbers


# sum of the square of the first 20 even numbers - sigma(sq(2k*20))
sigma_even = 0
for i in range(1, 21):
    sigma_even += (i * 2) ** 2
print('The sum of the square of the first 20 even numbers is', sigma_even)

# square of the sum of the first 20 even numbers - sq(sigma(2k*20))
sigma_even = 0
sq_of_sigma_even = 0
for i in range(1,21):
    sigma_even += (i * 2)

sq_of_sigma_even = sigma_even ** 2
print('The square of the sum of the first 20 even numbers is', sq_of_sigma_even)