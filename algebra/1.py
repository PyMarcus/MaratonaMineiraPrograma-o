table = {
    '0000': '0', '0001': '1', '0010': '2', '0011': '3',
    '0100': '4', '0101': '5', '0110': '6', '0111': '7',
    '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
    '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
}

def convertBase(num, base) -> None:
    """
    :param num:
    :param base: hex or bin
    :return:
    """
    if base == 'hex':
        response = convertToHex(num)
        print(response)
    elif base == 'bin':
        response = convertToBin(num)
        print(response)

def convertToBin(num) -> str:
    global table
    """
    :param num: 
    :return: 
    """
    string = ""
    for index, letters in enumerate(num):
        for k, v in table.items():
            if v == letters:
                string += k
    return string

def convertToHex(binary) -> str:
    global table
    string = ""
    for index, algarism in enumerate(binary):
        string += algarism
        if (index + 1) % 4 == 0 and index > 0:
            string += " "
    cc = string.strip().split(" ")
    for index, algarism in enumerate(cc):
        if table.get(algarism) is not None:
            cc[index] = table.get(algarism)
    return ''.join(cc)

if __name__ == '__main__':
    convertBase('FD', 'bin')
    convertBase('11111101', 'hex')