
# coding: utf-8

# In[ ]:


from azureml import Workspace
ws = Workspace()
experiment = ws.experiments['83958a3d3cd846b9bbc143bcfb49f6b7.f-id.cb260ca903334398a75d9f95c3156869']
ds = experiment.get_intermediate_dataset(
    node_id='1a205cce-2375-466b-8a04-83e2801ce495-10916',
    port_name='Results dataset',
    data_type_id='GenericCSV'
)
frame = ds.to_dataframe()


# In[ ]:


frame

