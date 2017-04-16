import math, random
# Импортируем один из пакетов Matplotlib
import pylab
# Импортируем пакет со вспомогательными функциями
from matplotlib import mlab


# Рисуем график функции y = sin(x)
klasters=4

# Создадим список координат по оси
# X на отрезке [-xmin; xmax], включая концы
xlist = [random.randint(0,10) for x in range(0,15)]

# Вычислим значение функции в заданных точках
ylist = [random.randint(0,10) for x in range(0,15)]

# Нарисуем одномерный график
pylab.scatter(xlist, ylist)
points = list(zip(xlist,ylist))
# собственно массив точек [(x,y),(x1,y2)...]
# Покажем окно с нарисованным графиком
print(list(points))
pmin=1000.0
for i in points: #поиск первого минимального отрезка РАБОТАЕТ

    for j in points:

       if i != j:
            p=math.hypot(i[0]-j[0],i[1]-j[1])

            if p<pmin:
                pmin=p
                p1=i
                p2=j
print(pmin,p1,p2)
pylab.plot([p1[0],p2[0]],[p1[1],p2[1]],color='blue')
dict_max = {}
izo_points=[]   # список неизолированных точек
izo_points.append(p1) #добавили первые 2 неизолированные
izo_points.append(p2)

points.remove(p1) #заремувили неизолированные точки  -  в points теперь будут только изолированные
points.remove(p2)
#print('dict_max 1',dict_max)


i=0
print(points)
print(izo_points)
while points != []:   #РАБОТАЕТ  НЕ ТРОГАЙ ФУФУ ФУ  ИНАЧЕ КУСь_КУСЬ
 pmin = 1000
 for i in points:

    for j in izo_points:

        p = math.hypot(i[0] - j[0], i[1] - j[1])

        if p < pmin:
            pmin = p
            p1 = i
            p2 = j
 pylab.plot([p1[0],p2[0]],[p1[1],p2[1]],color='red')
 for v in dict_max.keys():
     if p == v:
         test = random.random()
         if test>0.5:
             p=p+random.random()*0.00001
         else:
             p = p - random.random() * 0.00001
 #((15, 38), (40, 22))
 dict_max[p] = p1,p2
 izo_points.append(p1)
 points.remove(p1)
 print(i,'шаг')
 print(points)
 print(izo_points)
#print('dict2',dict_max) #  пока еще словарь
#dict_max = sorted(dict_max,reverse=True)
#k= sorted(dict_max.keys(),reverse=True)
#for key in sorted(dict_max.keys(),reverse=True):
   # print("(%s => %s)",key, dict_max[key])
###
s=0
for key in sorted(dict_max.keys(),reverse=True):
    print('sorted', key)
    if s<(klasters-1):
      print((dict_max[key])) #turple
      p1 = dict_max[key][0]
      p2 = dict_max[key][1]
      pylab.plot([p1[0], p2[0]], [p1[1], p2[1]], color='white')
      s += 1
  # # pylab.plot([p1[0], p2[0]], [p1[1], p2[1]], color='green')
###

pylab.show()
print('taki narisoval')