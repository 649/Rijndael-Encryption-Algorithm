#!/usr/bin/env python3

def circularbyteleftshift(w):
    w = [w[1], w[2], w[3], w[0]]
    return w

def hextranslate(w):
    if (w == 'A'):
        return 10
    elif (w == 'B'):
        return 11
    elif (w == 'C'):
        return 12
    elif (w =='D'):
        return 13
    elif (w == 'E'):
        return 14
    elif (w == 'F'):
        return 15
    else:
        return int(w)

def main():
    #ptext = input('Enter plaintext message (128 bits | 16 length): ').encode('utf-8')
    #ktext = input('Enter encryption key (128 bits | 16 length): ').encode('utf-8')
    ptext = "Two One Nine Two".encode('utf-8')
    ktext = "Thats my Kung Fu".encode('utf-8')

    if(len(ptext) == 16 and len(ktext) == 16):
        phext = ptext.hex().upper()
        khext = ktext.hex().upper()
        print(khext)

        sbox = [[ '63', '7C', '77', '7B', 'F2', '6B', '6F', 'C5', '30', '01', '67', '2B', 'FE', 'D7', 'AB', '76'], ['CA', '82', 'C9', '7D', 'FA', '59', '47', 'F0', 'AD', 'D4', 'A2', 'AF', '9C', 'A4', '72', 'C0'], ['B7', 'FD', '93', '26', '36', '3F', 'F7', 'CC', '34', 'A5', 'E5', 'F1', '71', 'D8', '31', '15'], ['04', 'C7', '23', 'C3', '18', '96', '05', '9A', '07', '12', '80', 'E2', 'EB', '27', 'B2', '75'], ['09', '83', '2C', '1A', '1B', '6E', '5A', 'A0', '52', '3B', 'D6', 'B3', '29', 'E3', '2F', '84'], ['53', 'D1', '00', 'ED', '20', 'FC', 'B1', '5B', '6A', 'CB', 'BE', '39', '4A', '4C', '58', 'CF'], ['D0', 'EF', 'AA', 'FB', '43', '4D', '33', '85', '45', 'F9', '02', '7F', '50', '3C', '9F', 'A8'], ['51', 'A3', '40', '8F', '92', '9D', '38', 'F5', 'BC', 'B6', 'DA', '21', '10', 'FF', 'F3', 'D2'], ['CD', '0C', '13', 'EC', '5F', '97', '44', '17', 'C4', 'A7', '7E', '3D', '64', '5D', '19', '73'], ['60', '81', '4F', 'DC', '22', '2A', '90', '88', '46', 'EE', 'B8', '14', 'DE', '5E', '0B', 'DB'], ['E0', '32', '3A', '0A', '49', '06', '24', '5C', 'C2', 'D3', 'AC', '62', '91', '95', 'E4', '79'], ['E7', 'C8', '37', '6D', '8D', 'D5', '4E', 'A9', '6C', '56', 'F4', 'EA', '65', '7A', 'AE', '08'], ['BA', '78', '25', '2E', '1C', 'A6', 'B4', 'C6', 'E8', 'DD', '74', '1F', '4B', 'BD', '8B', '8A'], ['70', '3E', 'B5', '66', '48', '03', 'F6', '0E', '61', '35', '57', 'B9', '86', 'C1', '1D', '9E'], ['E1', 'F8', '98', '11', '69', 'D9', '8E', '94', '9B', '1E', '87', 'E9', 'CE', '55', '28', 'DF'], ['8C', 'A1', '89', '0D', 'BF', 'E6', '42', '68', '41', '99', '2D', '0F', 'B0', '54', 'BB', '16']]


        w = []
        a = [khext[0]+khext[1], khext[2]+khext[3], khext[4]+khext[5], khext[6]+khext[7]]
        b = [khext[8]+khext[9], khext[10]+khext[11], khext[12]+khext[13], khext[14]+khext[15]]
        c = [khext[16]+khext[17], khext[18]+khext[19], khext[20]+khext[21], khext[22]+khext[23]]
        d = [khext[24]+khext[25], khext[26]+khext[27], khext[28]+khext[29], khext[30]+khext[31]]
        w.append(a)
        w.append(b)
        w.append(c)
        w.append(d)
        print(w[3])
        w[3] = circularbyteleftshift(w[3])
        print(w[3])
        w[3] = [sbox[hextranslate(w[3][0][0])][hextranslate(w[3][0][1])], sbox[hextranslate(w[3][1][0])][hextranslate(w[3][1][1])], sbox[hextranslate(w[3][2][0])][hextranslate(w[3][2][1])], sbox[hextranslate(w[3][3][0])][hextranslate(w[3][3][1])]]
        print(w[3])

    else:
        print('Error: Plaintext message is not 128 bits | 16 length.')

if __name__ == "__main__":
    main()