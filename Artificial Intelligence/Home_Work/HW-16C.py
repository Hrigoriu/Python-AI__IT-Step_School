# Завдання: Створити агента для спілкування з клієнтом

import os
from openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# --- Налаштуємо клієнта OpenAI ---
try:
    client = OpenAI(
        api_key=os.environ.get("тут впишемо наш OPENAI_API ключ")
    )
    # Перевіримо, чи ключ дійсно завантажено
    if client.api_key is None:
        raise TypeError
except TypeError:
    print("Помилка: Ключ OPENAI_API_KEY не знайдено.")
    print("Будь ласка, встановіть змінну оточення OPENAI_API_KEY або впишіть ключ безпосередньо в код.")
    exit()

# --- Створимо клас-обгортку, яка імітує поведінку "Runnable" з LangChain ---
class OpenAIRunnable:
    def __init__(self, client, model="gpt-4o-mini", temperature=0.7):
        self.client = client
        self.model = model
        self.temperature = temperature

    def invoke(self, prompt_text):
        try:
            resp = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt_text}],
                temperature=self.temperature
            )
            return resp.choices[0].message.content
        except Exception as e:
            print(f"\n[Помилка API: {e}]\n")
            return "Вибачте, сталася помилка. Спробуйте ще раз."

# 1. Ініціалізуємо "модель" (нашу обгортку)
llm_runnable = OpenAIRunnable(client)

# 2. Ініціалізуємо пам'ять
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=False)

# 3. Створимо шаблон промпту
# Створюємо "агента підтримки"
prompt_template = PromptTemplate(
    input_variables=["question", "chat_history"],
    template=(
        "Ти — дружній та корисний агент підтримки клієнтів компанії 'SuperStore'.\n"
        "Твоя мета — ввічливо та чітко відповідати на запитання клієнтів.\n\n"
        "Поточна історія розмови:\n{chat_history}\n\n"
        "Клієнт: {question}\n"
        "Агент:"
    )
)

print("--- Агент підтримки клієнтів 'SuperStore' ---")
print("Введіть 'вихід', щоб завершити програму.")

while True:
    user_question = input("Клієнт: ")
    if user_question.lower() == 'вихід':
        print("Агент: До побачення! Гарного дня.")
        break

    try:
        # 4. Завантажимо історію з пам'яті
        chat_history = memory.load_memory_variables({})["chat_history"]

        # 5. Форматуємо повний промпт
        prompt_text = prompt_template.format(question=user_question, chat_history=chat_history)

        # 6. Викликаємо модель
        response = llm_runnable.invoke(prompt_text)

        # 7. Зберігаємо цей обмін у пам'ять
        memory.save_context({"input": user_question}, {"output": response})

        print(f"Агент: {response}")

    except Exception as e:
        print(f"[Загальна помилка: {e}]")
