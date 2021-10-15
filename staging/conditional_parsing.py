data1 = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn',
                                                 'text': '*Ticket Triaging summary* for the requests from *2021-10-13 17:46:44* to *2021-10-14 00:46:44*  *EST*\n\n```Severity  Avg_TTA(min)  Avg_TTC(min)  Avg_WT(min) Updated   Logged  Closed  Total_Open\nHigh             36.75         36.75        36.75       0        1       1           0\nMedium           10.32        473.38       473.38       4        4       1         161\nLow               0.00          0.00         0.00       0        0       0           1\n\nNote\n* Avg_TTA(min)- Calculated for logged tickets(within shift)\n* Avg_TTC(min)- Calculated for closed tickets(within shift)\n* Avg_WT(min)- Average Waiting Time on Platform -SRE\n* Updated - Open requests(logged earlier) updated in the shift\n* Logged  - Requests logged in the current shift\n* Total_Open - Total backlog requests that are open at any given point of time.```\n- High requests Avg TTA is greater than the SLO of 30 mins :worried:\n\n'}}],
         'username': 'psre-bot', 'channel': '#test-reports'}
data2 = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn',
                                                 'text': '*Ticket Triaging summary* for the requests from *2021-10-14 09:40:30* to *2021-10-14 16:40:30*  *EST*\n\n```Severity  Avg_TTA(min)  Avg_TTC(min)  Avg_WT(min) Updated   Logged  Closed  Total_Open\nCritical          1.52          9.84         9.84       0        2       1           1\nHigh              0.00        269.15       269.15       1        0       1           0\nMedium            0.00         71.94        71.94       9        5       9         165\nLow               0.00          0.00         0.00       0        0       0           1\n\nNote\n* Avg_TTA(min)- Calculated for logged tickets(within shift)\n* Avg_TTC(min)- Calculated for closed tickets(within shift)\n* Avg_WT(min)- Average Waiting Time on Platform -SRE\n* Updated - Open requests(logged earlier) updated in the shift\n* Logged  - Requests logged in the current shift\n* Total_Open - Total backlog requests that are open at any given point of time.```\n\n'}}],
         'username': 'psre-bot', 'channel': '#test-reports'}

data_set1 = data1['blocks'][0]['text']['text']
data_set2 = data2['blocks'][0]['text']['text']
# print(data_set1)
# print(data_set2)

stencil = {'Critical': [0, 0, 0, 0, 0, 0, 0], 'High': [0, 0, 0, 0, 0, 0, 0], 'Medium': [0, 0, 0, 0, 0, 0, 0],
           'Low': [0, 0, 0, 0, 0, 0, 0]}
keywords_list = ['Critical', 'High', 'Medium', 'Low']
sentences1 = data_set1.split('\n')
sentences2 = data_set2.split('\n')

filtered_data = []
#print(sentences2)

for i in keywords_list:
    for j in sentences1:
        if i in j:
            filtered_data.append(j.split())
        else:
            pass

print(filtered_data)

k = []
v = []
j = 0
for i in filtered_data:
    k.append(filtered_data[j][0])
    v.append(filtered_data[j][1:])
    j += 1

dict_data = dict(zip(k, v))
print(dict_data)

stencil = {'Critical': [0, 0, 0, 0, 0, 0, 0], 'High': [0, 0, 0, 0, 0, 0, 0], 'Medium': [0, 0, 0, 0, 0, 0, 0],
           'Low': [0, 0, 0, 0, 0, 0, 0]}

stencil.u
stencil.update(dict_data)


print(stencil)
