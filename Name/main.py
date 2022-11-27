import pytrovich
from pytrovich.detector import PetrovichGenderDetector
from pytrovich.enums import NamePart, Gender, Case
from pytrovich.maker import PetrovichDeclinationMaker

import os
import os.path
import time

from progress.bar import IncrementalBar

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')

class Name:
    def main(self):
        self.slowType("""                    ██████╗░░██████╗███╗░░░███╗
                    ██╔══██╗██╔════╝████╗░████║
                    ██████╔╝╚█████╗░██╔████╔██║
                    ██╔══██╗░╚═══██╗██║╚██╔╝██║
                    ██║░░██║██████╔╝██║░╚═╝░██║
                    ╚═╝░░╚═╝╚═════╝░╚═╝░░░░░╚═╝""", .01)
        time.sleep(2)
        self.slowType("                       ®Made by: Myatnikboy", .05)
        time.sleep(2)
        file_path = "n_name.txt"
        if os.path.exists(file_path) == True:
            self.slowType("\nПодготовка перевода имён с Именительного падежа в Дательный падеж", .02)
            time.sleep(2)
            with open("n_name.txt", encoding="utf-8") as f:
                a = f.read()
                a = a.split()
                b = len(a) // 3
                suffix = '%(percent)d%% [%(eta_td)s]'
                bar = IncrementalBar('Прогресс..', max = b, suffix = suffix)
                s = 0
                n = 1
                m = 2
                detector = PetrovichGenderDetector()
                maker = PetrovichDeclinationMaker()
                new = open("d_name.txt","w+", encoding="utf-8")
                for i in range(b):
                    lastname = f'{a[s]}'
                    firstname = f'{a[n]}'
                    middlename = f'{a[m]}'
                    gender = detector.detect(firstname, lastname, middlename)
                    lastname = maker.make(NamePart.LASTNAME, gender, Case.DATIVE, lastname)
                    firstname = maker.make(NamePart.FIRSTNAME, gender, Case.DATIVE, firstname)
                    middlename = maker.make(NamePart.MIDDLENAME, gender, Case.DATIVE, middlename)
                    new.write(lastname + " " + firstname + " " + middlename + "\n")
                    s += 3
                    n += 3
                    m += 3
                    bar.next()
                    time.sleep(.02)
                bar.finish()
                new.close()
                print("\n")
                input("Готово. Нажмите Enter 5 раз для выхода из программы....")
                [input(i) for i in range(4, 0, -1)]
        else:
            print("Отсуствует файл!!")
            input("Готово. Нажмите Enter 5 раз для выхода из программы....")
            [input(i) for i in range(4, 0, -1)]

    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

if __name__ == '__main__':
    RSM = Name()
    RSM.main()