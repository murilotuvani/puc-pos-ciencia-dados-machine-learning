# Resumo Detalhado: Linguagem de Programação Python Aplicada à Análise de Dados (até pág. 33)

## Material Introdutório

* **Autor e Contexto:** O material é de autoria de Ariel da Silva Dias, Mestre em Ciência da Computação e Matemática Computacional pela USP e graduado em Ciência da Computação pela PUC Minas. Ele atua como professor universitário em diversas áreas relacionadas à computação e dados.
* **Justificativa da Disciplina:** A disciplina se justifica pelo crescimento exponencial do volume de dados gerados mundialmente e pela necessidade das organizações analisarem esses dados para tomadas de decisão estratégicas. O objetivo é apresentar técnicas para extrair informações valiosas a partir dos dados.
* **Engajamento e Relevância do Python:** Python é destacado por sua simplicidade e aplicabilidade em diversas áreas, incluindo desenvolvimento web, modelagem 3D e, crucialmente para esta disciplina, análise de dados através de suas poderosas bibliotecas. Questionamentos são levantados sobre a capacidade de análise de dados do Python puro versus o uso de bibliotecas e as vantagens das estruturas de dados de bibliotecas como NumPy sobre as nativas do Python.
* **Apresentação da Disciplina:** A disciplina é dividida em três unidades. A primeira foca nos fundamentos da linguagem Python, suas características e comandos principais. A segunda unidade aborda o primeiro contato com grandes volumes de dados, manipulação de fontes externas e o uso do Pandas. A terceira unidade explora a análise exploratória de dados, incluindo descritores estatísticos com Python e suas bibliotecas. O material enfatiza a importância da prática, incentivando a reprodução e criação de códigos.
* **Objetivos da Disciplina:** Ao final, espera-se que o estudante possa:
    * Identificar características do Python para Análise de Dados.
    * Investigar e usar bibliotecas de análise de dados.
    * Analisar e tratar dados em datasets.
    * Identificar e corrigir dados faltantes.
    * Explicar e utilizar descritores estatísticos.

## Unidade 1: Linguagem Python

* **Objetivos da Unidade 1:**
    * Examinar a sintaxe do Python.
    * Identificar componentes do ambiente de desenvolvimento.
    * Identificar e usar bibliotecas de análise de dados.
    * Aplicar comandos e particularidades da linguagem.
* **Apresentação da Unidade 1:** Reforça a análise de dados como um conjunto de técnicas para extrair informações de dados brutos. Python é destacado novamente por sua versatilidade, sintaxe simples, código enxuto e bibliotecas importantes (Pandas, NumPy, SciPy). A unidade abordará o ambiente de desenvolvimento, conceitos fundamentais, sintaxe, e as bibliotecas de análise de dados, sendo acessível tanto para quem já programa quanto para iniciantes. A importância da prática é novamente enfatizada.

### 1.1 Linguagem Python

* **Características:** Python, lançado em 1991 por Guido van Rossum, é uma linguagem de alto nível, tipo script, projetada para fácil leitura e escrita.
* **Estrutura:** Esta seção introduz a estrutura da linguagem, sintaxe, e as essenciais estruturas condicionais (para dividir o fluxo do código) e de repetição (cruciais para percorrer grandes datasets).
* **Bibliotecas vs. Python Puro:** Discute-se que, embora possível, desenvolver análise de dados em Python puro é complexo. As bibliotecas específicas simplificam enormemente o trabalho, reduzem o tempo de desenvolvimento e oferecem ampla documentação.

### 1.1.1 Ambiente de Desenvolvimento

* **Opções:** Para projetos pequenos, o editor shell pode ser usado, mas para projetos maiores, um editor dedicado ou IDE é recomendado.
* **Principais Ambientes:**
    * **Pydev (Eclipse):** Um plugin para Eclipse que o transforma em um IDE Python, suportando Jython e IronPython. Oferece recursos como preenchimento de código, análise, depurador, console interativo, etc..
    * **Visual Studio Code (VS Code):** Projeto da Microsoft, popular no GitHub. Permite adicionar suporte a linguagens como Python através de plugins.
    * **IDLE:** Ambiente integrado de desenvolvimento e aprendizagem, lançado por Guido van Rossum. É simples, adequado para iniciantes, com editor multi-janela, destaque de sintaxe e depurador básico.

#### 1.1.1.1 Anaconda

* **Definição:** Uma distribuição gratuita e de código aberto para Python e R, focada em facilitar a instalação de pacotes para ciência de dados e aprendizado de máquina.
* **Componentes Incluídos:**
    * **Conda:** Sistema de gerenciamento de pacotes e ambientes.
    * **Bibliotecas de Machine Learning:** TensorFlow, scikit-learn, Theano.
    * **Bibliotecas de Ciência de Dados:** Pandas, NumPy, Dask.
    * **Bibliotecas de Visualização:** Bokeh, Matplotlib, etc..
    * **Jupyter Notebook:** Ambiente interativo para código, visualizações e texto.
* **Instalação e Uso:** A instalação não é detalhada no material, mas o link para a documentação oficial é fornecido. A Figura 1 mostra o Anaconda Navigator. O material guiará o uso do Jupyter Notebook, instruindo o usuário a abri-lo via Navigator, clicar em "New" e selecionar "Python 3" para criar um novo arquivo (notebook). A Figura 2 ilustra esse processo. É sugerido criar uma pasta dedicada para organizar os arquivos.

