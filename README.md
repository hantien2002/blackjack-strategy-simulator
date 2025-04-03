# Blackjack Strategy Simulator

A Python-based simulation framework to test and compare custom blackjack strategies over multiple full-deck cycles. Designed to measure actual win rates, move frequencies, and profit under controlled rules and betting systems.

Aim to find the answer to the following questions:
- What is the true win rate of [basic strategy](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/)?
- Is there a better trategy than the basic strategy?

Furthermore, we aim to find the expected profit of two betting strategy, 1) Flat Betting, 2) Streak-Based Progression.

## How to Run
```bash
python main.py --strategy strategies/basic_strategy.json --cycles 100
```