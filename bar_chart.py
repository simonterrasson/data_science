from matplotlib import pyplot as plt

movies = ["Alien 1", "Alien 2", "Alien 3", "Alien 4", "Prometheus"]
num_oscars = [9, 10, 9, 2, 1]
# bars are by default width 0.8, so we'll add 0.1 to the left coordinates
# so that each bar is centered
xs = [i + 0.1 for i, _ in enumerate(movies)]
# print(xs)

xtest = []
idx = 0

for i in movies:
    # print(i)
    xtest.append(idx+0.1)
    idx += 1
    
print(xtest)
# plot bars with left x-coordinates [xs], heights [num_oscars]
plt.bar(xtest, num_oscars)
plt.ylabel("Personnal rating")
plt.title("Simple Alien Analysis")
# label x-axis with movie names at bar centers
plt.xticks([i + 0.5 for i, _ in enumerate(movies)], movies)
plt.show()
