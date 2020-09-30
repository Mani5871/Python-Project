#!/usr/bin/env python
# coding: utf-8

# In[1]:


# context managers


# In[38]:


import requests
import math
from tqdm import tqdm
import time

url = 'http://www.africau.edu/images/default/sample.pdf'
request = requests.get(url)
chunk_size = 256
file_size = int(request.headers['Content-Length'])

n = math.ceil(file_size/chunk_size)

with open("file.pdf", "wb") as file:
    for chunk in tqdm(request.iter_content(chunk_size = chunk_size), total = n):
        time.sleep(0.01)
        file.write(chunk)


# In[ ]:




