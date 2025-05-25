import numpy as np
from config import A, B, STEP

# 시야각 구하는 함수
def theta(h, a=A, b=B):
    """
    `h`: 광고판과 지면 사이의 높이,
    `horizontal_lenth`: 광고판의 가로 길이,
    `height`: 관찰자의 키
    """
    return 2 * np.arctan((a / 2) / (h - b))

def optimize_theta(b=B, step=STEP):
    h_value: float = b + step # 미지수 `h`

    prev_theta = theta(h_value)

    # 극한 구해보기 (컴퓨터 가혹행위)
    while(True):
        cur_theta: float = theta(h_value)

        if cur_theta < prev_theta:
            """
            업데이트된 시야각은 이전 것보다 낮으므로,
            이전 최대 시야각으로 되돌려 놓기
            """
            h_value -= step
            cur_theta = theta(h_value)

            break # 루프 종료
        h_value += step

    print(f"최적의 `h`: {(h_value):.5f} (m)\n")
    print(f"최대 시야각: {np.degrees(cur_theta):.2f} (°)\n")