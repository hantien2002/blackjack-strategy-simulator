import argparse
import json
from simulation import Simulation


def main():
    parser = argparse.ArgumentParser(description="Blackjack Simulator")
    parser.add_argument("--strategy", type=str, required=True, help="Path to strategy JSON file")
    parser.add_argument("--cycles", type=int, default=100, help="Number of full-deck cycles to run")
    parser.add_argument("--betting", type=str, choices=["flat", "streak"], default="flat", help="Betting system to use")
    parser.add_argument("--output", type=str, help="Path to JSON output file")
    args = parser.parse_args()

    with open(args.strategy) as f:
        strategy_data = json.load(f)

    sim = Simulation(strategy_data, args.betting, args.cycles)
    results, profits = sim.run()

    if args.output:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
    else:
        for k, v in results.items():
            print(f"{k}: {v}")

        import matplotlib.pyplot as plt
        plt.plot(profits)
        plt.title("Profit per Cycle")
        plt.xlabel("Cycle")
        plt.ylabel("Profit ($)")
        plt.grid()
        plt.show()


if __name__ == "__main__":
    main()
