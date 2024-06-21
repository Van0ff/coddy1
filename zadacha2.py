def burn_time(bengal_lights):
    if bengal_lights == 1:
        return 2
    else:
        return 2 + burn_time(bengal_lights // 2) * 2
#вводим изначальное значение бенгальских огней
start_bengal_lights = 5

total_burn_time = burn_time(start_bengal_lights)
print(f"Бенгальские огни будут гореть в течение {total_burn_time} часов.")