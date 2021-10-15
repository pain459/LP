data = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn',
                                                'text': '*Ticket Triaging summary* for the requests from *2021-10-13 17:46:44* to *2021-10-14 00:46:44*  *EST*\n\n```Severity  Avg_TTA(min)  Avg_TTC(min)  Avg_WT(min) Updated   Logged  Closed  Total_Open\nHigh             36.75         36.75        36.75       0        1       1           0\nMedium           10.32        473.38       473.38       4        4       1         161\nLow               0.00          0.00         0.00       0        0       0           1\n\nNote\n* Avg_TTA(min)- Calculated for logged tickets(within shift)\n* Avg_TTC(min)- Calculated for closed tickets(within shift)\n* Avg_WT(min)- Average Waiting Time on Platform -SRE\n* Updated - Open requests(logged earlier) updated in the shift\n* Logged  - Requests logged in the current shift\n* Total_Open - Total backlog requests that are open at any given point of time.```\n- High requests Avg TTA is greater than the SLO of 30 mins :worried:\n\n'}}],
        'username': 'psre-bot', 'channel': '#test-reports'}

data_set = data['blocks'][0]['text']['text']
print(data_set)
sentences = data_set.split('\n')
needed_sentences = []
for sentence in sentences[2:6]:
    needed_sentences.append(sentence.split())

needed_sentences[0][0] = needed_sentences[0][0][3:]
dict_results = dict(
    zip(needed_sentences[0], [needed_sentences[1], needed_sentences[2], needed_sentences[3], needed_sentences[4]]))
print(dict_results)

data2 = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn',
                                                 'text': '*Ticket Triaging summary* for the requests from *2021-10-14 09:40:30* to *2021-10-14 16:40:30*  *EST*\n\n```Severity  Avg_TTA(min)  Avg_TTC(min)  Avg_WT(min) Updated   Logged  Closed  Total_Open\nCritical          1.52          9.84         9.84       0        2       1           1\nHigh              0.00        269.15       269.15       1        0       1           0\nMedium            0.00         71.94        71.94       9        5       9         165\nLow               0.00          0.00         0.00       0        0       0           1\n\nNote\n* Avg_TTA(min)- Calculated for logged tickets(within shift)\n* Avg_TTC(min)- Calculated for closed tickets(within shift)\n* Avg_WT(min)- Average Waiting Time on Platform -SRE\n* Updated - Open requests(logged earlier) updated in the shift\n* Logged  - Requests logged in the current shift\n* Total_Open - Total backlog requests that are open at any given point of time.```\n\n'}}],
         'username': 'psre-bot', 'channel': '#test-reports'}

data_set2 = data2['blocks'][0]['text']['text']
# print(data_set2)


sentences2 = data_set2.split('\n')
keywords_list = ['Critical', 'High', 'Medium', 'Low']
filtered_sentences = []
# print(sentences2)

for i in keywords_list:
    for j in sentences2:
        if i in j:
            filtered_sentences.append(j.split())
        else:
            pass

print(filtered_sentences)

needed_sentences2 = []
# This is where the string lists we have to apply the filter function here.


for sentence in sentences2[2:7]:
    words = sentence.split()
    needed_sentences2.append(words)

print(needed_sentences2)

needed_sentences2[0][0] = needed_sentences2[0][0][3:]
print(needed_sentences2)
dict_results = dict(
    zip(needed_sentences2[0], [needed_sentences2[1], needed_sentences2[2], needed_sentences2[3], needed_sentences2[4]]))
print(dict_results)

# Below list to be sorted as a dict
data = [['Severity', 'Avg_TTA(min)', 'Avg_TTC(min)', 'Avg_WT(min)', 'Updated', 'Logged', 'Closed', 'Total_Open'],
        ['Critical', '1.52', '9.84', '9.84', '0', '2', '1', '1'],
        ['High', '0.00', '269.15', '269.15', '1', '0', '1', '0'],
        ['Medium', '0.00', '71.94', '71.94', '9', '5', '9', '165'], ['Low', '0.00', '0.00', '0.00', '0', '0', '0', '1']]
data = data[1:]
print(data)
k = []
v = []
j = 0
for i in data:
    k.append(data[j][0])
    v.append(data[j][1:])
    j += 1

dict_data = dict(zip(k, v))
print(dict_data)

print(type(dict_data['Critical'][0]))

# ---------------------------------------------------------------------------------------------------

# test_dict
stencil = {'Critical': [0, 0, 0, 0, 0, 0, 0], 'High': [0, 0, 0, 0, 0, 0, 0], 'Medium': [0, 0, 0, 0, 0, 0, 0],
           'Low': [0, 0, 0, 0, 0, 0, 0]}

#updict
enriched_data = {'Critical': ['0.55', '20.20', '20.20', '0', '1', '1', '0'],
                 'Medium': ['29.10', '41.26', '41.26', '4', '4', '2', '166'],
                 'Low': ['0.00', '0.00', '0.00', '0', '0', '0', '1']}

new_data = {key: enriched_data.get(key, stencil[key]) for key in stencil}

print(new_data)



# Python3 code to demonstrate working of
# Replace dictionary value from other dictionary
# Using dictionary comprehension

# initializing dictionary
test_dict = {"Gfg": 5, "is": 8, "Best": 10, "for": 8, "Geeks": 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing updict
updict = {"Gfg": 10, "Best": 17}

res = {key: updict.get(key, test_dict[key]) for key in test_dict}

# printing result
print("The updated dictionary: " + str(res))
