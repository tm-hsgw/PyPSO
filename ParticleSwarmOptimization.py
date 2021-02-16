import sys
import random
import copy
import numpy as np
import Swarm as swm

target = "Rosenbrock function"

def Main() :
    # 探索を終了する評価値の閾値
    c = sys.float_info.epsilon
    # 最大更新回数
    t = 1000
    # 探索空間
    dim = 2
    min = [-5.12 for _ in range(dim)]
    max = [5.12 for _ in range(dim)]
    # 粒子数
    number = 20

    print(f"target: {target}({len(max)})")
    print("terminate threshold:", c)

    # 探索終了までに要した更新回数と解のタプルを返す
    # t回の更新を経ても評価値がcを下回らなかった場合
    # 求められた最良の解を返す
    # その場合は更新回数の代わりに-1を返す
    result = Solve(c, t, min, max, number)

    print("\ncomplete.")
    print("epochs:", result[0])
    print("solution: ", np.round(result[1], 4))

def Solve(c, t, min, max, number) :
    swarm = swm.Swarm(min, max, number)

    for i in range(t):
        swarm.Move(i)
        if swarm.GlobalBestError < c:
            return i, swarm.GlobalBest

        # print(i, '{:.5e}'.format(swarm.GlobalBestError))
    
    return -1, swarm.GlobalBest

if __name__ == "__main__":
    Main()
