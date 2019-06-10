from vpython import *
#GlowScript 2.7 VPython
#Vpython 에서 실행해 주세요.

print('슬릿사이 간격 n배 설정.')
slitdistance = 1
scdistance = 1
wavelength = 0.5
l = 5
floor = box(pos = vec(-l/2, 0, 0), length = l, height = 0.5, width = 0.4, color = color.yellow)
#슬릿사이 간격설정
while(True):
    ev = scene.waitfor('click keydown') 
    if ev.event == 'click':
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
scene.waitfor('click')

#스크린과의 간격설정
print('스크린과의 간격 n배 설정.')
while(True):
    ev = scene.waitfor('click keydown') 
    if ev.event == 'click':
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
scene.waitfor('click')

#floor.visible = False
ballorigin = sphere(pos = vector(0, 0, 0), radius = 1, color = color.yellow)
ballstart = sphere(pos = vector(-l, 0, 0), radius = 1)
floor1 = box(pos = vector(0, 0, -(slitdistance * 2.5 + 7.5) - 2), length = 1, height = 2, width = 15, color = color.white)
floor2 = box(pos = vector(0, 0, 0), length = 1, height = 2, width = slitdistance * 5, color = color.white)
floor3 = box(pos = vector(0, 0, slitdistance * 2.5 + 7.5 + 2), length = 1, height = 2, width = 15, color = color.white)
screen = box(pos = vector(10 * scdistance, 0, 0), length = 1, height = 0.5, width = 30 + slitdistance * 5 + 4)
print_options(clear=True)
scene.waitfor('click')
##물결모양으로 파형 그리는 과정
i = -1
cnt = -1
j = -1
cnt2 = -1
di = 0.05
dj = 0.15
flag = True
while(True):
    print_options(clear=True)
    rate(20)
    cnt = cnt - 1
    i = cnt
    if not flag :
        cnt2 = cnt2 - 0.8
        j = cnt2
    place1 = {}
    place2 = {}
    while(i <= cnt * (-1)):
        #바깥쪽 간섭하는 파형 그리기
        if flag and sqrt(cnt*cnt - i*i) - l < 0 and abs(i) < slitdistance * 2.5 + 10 :
            p = sphere(pos = vector(sqrt(cnt*cnt-i*i) - l, 0, i), radius = 0.1, color = color.blue) 
        if i > 2.5 * scdistance and abs(cnt) > l: flag = False
        if flag == False :
            #안쪽에서 간섭하는 파형이 시작된다
            if sqrt(cnt2*cnt2-j*j) < scdistance * 10:
                if -15 < j - slitdistance * 2.5 - 1 < 15: 
                    p1 = sphere(pos = vector(sqrt(cnt2*cnt2-j*j), 0, j - slitdistance * 2.5 - 1), radius = 0.18, color = color.blue, opacity = 0.3)
                    if cnt % 2 != 0: p1.color = color.red
                    place1[p1.pos.x] = p1.pos.z
                if -15 < slitdistance * 2.5 + 1 - j < 15: 
                    p2 = sphere(pos = vector(sqrt(cnt2*cnt2-j*j), 0, slitdistance * 2.5 + 1 - j), radius = 0.18, color = color.blue, opacity = 0.3)
                    if cnt % 2 != 0 : p2.color = color.red
                    place2[p2.pos.x] = p2.pos.z
            j += dj
        i += di
    indexcnt = 0
    #scene.waitfor('click')
