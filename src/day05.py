from .utils import get_input, info


def seat_id(seat):
    row = seat[:-3]
    row = row.replace("F", "0").replace("B", "1")
    row = int(row, 2)

    column = seat[7:]
    column = column.replace("L", "0").replace("R", "1")
    column = int(column, 2)
    return row * 8 + column


def empty_seats(filled_seats):
    filled_seats = set(filled_seats)
    possible_seats = set()
    for i in range(128):
        for j in range(8):
            seat = i * 8 + j
            if seat not in filled_seats:
                possible_seats.add(seat)

    for seat in possible_seats:
        if (seat + 1) in possible_seats:
            continue
        if (seat - 1) in possible_seats:
            continue
        return seat


def run():
    assert seat_id("FBFBBFFRLR") == 357
    assert seat_id("BFFFBBFRRR") == 567
    assert seat_id("FFFBBBFRRR") == 119
    assert seat_id("BBFFBBFRLL") == 820
    info(max([seat_id(s) for s in get_input(5)]))
    info(empty_seats([seat_id(s) for s in get_input(5)]))
