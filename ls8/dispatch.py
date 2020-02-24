HLT = 0b00000001
LDI = 0b10000010
PRN = 0b01000111

class Dispatch():
    def __init__(self):
        self.dispatch = {
            HLT: self.halt,
            LDI: self.load_immediate,
            PRN: self.print,
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