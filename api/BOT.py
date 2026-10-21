import os
import subprocess
import json
import asyncio
import psutil
import GPUtil
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from PIL import ImageGrab
from aiogram.types import FSInputFile
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


# Настройки бота
# BOT_TOKEN = 't.me/@Cup_test_coffe_django_api_bot'
BOT_TOKEN = str(os.getenv("TOKEN_TG"))
ALLOWED_USER_ID = str(os.getenv("TG_ID")) # Замените на ваш Telegram ID
CONFIG_FILE = 'apps.json'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Проверка прав доступа
def check_access(user_id: int) -> bool:
    return user_id == ALLOWED_USER_ID

# Чтение конфигурации кнопок
def load_apps() -> dict:
    if not os.path.exists(CONFIG_FILE):
        return {} # Если файла нет, возвращаем пустой словарь
    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

# Генерация клавиатуры
def get_keyboard():
    apps = load_apps()
    builder = ReplyKeyboardBuilder()
    
    for app_name in apps.keys():
        builder.button(text=app_name)
        
    # Системные кнопки
    builder.button(text="📸 Скриншот")
    builder.button(text="📊 Статус ПК")
    builder.button(text="🔒 Заблокировать ПК")
    builder.button(text="🔴 Выключить ПК")
    builder.button(text="🔄 Обновить меню")
    
    # Если кнопок стало много, можно выводить по 2 или 3 в ряд
    builder.adjust(2) 
    return builder.as_markup(resize_keyboard=True)

# функцию уведомления о запуске скрипта
async def on_startup(bot: Bot):
    # Получаем текущее время компьютера и форматируем его (ДД.ММ.ГГГГ ЧЧ:ММ:СС)
    current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    
    try:
        # Отправляем сообщение напрямую по вашему ID
        await bot.send_message(
            chat_id=ALLOWED_USER_ID,
            text=f"✅ Компьютер включен. Бот управления запущен!\n🕒 Время запуска: {current_time}"
        )
    except Exception as e:
        print(f"Не удалось отправить уведомление при запуске: {e}")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    await message.answer(
        "Панель управления ПК готова.",
        reply_markup=get_keyboard()
    )

