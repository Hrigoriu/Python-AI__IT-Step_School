# Завдання №1: Створити застосунок діалогу

import os
from openai import OpenAI

try:
    client = OpenAI(
        api_key=os.environ.get("тут впишемо наш OPENAI_API ключ")
    )
except TypeError:
    print("Помилка: Ключ OPENAI_API_KEY не знайдено.")
    print("Будь ласка, встановіть змінну оточення OPENAI_API_KEY або впишіть ключ безпосередньо в код.")
    exit()

# 1. Почнемо історію з системного повідомлення.
messages = [
    {"role": "system", "content": "Ти — корисний помічник, що веде діалог."}
]

print("--- Застосунок простого діалогу ---")
print("Введіть 'вихід', щоб завершити програму.")

while True:
    # 2. Отримаємо ввід від користувача
    user_input = input("Ви: ")
    if user_input.lower() == 'вихід':
        print("До побачення!")
        break

    # 3. Додамо повідомлення користувача до історії
    messages.append({"role": "user", "content": user_input})

    try:
        # 4. Надсилаємо *всю* історію повідомлень до API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        # 5. Отримаємо відповідь AI
        ai_response = response.choices[0].message.content
        print(f"AI: {ai_response}")

        # 6. Додамо відповідь AI до історії для збереження контексту
        messages.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print(f"Виникла помилка API: {e}")
        # Видаляємо останнє повідомлення користувача, щоб уникнути помилки при наступній спробі
        messages.pop()
