import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
sns.set_theme()

df = pd.read_excel("ЛР1_Легоцький_251.xlsx", sheet_name='for_python', header=None, names=['Y', 'X'])


def beauty(f, word: str):
    def wrapper(*args, **kwargs):
        print(f'\n------{word}--------')
        result = f(*args, **kwargs)
        print(f'---end--{word}--end---')
        return result
    return wrapper


beauty(print, 'head')(df.head())
beauty(df.info, 'info')()
beauty(print, 'describe')(df.describe())
beauty(print, 'isnull')(df.isnull().sum())

Y = df['Y']
X = df['X']

plt.scatter(X, Y, color='red')
plt.title('Кореляційне поле')
plt.xlabel('Середній дохід населення, млн грн')
plt.ylabel('Середнє споживання населення, млн грн')

plt.show()


X_const = sm.add_constant(X)
model1 = sm.OLS(Y, X_const).fit()
print(model1.summary())

a = model1.params['const']
b = model1.params['X']
R2 = model1.rsquared
p_value = model1.pvalues['X']

print('\n')
print(f'Ŷ = {a:.4f} + {b:.4f}·X')
print(f'a = {a:.4f}, b = {b:.4f}')
print(f'R² = {R2:.4f}')
print(f'p-значення для b = {p_value:.2e}')

Y_pred = model1.predict(X_const)

plt.scatter(X, Y, label='Фактичні значення', color='red')
plt.plot(X, Y_pred, label='Лінія регресії')
plt.title('Лінія парної регресії')
plt.xlabel('Середній дохід населення, млн грн')
plt.ylabel('Середнє споживання населення, млн грн')
plt.text(8, 23, f'Ŷ = {a:.4f} + {b:.4f}·X\nR² = {R2:.4f}')
plt.legend()
plt.show()

def conclusions(model, alpha=0.05, factor='X') -> None:
    a = model.params['const']
    x = model.model.data.orig_exog[factor]
    b = model.params[factor]

    if b > 0:
        print(f"1. Зв'язок прямий: при зростанні доходу на 1 млн грн "
              f"споживання зростає в середньому на {b:.4f} млн грн.")
    else:
        print(f"1. Зв'язок обернений: при зростанні доходу на 1 млн грн "
              f"споживання зменшується в середньому на {abs(b):.4f} млн грн.")
    if 0 < b < 1:
        print(f"   Коефіцієнт b = {b:.4f} — гранична схильність до споживання: "
              f"з кожної додаткової гривні доходу {b * 100:.2f} % спрямовується "
              f"на споживання. Значення в межах (0; 1) узгоджується з економічною теорією.")
    else:
        print(f"   Значення b = {b:.4f} виходить за межі (0; 1), що не узгоджується "
              f"з економічною теорією споживання; модель потребує перегляду.")

    p_b = model.pvalues[factor]
    if p_b < alpha:
        print(f"2. p-значення коефіцієнта b = {p_b:.2e} < {alpha}, тому гіпотеза H0: β = 0 відхиляється."
              f" Дохід статистично значуще впливає на споживання.")
    else:
        print(f"2. p-значення коефіцієнта b = {p_b:.2e} ≥ {alpha}, гіпотеза H0: β = 0 не відхиляється."
              f" Вплив доходу на споживання статистично незначущий.")

    p_a = model.pvalues['const']
    reasons = []
    if p_a >= alpha:
        reasons.append(f"він статистично незначущий (p = {p_a:.4f} ≥ {alpha})")
    if x.min() > 0:
        reasons.append(f"значення X = 0 лежить поза межами вибірки "
                       f"(мінімальний дохід {x.min():.1f} млн грн)")
    if reasons:
        print(f"3. Вільний член a = {a:.4f} змістовно не інтерпретується: "
              + '; '.join(reasons) + '.')
    else:
        print(f"3. Вільний член a = {a:.4f} статистично значущий і відповідає "
              f"рівню споживання при нульовому доході.")

    R2 = model.rsquared
    r = R2 ** 0.5
    print(f"4. R² = {R2:.4f}: варіація доходу пояснює {R2 * 100:.2f} % варіації "
          f"споживання, решта {(1 - R2) * 100:.2f} % зумовлена іншими факторами.")
    if r >= 0.9:
        strength = 'дуже високий'
    elif r >= 0.7:
        strength = 'високий'
    elif r >= 0.5:
        strength = 'помітний'
    elif r >= 0.3:
        strength = 'помірний'
    elif r >= 0.1:
        strength = 'слабкий'
    else:
        strength = 'практично відсутній'
    print(f"   Коефіцієнт кореляції r = {r:.4f}, за шкалою Чеддока зв'язок {strength}.")

    p_F = model.f_pvalue  # скаляр
    if p_F < alpha:
        print(f"5. p-значення F-критерію = {p_F:.2e} < {alpha}: рівняння регресії "
              f"статистично значуще, модель адекватна.")
    else:
        print(f"5. p-значення F-критерію = {p_F:.2e} ≥ {alpha}: рівняння регресії "
              f"статистично незначуще, модель неадекватна.")

    print(f"6. Модель Ŷ = {a:.4f} + {b:.4f}·X може використовуватися для прогнозування "
          f"споживання в межах діапазону доходу {x.min():.1f}–{x.max():.1f} млн грн. "
          f"Через малий обсяг вибірки (n = {int(model.nobs)}) прогнози слід "
          f"інтерпретувати з обережністю.")

conclusions(model1)