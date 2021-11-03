import hashlib

class FECoin:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

tr1 = "Fatih sends 5 FE to Emirhan"
tr2 = "Tom sends 20 FE to Angelina"
tr3 = "Ahmet sends 8 FE to Kristin"
tr4 = "Fatih sends 3 FE to Hakmansoor"
tr5 = "Kristin sends 1 FE to Tom"
tr6 = "Ali sneds 2 FE to Baver"

initial_block = FECoin("Initial String", [tr1, tr2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = FECoin(initial_block.block_hash, [tr3, tr4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = FECoin(second_block.block_hash, [tr5, tr6])

print(third_block.block_data)
print(third_block.block_hash)

'''dünyanın en iyi yazılımcısı'''