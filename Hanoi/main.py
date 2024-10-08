def hanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        print(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    hanoi(n-1, from_rod, aux_rod, to_rod)
    print(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    hanoi(n-1, aux_rod, to_rod, from_rod)

# 主程式
n = int(input('輸入幾個盤子: '))
hanoi(n, 'A', 'C', 'B')
