# 🏥 Sistema de Controle de Estoque Hospitalar

## 📄 Documento de Envoltória

### Título
Sistema de Controle de Estoque Hospitalar

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

## 📘 README Técnico

### Como Executar
Execute o programa em um terminal com Python instalado:
```bash
python estoque.py
