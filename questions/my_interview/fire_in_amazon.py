
# year, state, month, number
# 2000, Rio, Novembro, 18
# 2002, Pernambuco, Fevereiro, 64
# 2001, Mato Grosso, Maio, 112
# 2003, Roraima, Janeiro, 547
# 2002, Maranhao, Julho, 4
# 2003, Rio, Março, 9
# 2000, Roraima, Outubro, 25
# 2001, Paraiba, Janeiro, 11

# year, number
# 2002,68
# 2000,43
# 2003,556
# 2001,123


# put the above file in 'test_file.txt'
import sys

even_year = {}
event_month = {}

sys.stdin = open('test_file.txt', 'r')

for line in sys.stdin:
    if line == "\n":
        continue
    key, *rest,  value = line.split(',')
    if len(rest) > 0 and key != 'year':
        event_month[key] = int(value.strip()) + event_month.get(key, 0)
    elif key != 'year':
        even_year[key] = int(value.strip())


def result():
    for key in even_year:
        if even_year[key] != event_month[key]:
            return False
    return True


print(result())
