import csv

def find_s(training_data):
    hypothesis = ['0'] * (len(training_data[0]) - 1)
    for row in training_data:
        if row[-1] == 'Yes':
            for i in range(len(hypothesis)):
                if hypothesis[i] == '0':
                    hypothesis[i] = row[i]
                elif hypothesis[i] != row[i]:
                    hypothesis[i] = '?'
    return hypothesis

data = [
    ['Sunny','Warm','Normal','Strong','Warm','Same','Yes'],
    ['Sunny','Warm','High','Strong','Warm','Same','Yes'],
    ['Rainy','Cold','High','Strong','Warm','Change','No']
]

print("Most Specific Hypothesis:", find_s(data))
