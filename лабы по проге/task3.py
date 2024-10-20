# 3 задание
from functools import partial

# Периоды полураспада для специфичных изотопов
elems = {
    "Sr_90": 28.8 * 365 * 24 * 3600,  # Период полураспада в секундах
    "C_14": 5730 * 365 * 24 * 3600,   # Период полураспада в секундах
    "Co_60": 5.27 * 365 * 24 * 3600   # Период полураспада в секундах
}

radioactive_funcs = {"Sr_90": None, "C_14": None, "Co_60": None}

def decay_amount(N0, t, t1_2):
    """Вычисляет, сколько радиоактивного вещества осталось после времени t."""
    N = N0 * (0.5 ** (t / t1_2))
    res = f"Масса радиоактивного вещества, t1_2={t1_2}"
    print(f'{res} с периодом полураспада {t1_2}, N0 = {N0}, t = {t}')
    return N

# Частично применяем функцию decay_amount
radioactive_funcs["Sr_90"] = partial(decay_amount, t1_2=elems['Sr_90'])
radioactive_funcs["C_14"] = partial(decay_amount, t1_2=elems['C_14'])
radioactive_funcs["Co_60"] = partial(decay_amount, t1_2=elems['Co_60'])

def main():
    """Основная программа, вычисляющая остаток веществ для каждого изотопа."""
    N0 = 100
    t = 4006.9 * 365 * 24 * 3600  # Время в секундах

    for isotope, func in radioactive_funcs.items():
        result = func(N0, t)
        print(f'Изотоп: {isotope}, Остаток: {result}')

if __name__ == "__main__":
    main()
