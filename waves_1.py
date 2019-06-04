from vpython import *
#GlowScript 2.7 VPython
scdis = 5
scdistance = 1
slitdis = 10
slitdistance = 1

floor = box(length = 30, height = 0.5, width = 0.4, color = color.yellow) 
print('[시작 전 초기 Setting 1] \n스크린과의 간격을 설정합니다. 기본값은 5입니다. \nn배 할 값을 설정해 주세요.')
while(True):
    ev = scene.waitfor('click keydown') 
    if ev.event == 'click':
        print_options(clear=True)
        print('설정 완료. 클릭해 주세요.')
        break
    if ev.event == 'keydown':
        if ev.keyCode == 38:
            scdistance += 0.25
            print_options(clear=True)
            print('스크린 사이 간격 : 기본값 *' + scdistance + '배')
        if ev.keyCode == 40:
            scdistance -= 0.25
            print_options(clear=True)
            print('스크린 사이 간격 : 기본값 *' + scdistance + '배')
scdis = scdis * scdistance
screen = box(length = 30, height = 0.5, width = 0.4, color = color.yellow, pos = vec(0, 0, scdis), text = 'screen!')
scene.waitfor('click')
print_options(clear=True)

#슬릿사이 간격설정
print('[시작 전 초기 Setting 2] \n슬릿간의 과의 간격을 설정합니다. 기본값은 10입니다. \nn배 할 값을 설정해 주세요.')
while(True):
    ev = scene.waitfor('click keydown') 
    if ev.event == 'click':
        print_options(clear=True)
        print('설정 완료. 클릭해 주세요.')
        break
    if ev.event == 'keydown':
        if ev.keyCode == 38:
            slitdistance += 0.25
            print_options(clear=True)
            print('슬릿 사이 간격 : 기본값 *' + slitdistance + '배')
        if ev.keyCode == 40:
            slitdistance -= 0.25
            print_options(clear=True)
            print('슬릿 사이 간격 : 기본값 *' + slitdistance + '배')
slitdis = slitdis * slitdistance

def make1(r, c, slitdis):
    if c == 0:
        a = extrusion(pos = vec(slitdis/2, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.red, shape=[[shapes.rectangle(pos=[0,0], width=0.4, height=0.1)]], opacity = 0.5)
    else : a = extrusion(pos = vec(slitdis/2, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.blue, shape=[[shapes.rectangle(pos=[0,0], width=0.4, height=0.1)]], opacity = 0.5)
    return a
def make2(r, c, slitdis):
    if c == 0:
        a = extrusion(pos = vec(-slitdis/2, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.red, shape=[[shapes.rectangle(pos=[0,0], width=0.4, height=0.1)]], opacity = 0.5)
    else : a = extrusion(pos = vec(-slitdis/2, 0, r/2), path=paths.arc(radius=r, angle1=-pi, angle2=0), color = color.blue, shape=[[shapes.rectangle(pos=[0,0], width=0.4, height=0.1)]], opacity = 0.5)
    return a
    
def move(x, r, flag, c, slitdis):
    dr = 0.01
    x.visible = False
    r += dr
    if flag == 1 : k = make1(r, c, slitdis)
    else: k = make2(r, c, slitdis)
    return k
    
shape = []
shape2 = []
shapecolor = [] #이거도 공용 사용
r = [] #r은 shape1과 shape2 모두 같음
makecnt = 0
shapecolor.append(0)
shape.append(make1(0.1, 0, slitdis))
shape2.append(make2(0.1, 0, slitdis))
r.append(0.1)
flag = 0

scene.waitfor('click')
print_options(clear=True)
while(True):
    rate(100)
    gdata = []
    term = 20
    if makecnt % term == 0 and makecnt != 0 : 
        shape.append(make1(0.1, int((makecnt // term) % 2), slitdis))
        shape2.append(make2(0.1, int((makecnt // term) % 2), slitdis))
        shapecolor.append(int((makecnt // term) % 2))
        r.append(0.1)
        
    l = len(shape)
    #추가 + 움직이기
    for i in range(l):
        flag = 0
        #if r[i] > scdis * 2.5:
        #    shape[i].visible = False
        #    shape2[i].visible = False
        item = shape[i]
        if item.visible == True :
            shape.append(move(item, r[i], 1, shapecolor[i], slitdis))
            r.append(r[i] + 0.05)
            shapecolor.append(shapecolor[i])          
                    
        item2 = shape2[i]
        if item2.visible == True :
            shape2.append(move(item2, r[i], 0, shapecolor[i], slitdis))
        
    #삭제 (실행속도 빠르게 하기 위해서)
    for i in range(l):
        if i < len(shape) and shape[i].visible == False:
            shape.remove(shape[i])
            r.remove(r[i])
            shapecolor.remove(shapecolor[i])
        if i < len(shape) and shape2[i].visible == False:
            shape2.remove(shape2[i])
    makecnt += 1