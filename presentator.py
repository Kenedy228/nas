from tabulate import tabulate


class Presentator:

    def print_blocks(blocks):
        headers = ["λ", "μ", "p[1]", "p[2]", "p[3]", "p[4]"]
        indexes = []
        data = []

        for i in range(len(blocks)):
            block = blocks[i]
            indexes.append(block.block_header)
            data.append([block.lamda, block.mu] + block.probabilities_of_failure)

        print(tabulate(data, headers=headers, showindex=indexes, tablefmt="grid"))

    def print_availability_factors(blocks, availability_factors):
        headers = ["Кг[1]", "Кг[2]", "Кг[3]", "Кг[4]"]
        indexes = []
        data = availability_factors

        for i in range(len(blocks)):
            indexes.append(blocks[i].block_header)

        print(tabulate(data, headers=headers, showindex=indexes, tablefmt="grid"))

    def print_blocks_ro(blocks, blocks_ro):
        headers = ["ρ"]
        indexes = []
        data = blocks_ro

        for i in range(len(blocks)):
            indexes.append(blocks[i].block_header)

        print(tabulate(data, headers=headers, showindex=indexes, tablefmt="grid"))

    def print_numbers_of_service_bodies(blocks, numbers_of_service_bodies):
        headers = ["n[1]", "n[2]", "n[3]", "n[4]"]
        indexes = []
        data = numbers_of_service_bodies

        for i in range(len(blocks)):
            indexes.append(blocks[i].block_header)

        print(tabulate(data, headers=headers, showindex=indexes, tablefmt="grid"))

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
            f"\nВремя длительности переходного процесса: {"не определено" if time == -1 else f"{time} ч."}\n"
        )

    def print_availability_factors_functions(blocks, functions, times):
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
                    functions[0][i],
                    functions[1][i],
                    functions[2][i],
                    functions[3][i],
                ]
            )

        print(tabulate(data, headers=headers, tablefmt="grid"))
