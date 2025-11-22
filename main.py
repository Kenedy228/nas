from block import *
from presentator import *
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

print("\nДано\n")
Presentator.print_blocks(blocks)

print(
    "\nКоэффициенты готовности для каждого элемента внутри блоков: Кг[n] = 1 - p[n]\n"
)
availability_factors = []
for i in range(len(blocks)):
    block = blocks[i]
    factors = Solver.find_availability_factors(block)
    availability_factors.append(factors)
Presentator.print_availability_factors(blocks, availability_factors)

print("\nРо для каждого блока: ρ[n] = λ[n] / μ[n]\n")
blocks_ro = []
for i in range(len(blocks)):
    block = blocks[i]
    ro = Solver.find_ro(block)
    blocks_ro.append([ro])
Presentator.print_blocks_ro(blocks, blocks_ro)

print("\nЧисло обслуживающих органов для каждого блока\n")
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
Presentator.print_numbers_of_service_bodies(
    blocks, numbers_of_service_bodies=numbers_of_service_bodies
)

print("\nОпределение длительности переходных процессов для каждого блока\n")
for i in range(len(blocks)):
    block = blocks[i]
    durations, deltas, time = Solver.find_duration_of_transient_processes(
        block.lamda, block.mu
    )
    Presentator.print_duration_of_transient_processes(
        block, durations=durations, deltas=deltas, time=time
    )

print("\nОпределение функции коэффициента готовности для каждого блока\n")
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
Presentator.print_availability_factors_functions(
    blocks=blocks,
    functions=blocks_availability_factors_function,
    times=times,
)
