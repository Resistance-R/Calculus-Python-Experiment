import matplotlib.pyplot as plt

from config import A, B

"""
그래프 그리기
"""
def draw_graph(h_val, theta_deg, a=A, b=B):
    plt.plot(h_val, theta_deg, label=r"$\theta(h)$")
    plt.axhline(90, color='gray', linestyle='--', label="90° 기준선")
    plt.axvline(b + a/2, color='red', linestyle='--', label=r"$h = b + a/2$ (90° 지점)")

    plt.title("광고판 설치 높이 h에 따른 시야각 변화")
    plt.xlabel("광고판 높이 h (m)")
    plt.ylabel("시야각 θ (도)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()