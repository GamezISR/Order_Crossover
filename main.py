
def make_empty_offspring(how_big):
    offspring = []
    for i in range(how_big):
        offspring.append("")
    return offspring


def order_crossover(p1, p2):
    offspring = make_empty_offspring(10)
    print(offspring)
    start = 1
    end = 6
    count = end
    for i in range(start,end):
        offspring[i] = p1[i]
    print(offspring)
    for i in range(end, len(offspring)):
        while True:
            try:
                found = offspring.index(p2[count])
                if count == len(offspring)-1:
                    count = 0
                else:
                    count += 1
            except ValueError:
                offspring[i] = p2[count]
                break
    print(offspring)
    while True:
        counter = 0
        if offspring[counter] != '':
            break
        else:
            for i in range(start):
                while True:
                    try:
                        found = offspring.index(p2[count])
                        count += 1
                    except ValueError:
                        offspring[i] = p2[count]
                        break
            counter = counter + 1
    print(offspring)





parent_one = ["J","B","F","C","A","D","H","G", "I", "E"]
parent_two = ["F", "A", "G", "D", "H", "C", "E","B", "J", "I"]

print("Parent 1: ", parent_one)
print("Parent 2: ", parent_two)
order_crossover(parent_one,parent_two)





