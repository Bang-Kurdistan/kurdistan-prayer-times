import json

cities = ['Akre','Amedi','Arbat','Barznja','Bazyan','Chamchamal','Chwarta',
  'Darbandixan','Duhok','Dukan','HajiAwa','Halabja','HalabjaN','Hawler',
  'Kalar','Kfri','Kirkuk','Koya','mosul','Penjuin','Piramagrun','qasre',
  'QadirKaram','Qaladze','Qaradax','Ranya','SaidSadiq','Slemany','Soran',
  'Takya','TaqTaq','Tasluja','tuzxurmatu','Xalakan','Xanaqin','Zaxo']

parts = []
total = 0
for city in cities:
    with open(f'data/{city}.json') as f:
        data = json.load(f)
    mini = [{'Date':r['Date'],'Fajr':r['Fajr'],'Sunrise':r['Sunrise'],'Dhuhr':r['Dhuhr'],'Asr':r['Asr'],'Maghrib':r['Maghrib'],'Isha':r['Isha']} for r in data]
    total += len(mini)
    parts.append(json.dumps(city) + ':' + json.dumps(mini, separators=(',',':')))

bundle = '{' + ','.join(parts) + '}'
print(f'Total entries: {total}')
print(f'Bundle size: {len(bundle)} bytes ({len(bundle)//1024}KB)')

with open('_data_bundle.js', 'w') as f:
    f.write('const CITY_DATA = ' + bundle + ';')
print('Written to _data_bundle.js')
