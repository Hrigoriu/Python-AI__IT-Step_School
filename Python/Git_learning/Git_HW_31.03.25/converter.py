# Конвертер валют
print('Конвертер валют починає роботу!')

RATES = {
    "USD": 41.2,
    "EUR": 44.5,
}
COMMISSION_PERCENT = 1.0 # Комісія 1%
amount_uah = float(input('Введіть суму в гривнях (UAH): '))
commission = amount_uah * (COMMISSION_PERCENT / 100)
amount_after_commission = amount_uah - commission
print(f'Комісія ({COMMISSION_PERCENT}%): {commission:.2f} UAH')
print(f'Сума після комісії: {amount_after_commission:.2f} UAH')

amount_usd = amount_after_commission / RATES["USD"]
print(f'{amount_uah} UAH (з урахуванням комісії) це приблизно {amount_usd:.2f} USD')

amount_eur = amount_after_commission / RATES["EUR"]
print(f'{amount_uah} UAH (з урахуванням комісії) це приблизно {amount_eur:.2f} EUR')