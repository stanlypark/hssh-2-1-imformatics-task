# Vpython을 통한 이중슬릿에 의한 간섭 모의실험
#### Visual Implementation of Dual Slit Interference Experiment Using Vpython
2212 박영진, 2219 이현수의 2019 2학년 1학기 정보 수행평가입니다.

![main](https://user-images.githubusercontent.com/40256530/59174213-7b7cc400-8b8b-11e9-97dc-85d94fb1b48a.JPG)

### [개요]

저희는 물리학 분야에서 파동의 간섭과 영의 이중슬릿 실험을 공부할 때, 그 현상을 잘 이해하지 못하고 파동이 직접 전파해 나가는 모습을 궁금해 하는 학생들을 위해서, 모의 실험을 Vpython 으로 설계하였습니다. 파동이 전파되는 모습부터, 어떤 원리로 슬릿에 극대/극소 무늬가 나타나는지, 조건이 변화할 때 그 무늬와 에너지 준위가 어떻게 되는지를 관찰할 수 있게 설계하였고 이를 이론과 비교하는 과정 역시 포함하고 있습니다.

Young's double-slit interference experiments were visualized and simulated by Vpython for students who did not understand the wave interference or were unable to recognize it by direct visual confirmation. In addition, graphs of interference fringes and energy levels are implemented, making it easier for students to see and understand them.

### [프로젝트 설명 영상]

https://youtu.be/HDwkwipLS2g 

### [각 파일 설명]

1) slit_ball.py : 공으로 파동의 전파 모습을 표현, 보강/상쇄간섭 위치 관찰가능

2) waves.py : 파동이 움직이고 전파되는 모습을 표현 (이동하는 모습 관찰가능)

3) slit_waves.py : 스크린에 보강/상쇄 간섭점이 나타나고 그 에너지 준위를 볼 수 있음. 또한, 스크린까지의 거리, 슬릿간의 거리, 파장을 변화시키면서 그 무늬의 변화를 관찰할 수 있음.
