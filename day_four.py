import re

problem_input = [] 
problem_input_str = ''

def has_item(iterable: list, item: str) -> bool:
    try:
        # not using the value from index anywhere because if not found
        # this will throw an exception, making the function return false
        iterable.index(item)
        return True
    except:
        return False 

def get_data_until_reaches_char(string_data: str, start_index: int, char: chr) -> str: 
    result = ''
    current_index = start_index
    while current_index <= len(string_data) - 1 and string_data[current_index] != char:
       result += string_data[current_index]
       current_index += 1

    return result

class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str

    
    def __init__(self, byr: str, iyr: str, eyr: str, hgt: str, hcl: str, ecl: str, pid: str):
        self.byr = byr
        self.iyr = iyr
        self.eyr = eyr
        self.hgt = hgt
        self.hcl = hcl
        self.ecl = ecl
        self.pid = pid

    def is_byr_valid(self):

        if len(self.byr) != 4 or not self.byr.isdigit():
            return False

        int_byr = int(self.byr)

        if int_byr < 1920 or int_byr > 2002:
            return False

        return True

    def is_iyr_valid(self):

        if len(self.iyr) != 4 or not self.iyr.isdigit():
            return False

        int_iyr = int(self.iyr)

        if int_iyr < 2010 or int_iyr > 2020:
            return False

        return True

    def is_eyr_valid(self):
        if len(self.eyr) != 4 or not self.eyr.isdigit():
            return False

        int_eyr = int(self.eyr)

        if int_eyr < 2020 or int_eyr > 2030:
            return False

        return True

    def is_hgt_valid(self):
        int_hgt = ''
        index = 0

        if not self.hgt or self.hgt == '':
            return False

        while index <= len(self.hgt) - 1 and self.hgt[index].isdigit():
            int_hgt += self.hgt[index]
            index += 1

        if not int_hgt.strip():
           return False 

        # I'm so sorry for using dynamic typing here...
        # int_hgt starts off as str and becomes int
        # found it to be convenient
        int_hgt = int(int_hgt)

        unit = self.hgt[index:]

        if unit not in ['cm', 'in']:
            return False

        if unit == 'cm' and (int_hgt < 150 or int_hgt > 193):
            return False
        elif unit == 'in' and (int_hgt < 59 or int_hgt > 76):
            return False

        return True

    def is_hcl_valid(self):
        if not self.hcl.startswith('#'):
            return False

        return re.fullmatch(r"^[0-9a-fA-F]$", self.hcl or '') or not None

    def is_ecl_valid(self):
        return self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    def is_pid_valid(self):
        return len(self.pid) == 9 

    def all_fields_are_valid(self):
        return self.is_byr_valid() and self.is_iyr_valid() and self.is_eyr_valid() and self.is_hgt_valid() and self.is_hcl_valid() and self.is_ecl_valid() and self.is_pid_valid()

valid_passport_count = 0

with open('dayfour_input.txt', 'r') as reader:
# with open('dayfour_input_sample.txt', 'r') as reader:
# with open('dayfour_input_sample_part2.txt', 'r') as reader:
    for line in reader:
        problem_input_str += line

problem_input = problem_input_str.split('\n\n')

for passport_data in problem_input:
    byr = '' 
    iyr = ''
    eyr = '' 
    hgt = ''
    hcl = ''
    ecl = ''
    pid = ''

    if has_item(passport_data, 'byr'):
        byr = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('byr'), ' ').split(':')[1]

    if has_item(passport_data, 'iyr'):
        iyr = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('iyr'), ' ').split(':')[1]

    if has_item(passport_data, 'eyr'):
        eyr = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('eyr'), ' ').split(':')[1]

    if has_item(passport_data, 'hgt'):
        hgt = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('hgt'), ' ').split(':')[1]

    if has_item(passport_data, 'hcl'):
        hcl = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('hcl'), ' ').split(':')[1]

    if has_item(passport_data, 'ecl'):
        ecl = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('ecl'), ' ').split(':')[1]

    if has_item(passport_data, 'pid'):
        pid = get_data_until_reaches_char(passport_data.replace('\n', ' '), passport_data.index('pid'), ' ').split(':')[1]

    passport: Passport = Passport(byr, iyr, eyr, hgt, hcl, ecl, pid)
    valid_passport_count += 1 if passport.all_fields_are_valid() else 0

print(valid_passport_count)
