import pandas as pd
from django.http import HttpResponseRedirect
import os
import django
import chardet

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PCX.settings')
django.setup()

from product.models import product_full

#with open('laptops.csv','rb') as rawdata:
#	result=chardet.detect(rawdata.read(10000000))
#print(result)

csv_data=pd.read_csv('laptops.csv',encoding='ISO-8859-1')
for i in range(1,1300):
	data=product_full()
	data.p_types='Laptop'
	data.p_brand=csv_data['Company'][i]
	data.p_name=csv_data['Product'][i]
	data.typ=csv_data['TypeName'][i]
	data.screen_size=csv_data['Inches'][i]
	data.screen_res=csv_data['ScreenResolution'][i]
	data.cpu=csv_data['Cpu'][i]
	data.ram=csv_data['Ram'][i]
	data.memory=csv_data['Memory'][i]
	data.gpu=csv_data['Gpu'][i]
	data.op_sys=csv_data['OpSys'][i]
	data.weight=csv_data['Weight'][i]
	data.p_rate=csv_data['Price_euros'][i]*89.47
	data.save()