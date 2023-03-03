class Disk:

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.free_storage = size
        self.data = []

    def get_storage(self) -> float:
        return self.free_storage
    
    def fill_storage(self, size: int) -> None:
        self.free_storage - size

    def write(self, size:int, data:bytearray = bytearray('No data', encoding='utf-8')) -> None:
        self.fill_storage(size)
        self.data.append(data)

    def read(self) -> bytearray:
        return self.data