from __future__ import annotations

class NormalCustomer:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def get_customer(self)-> str:
        return f"Customer {self.name}'s status is {self.status}"

def igwt()->str:
    return "In God We Trust"

if __name__ == "__main__":
    print(f"{igwt()}")

    my_normal_customer = NormalCustomer("Hit Monkey", "Alive")

    print(my_normal_customer.get_customer())