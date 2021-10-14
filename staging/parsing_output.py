data = {'blocks': [{'type': 'section', 'text': {'type': 'mrkdwn', 'text': '*Ticket Triaging summary* for the requests from *2021-10-13 17:46:44* to *2021-10-14 00:46:44*  *EST*\n\n```Severity  Avg_TTA(min)  Avg_TTC(min)  Avg_WT(min) Updated   Logged  Closed  Total_Open\nHigh             36.75         36.75        36.75       0        1       1           0\nMedium           10.32        473.38       473.38       4        4       1         161\nLow               0.00          0.00         0.00       0        0       0           1\n\nNote\n* Avg_TTA(min)- Calculated for logged tickets(within shift)\n* Avg_TTC(min)- Calculated for closed tickets(within shift)\n* Avg_WT(min)- Average Waiting Time on Platform -SRE\n* Updated - Open requests(logged earlier) updated in the shift\n* Logged  - Requests logged in the current shift\n* Total_Open - Total backlog requests that are open at any given point of time.```\n- High requests Avg TTA is greater than the SLO of 30 mins :worried:\n\n'}}], 'username': 'psre-bot', 'channel': '#test-reports'}


data_set = data['blocks'][0]['text']['text']
print(data_set)
sentences = data_set.split('\n')
needed_sentences = []
for sentence in sentences[2:6]:
    needed_sentences.append(sentence.split())

needed_sentences[0][0] = needed_sentences[0][0][3:]
dict_results = dict(zip(needed_sentences[0], [needed_sentences[1], needed_sentences[2], needed_sentences[3]]))
print(dict_results)