### 1.1.2 Variáveis e Comandos Básicos

* **Facilidade:** Python é mais fácil para quem já conhece C, Java ou C#.
* **Tipagem Implícita:** Diferentemente de outras linguagens, não é preciso declarar o tipo da variável explicitamente.
* **Exemplo Básico:**
    ```python
    nome = input("Qual o seu nome?")
    idade = input("Qual a sua idade? ")
    print("O seu nome é " + nome + " e você tem " + idade + " anos de idade.")
    ```
    * Este código demonstra a leitura de dados com `input()` (que retorna string) e a impressão com `print()`. A concatenação de strings é feita com o operador `+`.
* **Tipos de Dados Padrão:** Python possui 5 tipos padrão: números, string, lista, tupla e dicionário. Números e strings são abordados inicialmente.

#### 1.1.2.1 Números

* **Tipos Numéricos:**
    * `int` (inteiros): e.g., 36, -740.
    * `float` (ponto flutuante): e.g., 0.0, 88.5, 32e100.
    * `complex` (complexos): e.g., 3.14j, 3e+26j.
* **Exemplo - Área da Circunferência (Figura 4):**
    ```python
    PI = 3.1415 #isso é um valor constante, mas não necessariamente foi declarado como constante!
    raio = float(input("Informe o raio da circunferencia:"))
    raio = raio ** 2
    area = 3.1415 * raio
    print(area)
    ```
    * **Constantes:** Convenção (nome em maiúsculas), valor pode ser modificado.
    * **Comentários:** `#` inicia um comentário.
    * **Conversão de Tipo:** `float(input())` ou `int(input())` para cálculos.
    * **Potenciação:** `**` (exponenciação).
    * **Multiplicação:** `*`.

#### 1.1.2.2 String

* **Definição:** Sequências de caracteres entre aspas.
* **Fatiamento (Slicing):** Usando `[]` e `[:]`.
    * **Indexação:** Base 0.
    * **Exemplo (Figura 5):**
        ```python
        mensagem = "Python é uma linguagem muito poderosa"
        print(mensagem[9:]) # Do índice 9 até o final
        print(mensagem[:7]) # Do início até o índice 6 (o 7 é exclusivo)
        print(mensagem[7]) # Apenas o caractere no índice 7
        ```
    * **Explicação:** `[9:]` pega da posição 9 em diante. `[:7]` pega do início até a posição 6. `[7]` pega o caractere na posição 7.
* **Leitura Complementar:** Borges (2010).

### 1.1.3 Estruturas de Condição e de Repetição

* **Introdução:** Essenciais para controle de fluxo e iteração.

#### 1.1.3.1 Estrutura de Condição

* **Jogo de Adivinhação (Exemplo Figura 6):**
    ```python
    # ... (input e conversão para int) ...
    if valor == 10 or valor == 100 or valor == 1000:
        print("Você venceu!!! Adivinhou o número!")
    else:
        print("Você perdeu, não era este o número que eu esperava!")
    ```
    * **Sintaxe:** `if condicao:`, `else:`.
    * **Operadores Lógicos:** `or`, `and`.
    * **Indentação:** Define blocos (4 espaços por convenção).
* **Estrutura `elif` (Exemplo Figura 7 - Jogo com Pontuações):**
    ```python
    # ... (input e conversão para int) ...
    if valor == 10 or valor == 100 or valor == 1000:
        if valor == 10:
            print("Você ganhou 5 pontos, parabéns!")
        elif valor == 100:
            print("Você ganhou 20 pontos, parabéns!")
        else:
            print("Você ganhou 50 pontos, parabéns!")
    else:
        print("Você perdeu, não era este o número que eu esperava!")
    ```
    * **Aninhamento:** Condições dentro de outras.
    * **`elif`:** "else if", testa condições sequencialmente.

#### 1.1.3.2 Estruturas de Repetição

* **Estruturas:** `while`, `while-else`, `for`, `for-else`.
* **Estrutura `while` (Figura 8 - Sintaxe):** Executa enquanto a condição for verdadeira.
    * **Exemplo (Figura 9 - Contagem):**
        ```python
        contador = 1
        while contador < 5:
            print("Contando", contador)
            contador = contador + 1
        print("Terminei de contar")
        ```
    * **Comando `break` (Figura 10):** Sai do loop imediatamente.
        ```python
        # ...
            if contador % 2 == 0:
                break
        # ...
        ```
    * **Estrutura `while-else` (Figura 11):** `else` executa se o loop terminar normalmente (sem `break`).
* **Estrutura `for` (Figura 13 - Sintaxe):** Itera sobre sequências.
    * **Exemplo (Figura 14 - Iterando String):**
        ```python
        for letra in "Python":
            print("Caractere: ", letra)
        ```
    * **Estrutura `for-else` (Figura 15):** `else` executa se o loop terminar normalmente (sem `break`).
* **Aplicação ao Jogo (Figura 16):** Usa `while` para tentativas limitadas, `break` no acerto, `else` do `while` para indicar derrota por tentativas esgotadas. `for` não é adequado para este tipo de controle.
* **Leitura Complementar:** Barry e Griffiths (2018).