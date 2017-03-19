# Whatsapp Sentiments Visualizer 
Visualization of chat sentiments from a whatsapp chat backup (16k Messages).

![Chat](/plot.png?raw=true "Plot of 16k messages from a chat")  

# Dependencies:  
 * [textblob](http://textblob.readthedocs.io/en/dev/index.html)
 * [plotly](https://plot.ly/python/)
# Installation:
* `pip install -r requirements.txt`

* `python -m textblob.download_corpora`  

# Run:

* copy your whatsapp chat text in chat_sample.txt
* set usernames (`user1` & `user2` in the `whatsapp-sentiment.py` file)  
* `python whatsapp-sentiment.py`
