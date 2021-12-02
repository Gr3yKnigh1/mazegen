class Vector2Int(list):

    def __init__(self, x: int, y: int) -> None:
        self.extend((x, y))

    @property
    def x(self) -> int:
        return self[0]

    @property
    def y(self) -> int:
        return self[1]
