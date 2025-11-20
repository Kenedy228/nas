from tabulate import tabulate


class Presentator:
    def print_block(block):
        headers = ["λ", "μ"]

        for i in range(len(block.probabilities_of_failure)):
            headers.append(f"p[{i+1}]")

        data = [block.lamda, block.mu] + block.probabilities_of_failure

        print(f"\n{block.block_header}\n")
        print(tabulate([data], headers=headers, tablefmt="grid"))

    def print_availability_factors(block, availability_factors):
        headers = []

        for i in range(len(availability_factors)):
            headers.append(f"Кг[{i+1}]")

        data = availability_factors

        print(f"\n{block.block_header}\n")
        print(tabulate([data], headers=headers, tablefmt="grid"))

    def print_ro(block, ro):
        headers = ["ρ"]
        data = [ro]

        print(f"\n{block.block_header}\n")
        print(tabulate([data], headers=headers, tablefmt="grid"))

    def print_numbers_of_service_bodies(block, numbers_of_service_bodies):
        headers = []

        for i in range(len(numbers_of_service_bodies)):
            headers.append(f"n[{i+1}]")

        data = [numbers_of_service_bodies]

        print(f"\n{block.block_header}\n")
        print(tabulate(data, headers=headers, tablefmt="grid"))

    def print_duration_of_transient_processes(block, durations, deltas, time):
        headers = ["t", "p[0]", "p[1]", "p[2]", "Δp[0]"]
        data = []

        t = 0
        for i in range(50):
            data.append(
                [t, durations[0][i], durations[1][i], durations[2][i], deltas[i]]
            )
            t += 0.1

        print(f"\n{block.block_header}\n")
        print(tabulate(data, headers=headers, tablefmt="grid"))
        print(
            f"\nВремя длительности переходного процесса: {"не определено" if time == -1 else f"{time} ч." }\n"
        )

    def print_availability_factors_functions(block, functions_values, times):
        headers = [
            "t",
            "Кг(t)[Блок 1]",
            "Кг(t)[Блок 2]",
            "Кг(t)[Блок 3]",
            "Кг(t)[Блок 4]",
        ]
        data = []

        for i in range(50):
            data.append(
                [
                    times[i],
                    functions_values[0][i],
                    functions_values[1][i],
                    functions_values[2][i],
                    functions_values[3][i],
                ]
            )

        print(f"\nЗначения функции коэффициента готовности\n")
        print(tabulate(data, headers=headers, tablefmt="grid"))
