class LimitedStack:
    def __init__(self, k):
        self.stack = []  # Дарааллын өгөгдөл хадгалах массив
        self.k = k  # Дарааллын хамгийн их хэмжээ
        self.total_operations = 0  # Нийт үйлдлийн тоо

    def push(self, value):
        """
        Push үйлдэл: Дараалалд элемент нэмнэ.
        """
        if len(self.stack) >= self.k:
            print("Push failed: Stack overflow")
            return

        self.stack.append(value)
        self.total_operations += 1  # Нийт үйлдлийг тооцох
        print(f"Push: {value} added. Total operations: {self.total_operations}")

    def pop(self):
        """
        Pop үйлдэл: Дарааллаас элемент гаргана.
        """
        if not self.stack:
            print("Pop failed: Stack is empty")
            return None

        value = self.stack.pop()
        self.total_operations += 1  # Нийт үйлдлийг тооцох
        print(f"Pop: {value} removed. Total operations: {self.total_operations}")
        return value

    def simulate_copy(self):
        """
        Хуулбарлалтын үйлдэл: Дарааллын бүх элементүүдийг хуулбарлана.
        """
        self.total_operations += len(self.stack)  # Хуулбарлалтын өртөг
        print(f"Simulated copy: {len(self.stack)} elements copied.")

    def total_cost(self):
        """
        Нийт өртгийг буцаах.
        """
        return self.total_operations


# Жишээ ашиглалт
k = 5  # Дарааллын хамгийн их хэмжээ
stack = LimitedStack(k)

# Push үйлдлүүд
stack.push(1)
stack.push(2)
stack.push(3)

# Хуулбарлалт хийх
stack.simulate_copy()

# Pop үйлдлүүд
stack.pop()
stack.pop()

# Нийт өртгийг шалгах
print(f"Нийт үйлдэл: {stack.total_cost()}")
