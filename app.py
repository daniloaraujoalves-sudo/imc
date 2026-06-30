#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora de IMC - Versão Console
Funciona em qualquer computador sem precisar instalar nada extra.
"""

# Função que limpa a tela do terminal usando códigos ANSI
def limpar_tela():
    print("\033[2J\033[H", end="")  # Limpa a tela


# Função que aplica cor ao texto usando códigos ANSI (cores: azul, verde, amarelo, laranja, vermelho, cinza, branco)
def colorir(texto, cor):
    cores = {
        "azul": "\033[94m",
        "verde": "\033[92m",
        "amarelo": "\033[93m",
        "laranja": "\033[38;5;208m",
        "vermelho": "\033[91m",
        "cinza": "\033[90m",
        "branco": "\033[97m",
        "reset": "\033[0m"
    }
    return cores.get(cor, "") + texto + cores["reset"]


# Função principal: executa toda a calculadora de IMC (entrada, cálculo, classificação e repetição)
def calcular_imc():
    limpar_tela()
    print(colorir("╔════════════════════════════════════════════╗", "azul"))
    print(colorir("║     🧮  CALCULADORA DE IMC  (Console)     ║", "azul"))
    print(colorir("╚════════════════════════════════════════════╝", "azul"))
    print()

    while True:
        # === Entrada de dados ===
        peso_str = input("⚖️  Digite seu peso em kg (ex: 70.5 ou 70,5): ").strip()
        altura_str = input("📏 Digite sua altura em metros (ex: 1.75): ").strip()

        # Converte vírgula para ponto
        peso_str = peso_str.replace(",", ".")
        altura_str = altura_str.replace(",", ".")

        try:
            peso = float(peso_str)
            altura = float(altura_str)
        except ValueError:
            print(colorir("\n❌ Erro: Digite apenas números! Use ponto ou vírgula.", "vermelho"))
            input("\nPressione ENTER para tentar novamente...")
            limpar_tela()
            continue

        # Validações
        if peso <= 0:
            print(colorir("\n❌ Erro: O peso deve ser maior que zero.", "vermelho"))
            input("\nPressione ENTER para tentar novamente...")
            limpar_tela()
            continue

        if altura < 0 or altura > 3.0:
            print(colorir("\n❌ Erro: Altura deve estar entre 0m e 3.0m.", "vermelho"))
            input("\nPressione ENTER para tentar novamente...")
            limpar_tela()
            continue

        # Cálculo
        imc = peso / (altura ** 2)

        # === Resultado ===
        limpar_tela()
        print(colorir("╔════════════════════════════════════════════╗", "verde"))
        print(colorir("║              SEU RESULTADO                 ║", "verde"))
        print(colorir("╚════════════════════════════════════════════╝", "verde"))
        print()
        print(f"   Seu IMC é: {colorir(f'{imc:.2f}', 'branco')}")
        print()

        # Classificação
        if imc < 16.0:
            classificacao = "Magreza Grave (Grau III)"
            cor = "azul"
            icone = "⬇️"
        elif imc < 17.0:
            classificacao = "Magreza Moderada (Grau II)"
            cor = "azul"
            icone = "⬇️"
        elif imc < 18.5:
            classificacao = "Magreza Leve (Grau I)"
            cor = "azul"
            icone = "⬇️"
        elif imc < 22.0:
            classificacao = "Peso Normal (Faixa de Transição Baixa)"
            cor = "verde"
            icone = "✅"
        elif imc < 25.0:
            classificacao = "Peso Normal / Ideal (Parabéns!)"
            cor = "verde"
            icone = "✅"
        elif imc < 27.5:
            classificacao = "Sobrepeso Inicial (Alerta Leve)"
            cor = "amarelo"
            icone = "⚠️"
        elif imc < 30.0:
            classificacao = "Sobrepeso Avançado (Pré-Obesidade)"
            cor = "amarelo"
            icone = "⚠️"
        elif imc < 35.0:
            classificacao = "Obesidade Grau I (Moderada)"
            cor = "laranja"
            icone = "⚠️"
        elif imc < 40.0:
            classificacao = "Obesidade Grau II (Severa)"
            cor = "vermelho"
            icone = "❌"
        else:
            classificacao = "Obesidade Grau III (Mórbida)"
            cor = "vermelho"
            icone = "❌"

        print(f"   Classificação: {icone}  {colorir(classificacao, cor)}")
        print()
        print(colorir("────────────────────────────────────────────", "cinza"))
        print(colorir("⚠️  Lembre-se: isso é apenas um indicador.", "cinza"))
        print(colorir("   Consulte um profissional de saúde.", "cinza"))
        print(colorir("────────────────────────────────────────────", "cinza"))

        # Perguntar se quer calcular novamente
        print()
        novamente = input("Deseja calcular novamente? (s/n): ").strip().lower()
        if novamente != "s":
            print("\nObrigado por usar a calculadora! 👋")
            break
        limpar_tela()


if __name__ == "__main__":
    calcular_imc()