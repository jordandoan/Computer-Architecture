HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
class Dispatch():
    def __init__(self):
        self.dispatch = {
            HLT: self.halt,
            LDI: self.load_immediate,
            PRN: self.print,
            MUL: self.multiply,
            PUSH: self.push,
            POP: self.pop
        }

    def run(self, command, cpu):
        return self.dispatch[command](cpu)

    def halt(self, cpu):
        return True

    def load_immediate(self, cpu):
        reg_id = cpu.ram_read(cpu.pc + 1)
        val = cpu.ram_read(cpu.pc + 2)
        cpu.register[reg_id] = val
        cpu.pc += 2

    def print(self, cpu):
        print(cpu.register[cpu.ram_read(cpu.pc + 1)])
        cpu.pc += 1

    def multiply(self, cpu):
        val1 = cpu.ram_read(cpu.pc + 1)
        val2 = cpu.ram_read(cpu.pc + 2)
        cpu.pc += 2
        print(cpu.register[val1] * cpu.register[val2])

    def push(self, cpu):
        register = cpu.ram_read(cpu.pc + 1)
        val = cpu.register[register]
        cpu.ram_write(cpu.sc, val)
        cpu.sc -= 1
        cpu.pc += 1

    def pop(self, cpu):
        top = cpu.ram_read(cpu.sc+1)
        register = cpu.ram_read(cpu.pc + 1)
        cpu.register[register] = top
        cpu.ram_write(cpu.sc, 0)
        cpu.sc += 1
        cpu.pc += 1