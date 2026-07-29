# bounce.py
#
# Exercise 1.5

initial_height = 100
height_loss_factor = 3/5
height_from_ground = initial_height * height_loss_factor
num_bounces = 0

while num_bounces < 10:
    print(num_bounces + 1, height_from_ground)
    height_from_ground *= height_loss_factor
    num_bounces += 1