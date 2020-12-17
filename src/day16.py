from .utils import *

sample = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".splitlines()

sample2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9""".splitlines()


class Parser:
    def __init__(self, inp):
        self.fields = {}
        self.my_ticket = None
        self.nearby_tickets = []
        self.position_options = []
        self._parse_fields(inp)
        self._parse_tickets(inp)

        self._set_poistion_options()
        # info(self.fields)
        # info(self.my_ticket)
        # info(self.nearby_tickets)

    def get_result(self):
        for ticket in self.valid_tickets():
            # info(ticket)
            for pos, val in enumerate(ticket):
                for field in self.fields:
                    frst, scnd = self.fields[field]
                    if frst[0] <= val <= frst[1] or scnd[0] <= val <= scnd[1]:
                        ...
                    else:
                        if field in self.position_options[pos]:
                            self.position_options[pos].remove(field)
        parsed = set()
        ssm = 1
        while True:
            try:
                pos, val = next(
                    (i, f[0])
                    for i, f in enumerate(self.position_options)
                    if len(f) == 1 and f[0] not in parsed
                )
            except:
                break
            parsed.add(val)
            info(pos, val, self.my_ticket[pos])
            if "departure" in val:
                ssm *= self.my_ticket[pos]

            # self.position_options.pop(pos)
            for vals in self.position_options:
                if val in vals:
                    vals.remove(val)
        return ssm

        create_tasks_location_attributes = AttributeCriteriaFilter(
            boolean_operator=CriteriaFilterSetOperator.OR,
            filters=[
                AttributeCriteriaFilter(
                    LocationAttributeType.DELIVERY_DAY,
                    CriteriaOperator.EQ,
                    value="Monday",
                )
            ],
        )

    def _set_poistion_options(self):
        for _ in self.my_ticket:
            self.position_options.append(list(self.fields))

    def error_rate(self):
        return sum(self.error_values())

    def error_values(self):
        for ticket in self.nearby_tickets:
            for val in ticket:
                for frst, scnd in self.fields.values():
                    if frst[0] <= val <= frst[1] or scnd[0] <= val <= scnd[1]:
                        break
                else:
                    yield val

    def valid_tickets(self):
        for ticket in self.nearby_tickets:
            for i, val in enumerate(ticket):
                for field in self.fields:
                    frst, scnd = self.fields[field]
                    if frst[0] <= val <= frst[1] or scnd[0] <= val <= scnd[1]:
                        break
                else:
                    break
            else:
                yield ticket

    def _parse_tickets(self, inp):
        for line in inp:
            tickets = line.split(",")
            if len(tickets) == 1:
                continue
            if self.my_ticket is None:
                self.my_ticket = self._parse_ticket_line(tickets)
                continue
            self.nearby_tickets.append(self._parse_ticket_line(tickets))

    def _parse_ticket_line(self, ticket):
        return [int(t) for t in ticket]

    def _parse_fields(self, inp):
        for line in inp:
            if line == "":
                break
            name, values = line.split(": ")
            frst, scnd = values.split(" or ")
            self.fields[name] = [
                self._parse_field_vals(frst),
                self._parse_field_vals(scnd),
            ]

    def _parse_field_vals(self, val):
        frst, scnd = val.split("-")
        return (int(frst), int(scnd))


def run():
    assert Parser(sample).error_rate() == 71
    info(Parser(get_input(16)).error_rate())

    Parser(sample2).get_result()
    info(Parser(get_input(16)).get_result())
