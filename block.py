class Block:
    probabilities_of_failure = []

    def __init__(self, lamda, mu, block_number, probabilities_of_failure):
        self.lamda = lamda
        self.mu = mu
        self.block_header = f"Блок {block_number}"
        self.probabilities_of_failure = probabilities_of_failure