@dp.message(F.text == "🔄 Обновить меню")
async def reload_menu(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    # Отправляем новую клавиатуру
    await message.answer("Меню обновлено из файла apps.json!", reply_markup=get_keyboard())

@dp.message(F.text == "🔴 Выключить ПК")
async def cmd_shutdown(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    await message.answer("Инициирую выключение ПК (10 сек)...")
    os.system('shutdown /s /t 10')

@dp.message(F.text == "📸 Скриншот")
async def cmd_screenshot(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    # Отправляем сообщение, что процесс пошел (создание и отправка картинки занимает секунду-две)
    status_msg = await message.answer("Делаю снимок экрана...")
    
    try:
        # Делаем скриншот всего экрана
        screenshot = ImageGrab.grab()

        # Сохраняем текущее время
        current_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        
        # Сохраняем его во временный файл
        file_path = "screen.png"
        screenshot.save(file_path)
        
        # Подготавливаем файл для отправки в Telegram
        photo = FSInputFile(file_path)
        
        # Отправляем фото и удаляем статусное сообщение
        await message.answer_photo(photo, caption=f"📸 Ваш экран {current_time}")
        await status_msg.delete()
        
        # Удаляем временный файл с компьютера, чтобы не засорять папку
        os.remove(file_path)
        
    except Exception as e:
        await message.answer(f"❌ Ошибка при создании скриншота: {e}")

@dp.message(F.text == "🔒 Заблокировать ПК")
async def cmd_lock_pc(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    try:
        # Команда Windows для мгновенной блокировки учетной записи
        os.system("rundll32.exe user32.dll,LockWorkStation")
        await message.answer("🔒 Экран компьютера успешно заблокирован.")
    except Exception as e:
        await message.answer(f"❌ Ошибка при блокировке ПК:\n{e}")

@dp.message(F.text == "📊 Статус ПК")
async def cmd_pc_status(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return

    status_msg = await message.answer("⏳ Собираю данные о системе (занимает около 1 секунды)...")

    try:
        # 1. СЕТЬ: Снимаем начальные показатели
        net_start = psutil.net_io_counters()
        
        # 2. ПРОЦЕССОР: Замеряем загрузку (interval=1 дает паузу ровно в 1 секунду)
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # 3. СЕТЬ: Снимаем показатели после секундной паузы и считаем разницу
        net_end = psutil.net_io_counters()
        
        # Переводим байты в Мегабиты в секунду (Мбит/с)
        download_speed = (net_end.bytes_recv - net_start.bytes_recv) * 8 / (1024 * 1024)
        upload_speed = (net_end.bytes_sent - net_start.bytes_sent) * 8 / (1024 * 1024)
        
        # 4. ОПЕРАТИВНАЯ ПАМЯТЬ
        ram = psutil.virtual_memory()
        ram_total = round(ram.total / (1024 ** 3), 2)
        ram_used = round(ram.used / (1024 ** 3), 2)

        # 6. ВИДЕОКАРТА (NVIDIA)
        gpu_info = "Не обнаружена (или не NVIDIA)"
        try:
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]  # Берем первую видеокарту в системе
                # Формируем красивый вывод для GPU
                gpu_info = (f"{gpu.name}\n"
                            f"      ├ Загрузка: {gpu.load * 100:.1f}%\n"
                            f"      ├ Температура: {gpu.temperature}°C\n"
                            f"      └ VRAM: {gpu.memoryUsed:.0f} / {gpu.memoryTotal:.0f} МБ")
        except Exception:
            pass # Если библиотека выдаст ошибку, мы просто оставим надпись "Не обнаружена"

        # Формируем итоговое сообщение
        status_text = (
            "📊 <b>Статус системы:</b>\n\n"
            f"🧠 <b>Процессор (CPU):</b> {cpu_usage}%\n"
            f"🎮 <b>Видеокарта (GPU):</b> {gpu_info}\n"
            f"💾 <b>Память (RAM):</b> {ram_used} / {ram_total} ГБ ({ram.percent}%)\n"
            f"🌐 <b>Сеть (Ethernet):</b>\n"
            f"      ├ Загрузка: {download_speed:.2f} Мбит/с\n"
            f"      └ Отдача: {upload_speed:.2f} Мбит/с"
        )

        await status_msg.edit_text(status_text, parse_mode="HTML")

    except Exception as e:
        await status_msg.edit_text(f"❌ Ошибка при получении статуса:\n{e}")

@dp.message(F.text.startswith("http://") | F.text.startswith("https://"))
async def handle_links(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
    
    url = message.text.strip() # type: ignore
    
    # Укажите точный путь к вашему браузеру (обычно это Chrome)
    browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
    try:
        # Popen принимает список аргументов: [программа, аргумент1, аргумент2]
        subprocess.Popen([browser_path, "--profile-directory=Default", url])
        await message.answer(f"🌐 Ссылка открыта на ПК:\n{url}")
    except FileNotFoundError:
        await message.answer(f"❌ Браузер не найден по пути: {browser_path}\nПроверьте путь в коде.")
    except Exception as e:
        await message.answer(f"❌ Ошибка при открытии ссылки:\n{e}")

# Обработчик всех остальных текстовых сообщений
@dp.message(F.text)
async def handle_app_buttons(message: types.Message):
    if not check_access(message.from_user.id): # type: ignore
        return
        
    apps = load_apps()
    app_name = message.text
    
    # Если текст сообщения совпадает с названием кнопки из JSON
    if app_name in apps:
        app_path = apps[app_name]
        try:
            subprocess.Popen(app_path)
            await message.answer(f"✅ Успешно запущено: {app_name}")
        except Exception as e:
            await message.answer(f"❌ Ошибка при запуске {app_name}:\n{e}")
    else:
        await message.answer("Неизвестная команда. Пожалуйста, используйте кнопки меню.")

async def main():
    # функция которая сработает при старте (уведомление о том что включен пк)
    dp.startup.register(on_startup)

    # Запуск поллинга
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())