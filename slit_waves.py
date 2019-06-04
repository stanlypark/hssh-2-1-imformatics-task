from vpython import *
#GlowScript 2.7 VPython
scdis = 5
floor = box(length = 30, height = 0.5, width = 0.4, color = color.yellow) 
screen = box(length = 30, height = 0.5, width = 0.4, color = color.yellow, pos = vec(0, 0, scdis), text = 'screen!')
def make1(r, c):
    if c == 0:
        a = extrusion(pos = vec(5, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.red, shape=[[shapes.rectangle(pos=[0,0], width=0.3, height=0.1)]], opacity = 0.4)
    else : a = extrusion(pos = vec(5, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.blue, shape=[[shapes.rectangle(pos=[0,0], width=0.3, height=0.1)]], opacity = 0.4)
    return a
def make2(r, c):
    if c == 0:
        a = extrusion(pos = vec(-5, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.red, shape=[[shapes.rectangle(pos=[0,0], width=0.3, height=0.1)]], opacity = 0.4)
    else : a = extrusion(pos = vec(-5, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.blue, shape=[[shapes.rectangle(pos=[0,0], width=0.3, height=0.1)]], opacity = 0.4)
    return a
    
def move(x, r, flag, c):
    dr = 0.01
    x.visible = False
    r += dr
    if flag == 1 : k = make1(r, c)
    else: k = make2(r, c)
    return k

def meetcheck(com, r):
    scdis = 5
    return abs(com - (-5 + sqrt(r**2 - scdis**2))) < 0.2 or abs(com - (-5 - sqrt(r**2 - scdis**2))) < 0.2

def add(place, p, n):
    p = str(p)
    if abs(place[p]) >= 1:
        place[p] += n
    else:
        place[p] = n
    return place
    
shape = []
shape2 = []
shapecolor = [] #이거도 공용 사용
r = [] #r은 shape1과 shape2 모두 같음
makecnt = 0
shapecolor.append(0)
shape.append(make1(0.1, 0))
shape2.append(make2(0.1, 0))
r.append(0.1)
place = {}
g = gvbars(delta = 0.01, color = color.cyan)
gdata = []
flag = 0

scene.waitfor('click')
while(True):
    rate(100)
    gdata = []
    term = 20
    if makecnt % term == 0 and makecnt != 0 : 
        shape.append(make1(0.1, int((makecnt // term) % 2)))
        shape2.append(make2(0.1, int((makecnt // term) % 2)))
        shapecolor.append(int((makecnt // term) % 2))
        r.append(0.1)
        
    l = len(shape)
    
    #만나는지 판단
    for i in range(l):
        item = shape[i]
        if item.visible == True :
            #에너지 계산 - 만나는지 여부 판단
            if r[i] > scdis:
                #다른파동과 만나는지 검사한다
                com1 = 5 + sqrt((r[i])**2 - scdis**2)
                com2 = 5 - sqrt((r[i])**2 - scdis**2)
                for j in range(l):
                    itemcompare = shape2[j]
                    #종료조건
                    if itemcompare.visible == False or r[j] <= scdis :
                        continue
                    
                    #종료조건 check 를 통과하였다면
                    if meetcheck(com1, r[j]) == True or meetcheck(com2, r[j]) == True:
                        if meetcheck(com1, r[j]):
                            if shapecolor[i] == shapecolor[j] : place = add(place, com1, 2) #보강간섭
                            if shapecolor[i] != shapecolor[j] : place = add(place, com1, -2) #상쇄간섭
                        
                        if meetcheck(com2, r[j]):
                            if shapecolor[i] == shapecolor[j] : place = add(place, com2, 2) #보강간섭
                            if shapecolor[i] != shapecolor[j] : place = add(place, com2, -2) #상쇄간섭
    
    #추가 + 움직이기
    for i in range(l):
        flag = 0
        if r[i] > scdis * 2.0:
            shape[i].visible = False
            shape2[i].visible = False
        item = shape[i]
        if item.visible == True :
            shape.append(move(item, r[i], 1, shapecolor[i]))
            r.append(r[i] + 0.05)
            shapecolor.append(shapecolor[i])          
                    
        item2 = shape2[i]
        if item2.visible == True :
            shape2.append(move(item2, r[i], 0, shapecolor[i]))
        
    #삭제 (실행속도 빠르게 하기 위해서)
    for i in range(l):
        if i < len(shape) and shape[i].visible == False:
            shape.remove(shape[i])
            r.remove(r[i])
            shapecolor.remove(shapecolor[i])
        if i < len(shape) and shape2[i].visible == False:
            shape2.remove(shape2[i])
    makecnt += 1
    if place != {} :
        for i in place:
            g.plot([float(i), place[i]])
    if makecnt % 25 == 0 and makecnt != 0 : g.delete()
    #print_options(clear=True)