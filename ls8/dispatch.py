HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
ADD = 0b10100000

class Dispatch():
    def __init__(self):
        self.dispatch = {
            HLT: self.halt,
            LDI: self.load_immediate,
            PRN: self.print,
            MUL: self.multiply,
            PUSH: self.push,
            POP: self.pop,
            CALL: self.call,
            ADD: self.add,
        }

    def run(self, command, cpu):
        return self.dispatch[command](cpu)

    def halt(self, cpu):
        return True

    def call(self, cpu):
        RET = 0b00010001
        prev = cpu.pc
        cpu.pc = cpu.register[cpu.ram_read(cpu.pc+1)]
        while cpu.ram_read(cpu.pc) != RET:
            self.run(cpu.ram_read(cpu.pc), cpu)
            cpu.pc += 1
        cpu.pc = prev + 1

    def load_immediate(self, cpu):
        reg_id = cpu.ram_read(cpu.pc + 1)
        val = cpu.ram_read(cpu.pc + 2)
        cpu.register[reg_id] = val
        cpu.pc += 2

    def print(self, cpu):
        print(cpu.register[cpu.ram_read(cpu.pc + 1)])
        cpu.pc += 1

    def add(selfm, cpu):
        val1 = cpu.ram_read(cpu.pc + 1)
        val2 = cpu.ram_read(cpu.pc + 2)
        cpu.pc += 2
        cpu.register[val1] += cpu.register[val2]
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