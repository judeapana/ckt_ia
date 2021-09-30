import string
from pprint import pprint


class Hall:
    def __init__(self, rows, cols=None, courses=None):
        self.rows = rows
        self.courses = courses
        if cols:
            cols = list(string.ascii_uppercase)[:cols]
        self.cols = cols
        self.courses = courses


class Seat:
    def __init__(self, row, col, student=None):
        self.row = row
        self.col = col
        self.student = student

    @property
    def descriptor(self):
        return f"{self.row}{self.col}"

    def __repr__(self):
        return f"Descriptor <{self.descriptor}>"


class SeatAssigner:
    def __init__(self, hall: Hall):
        self.hall = hall
        self._blueprint = []
        self._placement = []

    @property
    def available_seats(self):
        return len(self._blueprint)

    def blueprint(self):
        for row in range(1, self.hall.rows + 1):
            for col in self.hall.cols:
                self._blueprint.append(Seat(col=col, row=row))
        return self._blueprint

    def placement(self, col, students):
        data = []
        pos = list(filter(lambda x: x.col == col, self._blueprint))
        for seat, student in list(zip(pos, students)):
            seat.student = student
            data.append(seat)
        return data


# range(len(students), len(pos) + 1), len(pos) - len(students)

if __name__ == "__main__":
    _students_mth101 = ['STUDENT 1', 'STUDENT 2', 'STUDENT 3']
    _students_csc401 = ['STUDENT 4', 'STUDENT 5', 'STUDENT 6']
    _hall = Hall(rows=10, cols=2)
    seatarr = SeatAssigner(_hall)
    # seatarr.blueprint()
    pprint(seatarr.blueprint())
    # print(seatarr.placement("A", _students_csc401))
    # print(seatarr.placement("B", _students_csc401))
