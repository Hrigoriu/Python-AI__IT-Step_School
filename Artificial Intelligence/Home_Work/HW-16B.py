# Завдання №2: Створити АІ діалог

import os
from openai import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

# --- Налаштуємо клієнта OpenAI ---

try:
    client = OpenAI(
        api_key=os.environ.get("тут впишемо наш OPENAI_API ключ")
    )
except TypeError:
    print("Помилка: Ключ OPENAI_API_KEY не знайдено.")
    print("Будь ласка, встановіть змінну оточення OPENAI_API_KEY або впишіть ключ безпосередньо в код.")
    exit()

# --- Клас-обгортка для сумісності ---
# Цей клас імітує поведінку "Runnable" з LangChain
class OpenAIRunnable:
    def __init__(self, client, model="gpt-4o-mini", temperature=0.7):
        self.client = client
        self.model = model
        self.temperature = temperature

    def invoke(self, prompt_text):
        """
        Метод invoke просто викликає API з одним єдиним промптом.
        """
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt_text}],
            temperature=self.temperature
        )
        return resp.choices[0].message.content

# 1. Ініціалізуємо "модель" (нашу обгортку)
llm_runnable = OpenAIRunnable(client)

# 2. Ініціалізуємо пам'ять
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=False)

# 3. Створимо шаблон промпту
# Щоб він брав нове питання та історію з пам'яті
prompt_template = PromptTemplate(
    input_variables=["question", "chat_history"],
    template=(
        "Ти — експерт з AI, що веде дружню розмову.\n"
        "Поточна історія розмови:\n{chat_history}\n\n"
        "Людина: {question}\n"
        "AI:"
    )
)

print("--- АІ діалог (стиль LangChain) ---")
print("Введіть 'вихід', щоб завершити програму.")

while True:
    user_question = input("Ви: ")
    if user_question.lower() == 'вихід':
        print("До побачення!")
        break

    try:
        # 4. Завантажимо історію з пам'яті
        chat_history = memory.load_memory_variables({})["chat_history"]

        # 5. Форматуємо повний промпт, поєднуючи історію та нове питання
        prompt_text = prompt_template.format(question=user_question, chat_history=chat_history)

        # 6. Викличемо модель з повним промптом
        response = llm_runnable.invoke(prompt_text)

        # 7. Збережемо цей обмін (питання та відповідь) у пам'ять
        memory.save_context({"input": user_question}, {"output": response})

        print(f"AI: {response}")

    except Exception as e:
        print(f"Виникла помилка: {e}")
