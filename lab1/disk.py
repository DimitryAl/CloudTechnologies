class Disk:

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.storage = size
        self.data = []

    def write(self, data:bytearray = bytearray('No data', encoding='utf-8')) -> None:
        self.data.append(data)

    def read(self) -> bytearray:
        return self.data