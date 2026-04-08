# soma_numeros_impares
Programa simples em Python que solicita ao usuário 15 números inteiros e calcula a soma apenas dos números ímpares inseridos.

📋 Sobre o Projeto
Este projeto é um exercício de lógica de programação em Python. O programa solicita ao usuário 15 números inteiros, identifica quais são ímpares e, ao final, exibe a soma acumulada desses valores.
É um ótimo exemplo para quem está aprendendo:

Estruturas de repetição (while)
Operadores aritméticos e lógicos
Entrada e saída de dados
Acumuladores e contadores


⚙️ Funcionalidades

✅ Solicita 15 números ao usuário, um por vez
✅ Verifica automaticamente se cada número é ímpar
✅ Ignora os números pares sem interromper o fluxo
✅ Exibe a soma total dos ímpares ao final

🧠 Como Funciona
pythoncont = 1
total = 0

while cont <= 15:
    n = int(input(f"Digite o {cont}° número: "))
    if n % 2 != 0:
        total += n         # acumula apenas os ímpares
    cont += 1              # avança para o próximo número


📚 Conceitos Abordados
Conceito Aplicação no código while Laço de repetição controlado por contador input() Entrada de dados pelo termina lint() Conversão de string para inteiro Operador % Verificação de paridade (par/ímpar) Acumulador Variável total que soma os ímpares F-stringFormatação da saída com f"..."

📁 Estrutura do Projeto
soma-impares/
└── main.py   # Arquivo principal com a lógica do programa

📄 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

