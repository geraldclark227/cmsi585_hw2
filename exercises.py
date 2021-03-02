def stretched(a):
    def rec(item, index):
        if index == 1:
            return [item]
        r = [item]
        r.extend(rec(item, index - 1))
        return r

    def tail(ar, index, result):
        if len(ar) == 0:
            return result
        else:
            result.extend(rec(ar.pop(0), index))

        return tail(ar, index + 1, result)

    return tail(a, 1, [])


#b = stretched([8, 3, 5, 2])
#print(b)


# POWERS
def powers(x, limit):
    r = 1
    while r <= limit:
        yield r
        r = r * x


p = powers(2, 7)
print(next(p))
print(next(p))
print(next(p))


# print(next(p))


def say(*first):
    if len(first) == 0:
        return ''

    def sub(*second):
        if len(second) == 0:
            return first[0]
        return say(f'{first[0]} {second[0]}')

    return sub


y = say('Hello')('my')('name')('is')('Colette')()
print(y)


def say2(*first):
    if len(first) == 0:
        return ''

    def sub2(*second):
        new = ''
        if len(second) == 0:
            for i in first:
                new += i + ' '
            return new

        for i in first:
            new += i + ' '
        new = new[: -1]
        for i in second:
            new += i + ' '
        return say2(new)

    return sub2


# y = say('Hello')('my')('name')('is')('Colette')()
# print(y)

z = say2('Hello')('my')('name')('is')('Colette')()
print(z)

input1 = {
    'ATL': [
        ['Betnijah Laney', 16, 263],
        ['Courtney Williams', 14, 193],
    ],
    'CHI': [
        ['Kahleah Copper', 17, 267],
        ['Allie Quigley', 17, 260],
        ['Courtney Vandersloot', 17, 225],
    ],
    'CONN': [
        ['DeWanna Bonner', 16, 285],
        ['Alyssa Thomas', 16, 241],
    ],
    'DAL': [
        ['Arike Ogunbowale', 16, 352],
        ['Satou Sabally', 12, 153],
    ],
    'IND': [
        ['Kelsey Mitchell', 16, 280],
        ['Tiffany Mitchell', 13, 172],
        ['Candice Dupree', 16, 202],
    ],
    'LA': [
        ['Nneka Ogwumike', 14, 172],
        ['Chelsea Gray', 16, 224],
        ['Candace Parker', 16, 211],
    ],
    'LV': [
        ['A’ja Wilson', 15, 304],
        ['Dearica Hamby', 15, 188],
        ['Angel McCoughtry', 15, 220],
    ],
    'MIN': [
        ['Napheesa Collier', 16, 262],
        ['Crystal Dangerfield', 16, 254],
    ],
    'NY': [
        ['Layshia Clarendon', 15, 188]
    ],
    'PHX': [
        ['Diana Taurasi', 13, 236],
        ['Brittney Griner', 12, 212],
        ['Skylar Diggins-Smith', 16, 261],
        ['Bria Hartley', 13, 190],
    ],
    'SEA': [
        ['Breanna Stewart', 16, 317],
        ['Jewell Loyd', 16, 223],
    ],
    'WSH': [
        ['Emma Meesseman', 13, 158],
        ['Ariel Atkins', 15, 212],
        ['Myisha Hines-Allen', 15, 236],
    ],
}


def top_ten_scorers(input1):
    topTen = []
    for k, v in input1.items():
        for players in v:
            if players[1] >= 15:
                if len(topTen) < 10:
                    ppg = players[2] / players[1]
                    topTen.append({'name': players[0], 'ppg': ppg, 'team': k})
                else:
                    ppg = players[2] / players[1]
                    topTen.sort(key=lambda x: x['ppg'])
                    if ppg > topTen[0]['ppg']:
                        topTen.pop(0)
                        topTen.append({'name': players[0], 'ppg': ppg, 'team': k})

    topTen.sort(key=lambda x: x['ppg'], reverse = True)
    return topTen


#g = topTenScorers(input1)
#print(len(g))
#print(g)

#INTERPRETER

def allNumbers(s):
   r = 1
   for i in s:
      if ord(i) > 57 or ord(i) < 48:
         return 0
   return r

def interpret(eval):
    token = eval.split(' ')
    stack1 = []
    for t in token:
        if allNumbers(t):
            stack1.insert(0, int(t))
        elif t == '+':
            y = stack1.pop(0)
            x = stack1.pop(0)
            stack1.insert(0, x + y)
        elif t == '-':
            y = stack1.pop(0)
            x = stack1.pop(0)
            stack1.insert(0, x - y)
        elif t == '*':
            y = stack1.pop(0)
            x = stack1.pop(0)
            stack1.insert(0, x * y)
        elif t == '/':
            y = stack1.pop(0)
            x = stack1.pop(0)
            stack1.insert(0, x / y)
        elif t == 'NEG':
            y = stack1.pop(0)
            stack1.insert(0, -1*y)
        elif t == 'SQRT':
            y = stack1.pop(0)
            stack1.insert(0, y**(1/2) )
        elif t == 'DUP':
            y = stack1[0]
            stack1.insert(0, y)
        elif t == 'SWAP':
            y = stack1.pop(0)
            stack1.insert(1, y)
        elif t == 'PRINT':
            x = stack1.pop(0)
            yield(x)
        else:
            raise ValueError

#print([*interpret("3 8 7 + PRINT 10 SWAP - PRINT")])

#print([*interpret("99 DUP * PRINT")])