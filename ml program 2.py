import numpy as np

def candidate_elimination(data):
    s = data[0][:-1]
    g = [['?' for _ in s]]
    for row in data:
        if row[-1] == 'Yes':
            for i in range(len(s)):
                if row[i] != s[i]:
                    s[i] = '?'
        else:
            for i in range(len(s)):
                if row[i] != s[i]:
                    g.append([s[j] if j==i else '?' for j in range(len(s))])
    return s, g

data = np.array([
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No']
])

s, g = candidate_elimination(data)
print("Specific Boundary:", s)
print("General Boundary:", g)
