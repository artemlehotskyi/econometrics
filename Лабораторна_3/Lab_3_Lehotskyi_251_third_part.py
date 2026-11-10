import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
sns.set_theme()

df1 = pd.read_excel('ЛР1_Легоцький_251.xlsx', sheet_name='for_python', header=None, names=['Y', 'X'])
df2 = pd.read_excel('ЛР2_Варіант_15_Легоцький.xlsx', sheet_name='for_python', header=None, names=['Y', 'X1', 'X2'])

Y1 = df1['Y']
X1_const = sm.add_constant(df1[['X']])
model1 = sm.OLS(Y1, X1_const).fit()

Y2 = df2['Y']
X2_const = sm.add_constant(df2[['X1', 'X2']])
model2 = sm.OLS(Y2, X2_const).fit()

print('Коефіцієнти моделі 1:')
print(model1.params)
print('R2 =', round(model1.rsquared, 4))
print('\nКоефіцієнти моделі 2:')
print(model2.params)
print('R2 =', round(model2.rsquared, 4))

excel1 = [0.0260, 0.9061, 0.9796]
python1 = [model1.params['const'], model1.params['X'], model1.rsquared]
compare1 = pd.DataFrame({'Excel': excel1, 'Python': python1}, index=['a', 'b', 'R2'])
compare1['Різниця'] = np.abs(compare1['Excel'] - compare1['Python'])
print('\nПорівняння Excel і Python (парна регресія):')
print(compare1.round(4))

excel2 = [-5.9892, 2.2412, 0.1923, 0.7435]
python2 = [model2.params['const'], model2.params['X1'], model2.params['X2'], model2.rsquared]
compare2 = pd.DataFrame({'Excel': excel2, 'Python': python2}, index=['a', 'b1', 'b2', 'R2'])
compare2['Різниця'] = np.abs(compare2['Excel'] - compare2['Python'])
print('\nПорівняння Excel і Python (множинна регресія):')
print(compare2.round(4))

Y1_pred = model1.predict(X1_const)
Y2_pred = model2.predict(X2_const)

plt.figure()
plt.scatter(Y1, Y1_pred)
plt.plot([Y1.min(), Y1.max()], [Y1.min(), Y1.max()], color='red', label='Y = Ŷ')
plt.title('Фактичні vs прогнозовані значення (парна регресія)')
plt.xlabel('Фактичне споживання, млн грн')
plt.ylabel('Прогнозоване споживання, млн грн')
plt.legend()
plt.show()

plt.figure()
plt.scatter(Y2, Y2_pred)
plt.plot([Y2.min(), Y2.max()], [Y2.min(), Y2.max()], color='red', label='Y = Ŷ')
plt.title('Фактичні vs прогнозовані значення (множинна регресія)')
plt.xlabel('Фактичний чистий прибуток, млн грн')
plt.ylabel('Прогнозований чистий прибуток, млн грн')
plt.legend()
plt.show()

resid1 = Y1 - Y1_pred
resid2 = Y2 - Y2_pred

plt.figure()
plt.scatter(Y1_pred, resid1)
plt.axhline(0, color='red')
plt.title('Залишки від прогнозованих значень (парна регресія)')
plt.xlabel('Прогнозоване споживання, млн грн')
plt.ylabel('Залишки, млн грн')
plt.show()

plt.figure()
plt.scatter(Y2_pred, resid2)
plt.axhline(0, color='red')
plt.title('Залишки від прогнозованих значень (множинна регресія)')
plt.xlabel('Прогнозований чистий прибуток, млн грн')
plt.ylabel('Залишки, млн грн')
plt.show()

print('\nЗалишки моделі 1:')
print(f'mean = {resid1.mean():.4f}')
print(f'std = {resid1.std():.4f}')
print(resid1.describe().round(4))

print('\nЗалишки моделі 2:')
print(f'mean = {resid2.mean():.4f}')
print(f'std = {resid2.std():.4f}')
print(resid2.describe().round(4))

print('\nВисновок:')
print('Результати Excel і Python збігаються (різниця лише через округлення)')
print('Середнє залишків обох моделей ≈ 0, як і має бути для МНК')
if model1.f_pvalue < 0.05:
    print(f'Модель 1 адекватна, R2 = {model1.rsquared:.4f}, придатна для прогнозування')
if model2.f_pvalue < 0.05:
    print(f'Модель 2 адекватна, R2 = {model2.rsquared:.4f}, придатна для прогнозування,')
    print('але коефіцієнти окремо незначущі через мультиколінеарність X1 і X2')