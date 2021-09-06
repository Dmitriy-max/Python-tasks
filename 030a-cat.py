#!/usr/bin/python
# Для того чтобы не запускать программу каждый раз через python, пишем верхнюю строку:#!/usr/bin/python,
# и в терминале выполняем команду : chmod +x 030a-cat.py
# Импортируем модуль sys.
import sys
# Для проверки на ошибки и исключения используем конструкцию try-except.
try:
        # Валидация ввода данных пользователем.
        std_argvLen = len(sys.argv)
        if std_argvLen != 2 :
                print("Incorrect input")
                sys.exit(1)
        # Находим последний аргумент списка sys.argv и сохраняем в локальную переменную.
        inputFile = sys.argv[len(sys.argv) - 1]
        # Для отладки программы выводим последний аргумент списка sys.argv
        #print(inputFile)
        # Окрываем файл для чтения в бинарном режиме inputFile используя конструкцию with-as и сохраняем данные в переменную file.
        with open(inputFile,'rb') as file:
                # Создаем бесконечный цикл для потокового считывания данных файла по 50 МВ.
                while True:
                        line = file.read(51200)
                        # Прерываем цикл если строки (данные в файле) заканчиваются.
                        if len(line) == 0:
                                break
                        # Выводим на экран считанные данные. 
                        sys.stdout.buffer.write(line)
# Создаем блоки исключений и ошибок, выводим на экран данные об ошибке, заканчиваем программу с кодом 1-5.
except FileNotFoundError: 
        print("No such file or directory", file=sys.stderr)
        sys.exit(2)
except IsADirectoryError: 
        print("Is a directory", file=sys.stderr)
        sys.exit(3)
except IOError: 
        print("No file", file=sys.stderr)
        sys.exit(4)
except MemoryError: 
        print("Large file size", file=sys.stderr)
        sys.exit(5)
print()
print()
print()
print('Thanks for using our utility tools.')
print('(c) 2021 Dmitry Detukov')

#Ожидаемый вывод программы после запуска из консоли:
#$ ./030a-cat /proc/cpuinfo 
#processor	: 0
#vendor_id	: GenuineIntel
#cpu family	: 6
#model		: 63
#model name	: DO-Regular
#stepping	: 2
#microcode	: 0x1
#cache size	: 4096 KB
#fpu		: yes
#cpuid level	: 13
#flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ss syscall nx rdtscp lm constant_tsc arch_perfmon rep_good nopl cpuid tsc_known_freq pni pclmulqdq vmx ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm cpuid_fault invpcid_single pti ssbd ibrs ibpb tpr_shadow vnmi flexpriority ept vpid ept_ad fsgsbase tsc_adjust bmi1 avx2 smep bmi2 erms invpcid xsaveopt md_clear
#vmx flags	: vnmi preemption_timer invvpid ept_x_only ept_ad ept_1gb flexpriority tsc_offset vtpr mtf vapic ept vpid unrestricted_guest vapic_reg vid pml
#bugs		: cpu_meltdown spectre_v1 spectre_v2 spec_store_bypass l1tf mds swapgs itlb_multihit
#address sizes	: 40 bits physical, 48 bits virtual
#power management:



#Thanks for using our utility tools.
#(c) 2020 Sergey Ivanov








