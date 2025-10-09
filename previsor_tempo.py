import random
import time

def get_weather_condition():
    """Retorna uma condição climática aleatória"""
    conditions = ["☀️ Ensolarado", "🌧️ Chuvoso", "⛅ Parcialmente nublado", "🌩️ Tempestade", "❄️ Nevando", "🌫️ Neblina"]
    return random.choice(conditions)

def get_temperature():
    """Gera uma temperatura aleatória entre -5°C e 40°C"""
    return random.randint(-5, 40)

def generate_weather_report(city):
    """Gera o relatório completo do clima de uma cidade"""
    temperature = get_temperature()
    condition = get_weather_condition()

    print(f"\n📍 Cidade: {city}")
    print(f"🌡️ Temperatura: {temperature}°C")
    print(f"🌤️ Condição: {condition}")
    if temperature > 30:
        print("💡 Dica: Mantenha-se hidratado!")
    elif temperature < 10:
        print("🧣 Dica: Vista-se bem, está frio!")
    else:
        print("😎 Clima agradável!")

def main():
    print("=== SIMULADOR DE PREVISÃO DO TEMPO ===")
    cities = ["São Paulo", "Rio de Janeiro", "Curitiba", "Recife", "Brasília", "Porto Alegre"]

    while True:
        print("\nCidades disponíveis:")
        for i, city in enumerate(cities, 1):
            print(f"{i} - {city}")
        print("0 - Sair")

        try:
            option = int(input("\nEscolha uma cidade pelo número: "))
            if option == 0:
                print("Encerrando o programa. ☁️ Até logo!")
                break
            elif 1 <= option <= len(cities):
                print("Gerando previsão...")
                time.sleep(1.5)
                generate_weather_report(cities[option - 1])
            else:
                print("❌ Opção inválida.")
        except ValueError:
            print("⚠️ Digite um número válido.")

if __name__ == "__main__":
    main()
