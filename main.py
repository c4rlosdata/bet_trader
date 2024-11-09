from api_handler import iniciar_driver, obter_dados_api
from telegram_bot import enviar_mensagem_telegram
import time
import logging
from datetime import datetime

# Configurações iniciais
logging.basicConfig(filename='fut_trading_bot.log', level=logging.INFO, 
                    format='%(asctime)s %(levelname)s:%(message)s')

jogos_enviados = []

def construir_mensagem(game, strategy):
    home_team = game["homeTeam"]["name"]
    away_team = game["awayTeam"]["name"]
    home_score = game["scores"]["homeTeamScore"]
    away_score = game["scores"]["awayTeamScore"]

    minute = game.get("currentTime", {}).get("minute")
    if minute is None:
        print("Valor de 'minute' é None. Definindo para 0.")
        minute = 0
    
    mensagem = (f"⚽ Jogo: {home_team} vs {away_team}\n"
                f"⏰ Minuto: {minute}\n"
                f"🏆 Placar: {home_team} {home_score} x {away_team} {away_score}\n"
                f"Estrategia: {strategy}")
    return mensagem

def analisar_jogo(game):
    stats = game.get("stats", {})

    minute = game.get("currentTime", {}).get("minute")
    if minute is None:
        print("Valor de 'minute' é None. Definindo para 0.")
        minute = 0

    addedtime = game.get("currentTime", {}).get("addedTime", 0)
    home_score = game.get("scores", {}).get("homeTeamScore", 0)
    away_score = game.get("scores", {}).get("awayTeamScore", 0)

    # Estatísticas novas e existentes
    home_shotsongoal = stats.get("shotsOngoal", {}).get("home", 0)
    away_shotsongoal = stats.get("shotsOngoal", {}).get("away", 0)
    home_shotsoffgoal = stats.get("shotsOffgoal", {}).get("home", 0)
    away_shotsoffgoal = stats.get("shotsOffgoal", {}).get("away", 0)
    home_corners = stats.get("corners", {}).get("home", 0)
    away_corners = stats.get("corners", {}).get("away", 0)
    home_dangerousattacks = stats.get("dangerousAttacks", {}).get("home", 0)
    away_dangerousattacks = stats.get("dangerousAttacks", {}).get("away", 0)
    home_redcards = stats.get("redcards", {}).get("home", 0)
    away_redcards = stats.get("redcards", {}).get("away", 0)
    home_attacks = stats.get("attacks", {}).get("home", 0)
    away_attacks = stats.get("attacks", {}).get("away", 0)
    home_possession = stats.get("possessiontime", {}).get("home", 0)
    away_possession = stats.get("possessiontime", {}).get("away", 0)
    home_saves = stats.get("saves", {}).get("home", 0)
    away_saves = stats.get("saves", {}).get("away", 0)
    home_fouls = stats.get("fouls", {}).get("home", 0)
    away_fouls = stats.get("fouls", {}).get("away", 0)
    home_offsides = stats.get("offsides", {}).get("home", 0)
    away_offsides = stats.get("offsides", {}).get("away", 0)
    home_yellowcards = stats.get("yellowcards", {}).get("home", 0)
    away_yellowcards = stats.get("yellowcards", {}).get("away", 0)
    home_shotsinsidebox = stats.get("shotsInsidebox", {}).get("home", 0)
    away_shotsinsidebox = stats.get("shotsInsidebox", {}).get("away", 0)
    home_shotsoutsidebox = stats.get("shotsOutsidebox", {}).get("home", 0)
    away_shotsoutsidebox = stats.get("shotsOutsidebox", {}).get("away", 0)
    
    # Estratégia BTS
    if minute <= 45 and minute != 0:
        if home_score == 0 and away_score ==0:
            if home_shotsongoal + away_shotsongoal >= 6 and home_shotsongoal >=2 and away_shotsongoal >= 2:
                if home_redcards + away_redcards == 0:
                    if home_corners >= 2 and away_corners >=2:
                        if home_corners + away_corners + home_shotsongoal + away_shotsongoal + home_shotsoffgoal + away_shotsoffgoal >= 15:
                            if home_dangerousattacks >= 10 and away_dangerousattacks >= 10:
                                return "BTS"

    
    return None

def verificar_dados_e_enviar(dados):
    if dados is None:
        return

    for game in dados['data']:
        if game['stats'] is None:
            continue
        fixture_id = game['fixtureId']
        if fixture_id in jogos_enviados:
            continue

        strategy = analisar_jogo(game)
        if strategy:
            mensagem = construir_mensagem(game, strategy)
            enviar_mensagem_telegram(mensagem)
            jogos_enviados.append(fixture_id)

def main():
    driver = iniciar_driver()
    try:
        while True:
            dados = obter_dados_api(driver)
            verificar_dados_e_enviar(dados)
            time.sleep(60)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
