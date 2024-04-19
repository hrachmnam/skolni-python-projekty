def draw_graph(temps):
    days = ["mon", "tue", "wen", "thu", "fri", "sat", "sun"]
    min_temp = min(temps)
    max_temp = max(temps)
    avg_temp = sum(temps) / len(temps)
    
    print("Temperature:")
    for i in range(len(days)):
        print(f"Temperature in {days[i]}: {temps[i]}")
    
    print("\nGraphical representation:")
    for i in range(len(days)):
        print(f"{days[i]}:", end=" ")
        if temps[i] > 0:
            print(" " * 39 + "|" + "+" * temps[i])
        elif temps[i] < 0:
            print(" " * (39 + temps[i]) + "*" * abs(temps[i]) + "|")
        else:
            print(" " * 40 + "|")
    
    print(f"\nMinimum: {min_temp} ({days[temps.index(min_temp)]})")
    print(f"Maximum: {max_temp} ({days[temps.index(max_temp)]})")
    print(f"Average: {avg_temp:.2f}")

def main():
    temperatures = []
    days = ["mon", "tue", "wen", "thu", "fri", "sat", "sun"]
    
    for day in days:
        temp = int(input(f"Temperature in {day}: "))
        temperatures.append(temp)
    
    draw_graph(temperatures)

if __name__ == "__main__":
    main()
