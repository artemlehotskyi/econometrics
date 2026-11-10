import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
sns.set_theme()


df = pd.read_excel('ЛР2_Варіант_15_Легоцький.xlsx', sheet_name='for_python', header=None, names=['Y', 'X1', 'X2'])

Y = df['Y']
X = df[['X1', 'X2']]

print(df.head())
df.info()
print(df.describe())
print(df.isnull().sum())

X_const = sm.add_constant(X)
model2 = sm.OLS(Y, X_const).fit()

print(model2.summary())

coef_table = pd.DataFrame({
    'coef': model2.params.round(3),
    'bse': model2.bse.round(3),
    'tvalues': model2.tvalues.round(3),
    'pvalues': model2.pvalues.round(3)
})

print('\n', coef_table)

fit_stats = pd.Series([model2.rsquared, model2.rsquared_adj, model2.fvalue, model2.f_pvalue],
                      index=['R2', 'R2_adj', 'F', 'p(F)'])

print('\n', fit_stats)

alpha = 0.05
p_factors = model2.pvalues.drop('const')
significant = p_factors[p_factors < alpha]

if significant.empty:
    print('\nЗначущих факторів немає')
else:
    print('\nЗначущі фактори:')
    print(significant)

Y_pred = model2.predict(X_const)
print(pd.DataFrame({'Y': Y, 'Y_pred': Y_pred.round(3)}))

n = range(1, len(Y) + 1)
plt.scatter(n, Y, label='Фактичні')
plt.plot(n, Y_pred, color='red', label='Прогнозовані')
plt.title('Фактичні та прогнозовані значення Y')
plt.xlabel('Номер спостереження')
plt.ylabel('Чистий прибуток, млн грн')
plt.legend()
plt.show()

b = model2.params
print(f'\nY = {b["const"]:.4f} + {b["X1"]:.4f}*X1 + {b["X2"]:.4f}*X2')
print(f'R2 = {model2.rsquared:.4f}')

if model2.f_pvalue < alpha:
    print('Модель адекватна за F-критерієм, її можна використовувати для прогнозування')
else:
    print('Модель неадекватна')

if significant.empty:
    print('Але жоден фактор окремо не значущий через мультиколінеарність X1 і X2')