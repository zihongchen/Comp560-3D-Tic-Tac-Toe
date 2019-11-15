#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import random
from time import sleep
import math
from Game import *
from learning import *


# In[10]:


iterations1=100
iterations2=1000
iterations3=2000
learning_randomly_4x4x4(iterations1,iterations2,iterations3)


# In[11]:


iterations1=1
iterations2=10
iterations3=20000
learning_with_exploration_and_exploitation(iterations1,iterations2,iterations3)


# In[ ]:




