from block import *
from presentator import *
from presentator_builder import *
from solver import *
import numpy as np

blocks = [
    Block(
        lamda=1,
        mu=0.2,
        block_number=1,
        probabilities_of_failure=[0.5, 0.1, 0.05, 0.003],
    ),
    Block(
        lamda=1,
        mu=0.5,
        block_number=2,
        probabilities_of_failure=[0.5, 0.1, 0.05, 0.003],
    ),
    Block(
        lamda=1, mu=1, block_number=3, probabilities_of_failure=[0.5, 0.1, 0.05, 0.003]
    ),
    Block(
        lamda=1, mu=2, block_number=4, probabilities_of_failure=[0.5, 0.1, 0.05, 0.003]
    ),
]

def print_task_initials():
    title = "\nДано\n"
    conclusion = ""
    headers = ["λ", "μ", "p[1]", "p[2]", "p[3]", "p[4]"]
    indexes = []
    data = []

    for i in range(len(blocks)):
        block = blocks[i]
        indexes.append(block.block_header)
        data.append([block.lamda, block.mu] + block.probabilities_of_failure)

    builder = PresentatorBuilder()
    builder.set_title(title)
    builder.set_conclusion(conclusion)
    builder.set_headers(headers)
    builder.set_indexes(indexes)
    builder.set_data(data)

    presentator = builder.build()
    presentator.print_content()

def print_availability_factors():
    availability_factors = []

    for i in range(len(blocks)):
        block = blocks[i]
        factors = Solver.find_availability_factors(block)
        availability_factors.append(factors)
    
    title = "\nКоэффициенты готовности для каждого элемента внутри блоков: Кг[n] = 1 - p[n]\n"
    conclusion = ""
    headers = ["Кг[1]", "Кг[2]", "Кг[3]", "Кг[4]"]
    indexes = []
    data = availability_factors

    for i in range(len(blocks)):
        indexes.append(blocks[i].block_header)

    builder = PresentatorBuilder()
    builder.set_title(title)
    builder.set_conclusion(conclusion)
    builder.set_headers(headers)
    builder.set_indexes(indexes)
    builder.set_data(data)

    presentator = builder.build()
    presentator.print_content()

def print_ro():
    blocks_ro = []
    for i in range(len(blocks)):
        block = blocks[i]
        ro = Solver.find_ro(block)
        blocks_ro.append([ro])
    
    title = "\nРо для каждого блока: ρ[n] = λ[n] / μ[n]\n"
    conclusion = ""
    headers = ["ρ"]
    indexes = []
    data = blocks_ro

    for i in range(len(blocks)):
        indexes.append(blocks[i].block_header)

    builder = PresentatorBuilder()
    builder.set_title(title)
    builder.set_conclusion(conclusion)
    builder.set_headers(headers)
    builder.set_indexes(indexes)
    builder.set_data(data)

    presentator = builder.build()
    presentator.print_content()


def print_number_of_service_bodies():
    numbers_of_service_bodies = []

    for i in range(len(blocks)):
        block = blocks[i]
        ro = Solver.find_ro(block)

        current_number_of_service_body = []
        for j in range(len(block.probabilities_of_failure)):
            probability_of_failure = block.probabilities_of_failure[j]
            number_of_service_body = Solver.find_number_of_service_body(
                probability_of_failure=probability_of_failure, ro=ro
            )
            current_number_of_service_body.append(math.ceil(number_of_service_body))
        numbers_of_service_bodies.append(current_number_of_service_body)

    title = "\nЧисло обслуживающих органов для каждого блока\n"
    conclusion = ""
    headers = ["n[1]", "n[2]", "n[3]", "n[4]"]
    indexes = []
    data = numbers_of_service_bodies

    for i in range(len(blocks)):
        indexes.append(blocks[i].block_header)
    
    builder = PresentatorBuilder()
    builder.set_title(title)
    builder.set_conclusion(conclusion)
    builder.set_headers(headers)
    builder.set_indexes(indexes)
    builder.set_data(data)

    presentator = builder.build()
    presentator.print_content()

def print_duration_of_transient_processes():
    for i in range(len(blocks)):
        block = blocks[i]
        durations, deltas, time = Solver.find_duration_of_transient_processes(
            block.lamda, block.mu
        )

        title = f"\nОпределение длительности переходных процессов для блока: {block.block_header}\n"
        headers = ["t", "p[0]", "p[1]", "p[2]", "Δp[0]"]
        indexes = []
        data = []

        t = 0
        for i in range(50):
            data.append(
                [t, durations[0][i], durations[1][i], durations[2][i], deltas[i]]
            )
            t += 0.1

        conclusion = f"\nВремя длительности переходного процесса: {"не определено" if time == -1 else f"{time} ч."}\n"

        builder = PresentatorBuilder()
        builder.set_title(title)
        builder.set_headers(headers)
        builder.set_conclusion(conclusion)
        builder.set_indexes(indexes)
        builder.set_data(data)

        presentator = builder.build()
        presentator.print_content()

def print_availability_factor_functions():
    blocks_availability_factors_function = []
    times = np.linspace(0, 50 * 0.1, 51)
    for i in range(len(blocks)):
        block = blocks[i]
        availability_factors_function_values = Solver.find_availability_factors_function(
            block,
            times
        )
        blocks_availability_factors_function.append(
            availability_factors_function_values
        )

    title = "\nОпределение функции коэффициента готовности для каждого блока\n"
    conclusion = ""
    headers = ["t", "Кг(t)[Блок 1]", "Кг(t)[Блок 2]", "Кг(t)[Блок 3]", "Кг(t)[Блок 4]"]
    indexes = []
    data = []

    for i in range(50):
        data.append(
            [times[i],
            blocks_availability_factors_function[0][i],
            blocks_availability_factors_function[1][i],
            blocks_availability_factors_function[2][i],
            blocks_availability_factors_function[3][i]
            ])

    builder = PresentatorBuilder()
    builder.set_title(title)
    builder.set_headers(headers)
    builder.set_conclusion(conclusion)
    builder.set_indexes(indexes)
    builder.set_data(data)

    presentator = builder.build()
    presentator.print_content()

print_task_initials()
print_availability_factors()
print_ro()
print_number_of_service_bodies()
print_duration_of_transient_processes()
print_availability_factor_functions()
