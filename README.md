# 🏥 Sistema de Controle de Estoque Hospitalar

Grupo:
- Adolfo Kentaro Hada   RM:556884
- Bruno Otavio SIlva de Oliveira   RM:556196
- Guilherme Flores Pereira de Almeida   RM:554948
- Luiz Fernando de Aragão Souza   RM:555561
- Marcello de Freitas Almeida   RM:557531

## 📄 Documento de Envoltória

### Título
Sistema de Controle de Estoque Hospitalar (SCEH)

### Objetivo
Este sistema tem como propósito gerenciar o estoque de insumos hospitalares, monitorando se os níveis estão dentro do ideal, identificando itens em falta ou em excesso, permitindo buscas otimizadas e facilitando a tomada de decisão para reposição.

### Público-Alvo
Profissionais da saúde e da gestão hospitalar responsáveis pelo almoxarifado, farmácia e distribuição de materiais e medicamentos.

### Funcionalidades Principais
- Inserção de novos insumos no estoque
- Exibição e busca de insumos por localização
- Detecção de insumos em falta ou sobrando com base em estoque ideal
- Busca por atributos com ordenação e busca binária
- Atualização da quantidade dos insumos
- Interface interativa via terminal

---

## 📌 Hipóteses e Dados Considerados

- O sistema trabalha com uma estrutura de **lista de dicionários**, onde cada dicionário representa um insumo.
- Cada insumo possui os seguintes campos:
  - `id`: identificador numérico único
  - `nome`: nome do insumo ou medicamento
  - `local`: local (ex: UTI, Enfermaria, Farmácia)
  - `quantidade`: quantidade atual em estoque
  - `ideal`: quantidade considerada ideal para aquele local
- Um insumo é considerado:
  - **Em falta**: quando `quantidade < ideal`
  - **Sobrando**: quando `quantidade > ideal`
  - **Adequado**: quando `quantidade == ideal`
- A busca por insumos é otimizada através de:
  - Ordenação por campo escolhido (`id`, `nome`, etc.)
  - Busca binária após a ordenação
- Os dados de teste estão pré-carregados para facilitar o uso sem a necessidade de inserção manual.

---

## 🧪 Estrutura dos Dados

Os insumos são armazenados na lista `Estoque`, com o seguinte formato:

```python
{
    "id": 101,
    "nome": "Soro Fisiológico 0.9%",
    "local": "Enfermaria",
    "quantidade": 12,
    "ideal": 20
}
```

Cada insumo representa uma entrada independente do estoque, associada a uma localidade hospitalar.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem**: Python 3.10 ou superior
- **Interface**: Terminal interativo
- **Algoritmos utilizados**:
  - Ordenação por seleção (Selection Sort) — para ordenar insumos com base em um campo específico
  - Busca binária — para localizar insumos de forma eficiente após ordenação

---

## ✅ Requisitos para Execução

- Python instalado na máquina (versão 3.10 ou superior)
- Terminal ou IDE capaz de executar scripts `.py`

Para executar o programa:
```bash
python estoque.py
```

---

## 🧾 Normas, Estilo e Convenções de Código

- **Estilo de código**:
  - Funções nomeadas com `snake_case` (`inserir_insumo`, `buscar_insumo`).
  - Variáveis descritivas e concisas (`quantidade_atual`, `local_estoque`).
- **Modularização**:
  - Cada funcionalidade foi separada em funções específicas.
  - O código é reutilizável e organizado para fácil manutenção.
- **Comentários**:
  - Cada função tem comentários explicativos, incluindo complexidade computacional.
  - Trechos importantes de código estão documentados com explicações de lógica.
- **Tratamento de erros**:
  - Entradas numéricas validadas com `try/except`.
  - Campos opcionais com validação para evitar falhas.
- **Interface com o usuário**:
  - Menu claro e direto.
  - Feedback imediato após cada operação.
