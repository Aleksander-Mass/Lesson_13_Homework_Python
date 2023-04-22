# Доработайте классы исключения так, чтобы они выдали
# подробную информацию об ошибках.
# Передавайте необходимые данные из основного кода
# проекта.

class SideValueError(Exception):
    def __init__(self, side):
        self.value = side

    def __str__(self):
        return f"Сторона должна быть больше 0. Получено значение = {self.value}"


class SideTypeError(Exception):
    def __init__(self, side):
        self.value = side

    def __str__(self):
        return f"Сторона должна иметь тип int/float. Переданный тип {type(self.value)}"


class Rectangle:
    def __init__(self, side_a: float, side_b: float = None):
        if not isinstance(side_a, int | float):
            raise SideTypeError(side_a)

        if not isinstance(side_b, int | float):
            raise SideTypeError(side_b)

        if side_a < 0:
            raise SideValueError(side_a)

        if side_b < 0:
            raise SideValueError(side_b)

        self.side_a = side_a
        self.side_b = side_a if side_b is None else side_b
        self._area = self.side_a * self.side_b
        self._long = 2 * (self.side_a + self.side_b)

    def get_area(self) -> float:
        return self._area

    def get_long(self) -> float:
        return self._long

    def __add__(self, other):
        new_long = self._long + other._long
        new_a = self.side_a + other.side_a
        new_b = new_long / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        new_long = abs(self._long - other._long)
        new_a = abs(self.side_a - other.side_a)
        new_b = new_long / 2 - new_a
        return Rectangle(new_a, new_b)

    def __ne__(self, other):
        return self._area != other._area

    def __gt__(self, other):
        return self._area > other._area

    def __eq__(self, other):
        return self._area == other._area

    def __lt__(self, other):
        return self._area < other._area

    def __ge__(self, other):
        return self._area >= other._area

    def __le__(self, other):
        return self._area <= other._area

    def __str__(self):
        return f'Класс создает прямоугольник с параметрами: длина = {self.side_a} ' + \
               f'ширина = {self.side_b}, периметр = {self._long}, площадь = {self._area}'

    def __repr__(self):
        return f'(Rectangle{self.side_a}, {self.side_b}, {self._long}, {self._area})'


if __name__ == '__main__':
    # rectangle = Rectangle(-3, 9)

    rectangle = Rectangle('True', 9)