import numpy as np
import matplotlib as mpl

from config import A, B, STEP
from optimizer import theta, optimize_theta
from graph import draw_graph

# 상수 정의
a = A
b = B
epsilon = STEP

# h 값 범위 설정: b + ε 부터 b + a까지; 1000개의 데이터 생성
h_values = np.linspace(b + epsilon, b + a, 1000)

theta_values = theta(h_values, a, b) # `optimizer.py` 함수 재활용
theta_degrees = np.degrees(theta_values) # 라디안(θ)을 도(°) 단위로 변환


if __name__ == "__main__":
    mpl.rc('font', family='AppleGothic') # for macOS
    # mpl.rc('font', family='Malgun Gothic') # for Windows OS

    optimize_theta() # 최적 `h`값을 계산하여 출력 (`optimizer.py`)
    draw_graph(h_val=h_values, theta_deg=theta_degrees) # 그래프로 시각화 (`graph.py`)
