
# coding: utf-8

# In[ ]:


from azureml import Workspace
ws = Workspace()
experiment = ws.experiments['83958a3d3cd846b9bbc143bcfb49f6b7.f-id.b6d0b07e33f24f538b883821995db957']
ds = experiment.get_intermediate_dataset(
    node_id='e58a7c54-7aef-4853-a8cd-259fded3ec4c-7499',
    port_name='Results dataset',
    data_type_id='GenericCSV'
)
frame = ds.to_dataframe()


# In[ ]:


frame

