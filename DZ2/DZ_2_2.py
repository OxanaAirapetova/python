
ls = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ls2 = []

for item in ls:
   if item.isdigit():
      ls2.extend(['"', f'{int(item):02}', '"'])
   elif item[1:].isdigit():
      ls2.extend(['"', f'{item[0]}{int(item):02}', '"'])
   else:
      ls2.append(item)
print(ls2)

ls2 = ' '.join(ls2)
print(ls2)

