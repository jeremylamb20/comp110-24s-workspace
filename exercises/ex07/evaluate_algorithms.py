__author__ = "730461078"

from exercises.ex07.runtime_analysis_functions import evaluate_runtime, evaluate_memory_usage
import matplotlib.pyplot as plt

START_SIZE: int = 0
END_SIZE: int = 1000

times = evaluate_runtime("selection_sort", START_SIZE, END_SIZE)
plt.plot(times)
plt.title("Runtime Analysis of Selection Sort - 730461078")
plt.show()