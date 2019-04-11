#!/usr/bin/env python
# coding: utf-8

# In[1]:


from azureml import Workspace
ws = Workspace()
experiment = ws.experiments['83958a3d3cd846b9bbc143bcfb49f6b7.f-id.9a51af92346549aeb9d01f8088bac6c0']
ds = experiment.get_intermediate_dataset(
    node_id='5441beca-c0dc-4eed-acf6-c65d1ccc02c7-37198',
    port_name='Results dataset',
    data_type_id='GenericCSV'
)
frame = ds.to_dataframe()


# In[2]:


frame


# In[ ]:




