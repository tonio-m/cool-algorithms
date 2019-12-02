import random

def population(n,strsize):
    p = list()
    for i in range(n):
        s = generate_string(strsize)
        p.append(s)
    return p

def choose_best(population,target,n):
    scores = []
    for string in population:
        score = fitness(string,target) 
        scores.append(score)
    results = list(zip(scores,population))
    results = sorted(results, reverse=True)
    chosen = [x[1] for x in results[:n]]
    return chosen

def reproduce(*parents,target):
    strlen = len(target)
    child = []
    for i in range(strlen):
        match = any_match_pos(parents,target,i)
        if match:
            child.insert(i,match)
        else:
            parent = random.randint(0,len(parents)-1)
            child.insert(i,parents[parent][i])
    child = ''.join(child)
    return [child]

def mutate(population,rate):
    letters = ' abcdefghijklmnopqrstuvwxyz'
    population = [list(s) for s in population]
    for i in range(len(population)):
        for j in range(len(population[i])):
            chosen = random.choices((True,False),weights=(rate,1-rate))[0]
            if chosen:
                population[i][j] = random.choice(letters)
    population = [''.join(l) for l in population]
    return population

def kill(population,target,kill_rate):
    strlen = len(target)
    scores = list()
    for string in population:
        score = fitness(string,target)
        scores.append(score)
    results = list(zip(scores,population))
    results= sorted(results)
    results = results[round(kill_rate):]
    return [r[1] for r in results]

def generate_string(strsize):
    letters = ' abcdefghijklmnopqrstuvwxyz'
    string = str()
    for i in range(strsize):
        string += random.choice(letters)
    return string

def any_match_pos(parents,target,i):
    strlen = len(target)
    match = None
    for parent in parents:
        if parent[i] == target[i]:
            match = parent[i]
            break
    return match

def fitness(string,target):
    score = 0
    for i in range(len(string)):
        if string[i] == target[i]:
            score += 1
    return score

def init(target,pop_size,mut_rate,kill_rate,parent_num):
    gen = 0
    pop = population(pop_size,strsize=len(target))
    while True:
        best = choose_best(pop,target,parent_num)
        print('\r',end=''); print(best[0],end='')
        if target in best:
            print('\n',end='')
            print(f'the algorithm suceeded after {gen} generations')
            return
        new = reproduce(*best,target=target)
        new = mutate(new,mut_rate)
        pop += new
        pop = kill(pop,target,kill_rate)
        gen +=1

if __name__ == '__main__':
    target = 'the algorithm will evolve to this string'
    pop_size = 11
    mut_rate = 0.1
    kill_rate = 1
    parents = 2
    
    init(target,pop_size,mut_rate,kill_rate,parents)