from scipy.optimize import fsolve
from scipy.special import gamma
import math
import numpy as np
from scipy.integrate import solve_ivp


class Solver:
    # поиск коэффициента готовности
    def find_availability_factors(block):
        availabitility_factors = []

        for i in range(len(block.probabilities_of_failure)):
            probability = block.probabilities_of_failure[i]
            availabitility_factors.append(1 - probability)

        return availabitility_factors

    # поиск ро
    def find_ro(block):
        return block.lamda / block.mu

    # поиск числа обслуживающих органов
    def find_number_of_service_body(probability_of_failure, ro):

        # определение функции для поиска значения n
        def equation(n):
            numerator = ro**n / gamma(n + 1)
            denominator = sum(ro**i / gamma(i + 1) for i in range(int(n) + 1))
            return numerator / denominator - probability_of_failure

        n_initial_guess = ro
        n_solution = fsolve(equation, n_initial_guess)
        return n_solution

    # поиск длительности переходных процессов
    def find_duration_of_transient_processes(lamda, mu):
        def find_durations():
            def system(t, p):
                p0, p1, p2 = p
                dp0 = -lamda * p0 + mu * p1
                dp1 = lamda * p0 - (lamda + mu) * p1 + 2 * mu * p2
                dp2 = lamda * p1 - 2 * mu * p2
                return [dp0, dp1, dp2]

            t_span = (0, 50 * 0.1)
            t_eval = np.linspace(0, 50 * 0.1, 51)

            p0 = [1, 0, 0]  # начальные условия

            solution = solve_ivp(system, t_span, p0, t_eval=t_eval, method="RK45")

            return solution.y

        def find_deltas(durations):
            deltas = [1e10]

            for i in range(1, len(durations[0])):
                d = abs(durations[0][i] - durations[0][i - 1])
                deltas.append(d)

            return deltas

        def find_time(deltas):
            epsilon = 1e-4
            times = np.linspace(0, 50 * 0.1, 51)

            for i in range(1, len(deltas)):
                delta = abs(deltas[i] - deltas[i - 1])

                if delta < epsilon:
                    return times[i]
            return -1

        durations = find_durations()
        deltas = find_deltas(durations=durations)
        time = find_time(deltas=deltas)

        return durations, deltas, time

    # поиск значений функции коэффициента готовности
    def find_availability_factors_function(block, times):
        function_values = []

        for i in range(50):
            value = (block.mu / (block.lamda + block.mu)) + (
                block.mu / (block.lamda + block.mu)
            ) * math.exp(-1 * (block.lamda + block.mu) * times[i])

            function_values.append(value)

        return function_values
