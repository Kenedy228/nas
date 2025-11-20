from block import *
from presentator import *
from solver import *

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
for i in range(len(blocks)):
    Presentator.print_block(block=blocks[i])

print(
    "\nКоэффициенты готовности для каждого элемента внутри блоков: Кг[n] = 1 - p[n]\n"
)
for i in range(len(blocks)):
    block = blocks[i]
    availability_factors = Solver.find_availability_factors(block)
    Presentator.print_availability_factors(block, availability_factors)

print("\nРо для каждого блока: ρ[n] = λ[n] / μ[n]\n")
for i in range(len(blocks)):
    block = blocks[i]
    ro = Solver.find_ro(block)
    Presentator.print_ro(block, ro)

print("\nЧисло обслуживающих органов для каждого блока\n")
for i in range(len(blocks)):
    block = blocks[i]
    ro = Solver.find_ro(block)

    numbers_of_service_bodies = []
    for j in range(len(block.probabilities_of_failure)):
        factor = block.probabilities_of_failure[j]
        number_of_service_body = Solver.find_number_of_service_body(
            availability_factor=factor, ro=ro
        )
        numbers_of_service_bodies.append(math.ceil(number_of_service_body))

    Presentator.print_numbers_of_service_bodies(
        block, numbers_of_service_bodies=numbers_of_service_bodies
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
block_availability_factors_function_values = []
for i in range(len(blocks)):
    block = blocks[i]
    availability_factors_function_values = Solver.find_availability_factors_function(
        block
    )
    block_availability_factors_function_values.append(
        availability_factors_function_values
    )
times = np.linspace(0, 50 * 0.1, 51)
Presentator.print_availability_factors_functions(
    block=block,
    functions_values=block_availability_factors_function_values,
    times=times,
)
