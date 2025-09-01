movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

add = int(input("No. of movies to add: "))
n = 0
while n < add:
    name = input("Enter movie name: ")
    budget = int(input("Enter budget: "))
    movies.append((name, budget))
    n += 1

total = 0
for i in range(len(movies)):
    total += movies[i][1]
avg = total / len(movies)
print("Average budget is:", avg)

high_budget = []
for j in range(len(movies)):
    if movies[j][1] > avg:
        diff = movies[j][1] - avg
        print(f"{movies[j][0]}  is {diff} higher than the average movie's budget")
        high_budget.append(movies[j][0])

print("Movies haing more than avg budget:", high_budget)
print("No. of movies spent more than the average:", len(high_budget))
