import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def apply_rule3(l_nb, current_num, r_nb):
    # rule 184 をセットアップ(00011101)
    if l_nb == 0 and current_num == 0 and r_nb == 0:
        return 0
    elif l_nb == 0 and current_num == 0 and r_nb == 1:
        return 0
    elif l_nb == 0 and current_num == 1 and r_nb == 0:
        return 0
    elif l_nb == 1 and current_num == 1 and r_nb == 0:
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
            l_nb = current_state[i - 1]
            r_nb = current_state[(i + 1) % num_cells]
            new_state[i] = apply_rule3(l_nb, current_state[i], r_nb)

        # 状態を更新
        current_state = new_state[:]

    return current_state

if __name__ == "__main__":
    # 初期状態をランダムに設定
    np.random.seed(357)  # シードを参照して再現性を持たせた
    initial_state = np.random.choice([0, 1], size=20)

    # シミュレーションのステップ数を指定
    steps = 20

    # セルオートマトン実装
    final_state = cellular_automation(initial_state, steps)
    print(f"Final State: {final_state}")