temperatures = [100, -5, -500, 0, 234, -1051, 34, 36]


def writer(temperatures, path):
    for temperature in temperatures:
        if temperature < -273.15:
            print('oof for ' + str(temperature))
        else:
            f = temperature * 9/5 + 32
            with open(path, 'a') as file:
                file.write(str(f) + '\n')


writer(temperatures, 'files/long_converted.txt')
