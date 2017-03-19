from textblob import TextBlob
from plotly.offline import plot
import plotly.graph_objs as go
import random
user1 = "Bob"
user2 = 'Alice'
with open('chat_sample.txt', 'r+') as f:
    samples = f.readlines()
    d = {user1:[], user2:[]}
    for line in samples:
        time, *text = line.split('-')
        text = ''.join(text)
        name, *chat = text.split(':')
        t = TextBlob(''.join(chat))
        name = name.strip()
        if name == user1 or name == user2:
            d[name].append(t.sentiment.polarity)
trace1 = go.Scatter(
    y = d[user1][:9000],
    name = user1,
    mode = 'markers',
    marker=dict(
        size='8',
        colorscale='Picnic',
        color = random.sample(range(9000),9000),
        )
    )
trace2 = go.Scatter(
    y = d[user2],
    name = user2,
    mode = 'markers',
    marker=dict(
        size='7',
        color = random.sample(range(8000), 8000),
        colorscale='Electric',
        )
    )
data = [trace1, trace2]
plot(data)