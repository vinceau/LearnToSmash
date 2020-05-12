import argparse
import numpy as np
import matplotlib.pyplot as plt


def ema(x, alpha=0.99):
    y = np.zeros_like(x)
    y[0] = x[0]
    for i in range(1, len(x)):
        y[i] = alpha*y[i-1] + (1-alpha) * x[i]
    return y


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', type=str, default="results/latest/reward.txt", help='file to display')
    parser.add_argument('-b', '--begin', type=int, default=0, metavar='N', help='plot starts at epoch s (default: 0)')
    parser.add_argument('-s', '--smooth', type=float, default=0.97, metavar='N', help='exponential moving average parameters. <1 (default: 0)')
    args = parser.parse_args()

    reward = np.genfromtxt(args.file, delimiter=',')

    plt.plot(reward[args.begin:, 0], reward[args.begin:, 1], alpha=0.3)
    plt.plot(reward[args.begin:, 0], ema(reward[args.begin:, 1], args.smooth), alpha=0.3)
    plt.show()