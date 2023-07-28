import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# cn = current_number
def apply_rule5(l2, l1, cn, r1, r2):
    # fastcase をセットアップ(11011100110011111100110011000000)
    if l2 == 0 and l1 == 0 and cn == 0 and r1 == 0 and r2 == 0: # 00000
        return 0
    elif l2 == 0 and l1 == 0 and cn == 0 and r1 == 0 and r2 == 1: # 00001
        return 0
    elif l2 == 0 and l1 == 0 and cn == 0 and r1 == 1 and r2 == 0: # 00010
        return 0
    elif l2 == 0 and l1 == 0 and cn == 0 and r1 == 1 and r2 == 1: # 00011
        return 0
    elif l2 == 0 and l1 == 0 and cn == 1 and r1 == 0 and r2 == 0: # 00100
        return 0
    elif l2 == 0 and l1 == 0 and cn == 1 and r1 == 0 and r2 == 1: # 00101
        return 0
    elif l2 == 0 and l1 == 1 and cn == 0 and r1 == 0 and r2 == 0: # 01000
        return 0
    elif l2 == 0 and l1 == 1 and cn == 0 and r1 == 0 and r2 == 1: # 01001
        return 0
    elif l2 == 0 and l1 == 1 and cn == 1 and r1 == 0 and r2 == 0: # 01100
        return 0
    elif l2 == 0 and l1 == 1 and cn == 1 and r1 == 0 and r2 == 1: # 01101
        return 0
    elif l2 == 1 and l1 == 0 and cn == 1 and r1 == 0 and r2 == 0: # 10100
        return 0
    elif l2 == 1 and l1 == 0 and cn == 1 and r1 == 0 and r2 == 1: # 10101
        return 0
    elif l2 == 1 and l1 == 1 and cn == 0 and r1 == 0 and r2 == 0: # 11000
        return 0
    elif l2 == 1 and l1 == 1 and cn == 0 and r1 == 0 and r2 == 1: # 11001
        return 0
    elif l2 == 1 and l1 == 1 and cn == 1 and r1 == 0 and r2 == 1: # 11101
        return 0
    else:
        return 1
def cellular_automation(initial_state, steps):
    # 初期状態をセットアップ
    current_state = initial_state[:]
    num_cells = len(current_state)
    new_state = [0] * num_cells  # 初期化

    for step in range(steps):
        print(f"Step {step + 1}: {current_state}")

        # 新しい状態を計算
        for i in range(num_cells):
            # 周期境界条件を適用
            l2 = current_state[i - 2]
            l1 = current_state[i - 1]
            r1 = current_state[(i + 1) % num_cells]
            r2 = current_state[(i + 2) % num_cells]
            new_state[i] = apply_rule5(l2, l1, current_state[i],r1, r2)

        # 状態を更新
        current_state = new_state[:]

    return current_state

if __name__ == "__main__":
    # 初期状態をランダムに設定
    np.random.seed(480)  # シードを参照して再現性を持たせた
    initial_state = np.random.choice([0, 1], size=20)

    # シミュレーションのステップ数を指定
    steps = 20

    # セルオートマトン実装
    final_state = cellular_automation(initial_state, steps)
    print(f"Final State: {final_state}")
