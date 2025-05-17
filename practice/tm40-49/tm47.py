# 题目：首都
cities_dict={
    'Beijing': {'Capital': 'China'},
    'Moscow': {'Capital': 'Russia'},
    'Paris': {'Capital': 'France'}
    }
# 方法一：
for i in sorted(cities_dict):
    print(f"{i} is the capital of {cities_dict[i]['Capital']}!")
# 方法二：
for i,j in sorted(cities_dict.items()):
    print('%s is the capital of %s!'%(i,j['Capital']))
