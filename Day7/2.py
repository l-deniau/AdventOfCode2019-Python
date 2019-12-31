import sys
import os
import itertools

class Computer:

    class State:
        init = 0
        running = 1
        done = 2

    def __init__(self, intcode, phase_setting):
        self.intcode = intcode
        self.actual_state = self.State.init
        self.phase_setting = phase_setting
        self.pointer = 0
        self.phase_setting_consumed = False
        self.output_signal = 0

    def isDone(self):
        return self.actual_state == self.State.done

    def run(self, input_signal):
        self.actual_state = self.State.running
        while self.pointer < len(self.intcode):
            first_int = self.intcode[self.pointer]
            opcode = first_int % 100
            first_param_mode = int(first_int/100%10)
            second_param_mode = int(first_int/1000%10)
            # third_param_mode = int(first_int/10000%10)
            if opcode == 1:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                self.intcode[self.intcode[self.pointer+3]] = first_param + second_param
                self.pointer += 4
            elif opcode == 2:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                self.intcode[self.intcode[self.pointer+3]] = first_param * second_param
                self.pointer += 4
            elif opcode == 3:
                if not self.phase_setting_consumed:
                    self.intcode[self.intcode[self.pointer+1]] = self.phase_setting
                    self.phase_setting_consumed = True
                else:
                    self.intcode[self.intcode[self.pointer+1]] = input_signal
                self.pointer += 2
            elif opcode == 4:
                self.output_signal = self.intcode[self.intcode[self.pointer+1]]
                self.pointer += 2
                break
            elif opcode == 5:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                if first_param: self.pointer = second_param
                else: self.pointer += 3
            elif opcode == 6:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                if not first_param: self.pointer = second_param
                else: self.pointer += 3
            elif opcode == 7:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                self.intcode[self.intcode[self.pointer+3]] = 1 if first_param < second_param else 0
                self.pointer += 4
            elif opcode == 8:
                first_param = self.intcode[self.pointer+1] if first_param_mode else self.intcode[self.intcode[self.pointer+1]]
                second_param = self.intcode[self.pointer+2] if second_param_mode else self.intcode[self.intcode[self.pointer+2]]
                self.intcode[self.intcode[self.pointer+3]] = 1 if first_param == second_param else 0
                self.pointer += 4
            elif opcode == 99:
                self.actual_state = self.State.done
                break
            else:
                print("Error")
                print("last iteration :")
                print(self.pointer)
                print("opcode :")
                print(opcode)
                sys.exit()


def main():
    input_file_path = sys.argv[1]

    if not os.path.isfile(input_file_path):
       print(int("File path {} does not exist. Exiting...".format(input_file_path)))
       sys.exit()

    intcode_raw = open(input_file_path, 'r').readline()
    intcode_string = intcode_raw.split(",")
    initial_intcode = [int(char) for char in intcode_string]

    phase_setting_combinations = list(itertools.permutations([5,6,7,8,9], 5))
    final_output_signal_list = []

    for phase_setting_combination in phase_setting_combinations:
        engine_list = [
            Computer(initial_intcode.copy(), phase_setting_combination[0]),
            Computer(initial_intcode.copy(), phase_setting_combination[1]),
            Computer(initial_intcode.copy(), phase_setting_combination[2]),
            Computer(initial_intcode.copy(), phase_setting_combination[3]),
            Computer(initial_intcode.copy(), phase_setting_combination[4])
        ]
        input_signal = 0
        for engine in itertools.cycle(engine_list):
            engine.run(input_signal)
            last_output_signal = engine.output_signal
            if all_engine_are_done(engine_list):
                final_output_signal_list.append(last_output_signal)
                break
            input_signal = last_output_signal

    print(max(final_output_signal_list))


def all_engine_are_done(engine_list):
    return all((engine.isDone() for engine in engine_list))


if __name__ == '__main__':
    main()