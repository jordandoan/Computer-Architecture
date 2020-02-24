"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * (2 ** 8)
        self.register = [0] * 8
        self.register[-1] = 0xF4
        self.pc = 0

    def ram_read(self, memory):
        return self.ram[memory]

    def ram_write(self, memory, value):
        self.ram[memory] = value

    def load(self):
        """Load a program into memory."""

        address = 0
        try:
            path = sys.argv[1]
        except:
            path = 'examples/print8.ls8'
        with open(path, 'r') as program:
            for instruction in program:
                if len(instruction) > 1:
                    if instruction[0] != '#':
                        self.ram[address] = int(instruction[0:8],2)
                        address += 1

    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        # elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            # self.fl,
            # self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()

    def run(self):
        """Run the CPU."""
        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111

        while True:
            command = self.ram_read(self.pc)

            if command == HLT:
                break
            elif command == LDI:
                reg_id = self.ram_read(self.pc + 1)
                val = self.ram_read(self.pc + 2)
                self.register[reg_id] = val
                self.pc += 2
            elif command == PRN:
                print(self.register[self.ram_read(self.pc + 1)])
                self.pc += 1
            self.pc += 1