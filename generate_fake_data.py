from faker import Faker
import pandas as pd
import random
import numpy as np
from datetime import datetime

fake = Faker("pt_BR")
Faker.seed(42)
random.seed(42)
np.random.seed(42)

NUM_CLIENTES = 100_000
NUM_CONTAS = 150_000
NUM_TRANSACOES = 3_000_000
NUM_EMPRESTIMOS = 20_000

# =====================

def maybe_null(value, chance=0.1):
    return value if random.random() > chance else None

def dirty_text(options):
    return random.choice(options + [None])

def dirty_date():
    options = [
        fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d"),
        fake.date_between(start_date="-5y", end_date="today").strftime("%d/%m/%Y"),
        fake.date_between(start_date="-5y", end_date="today").strftime("%Y/%m/%d"),
        "2023/13/40",
        None
    ]
    return random.choice(options)

# =====================

clientes = []

for i in range(1, NUM_CLIENTES + 1):
    clientes.append({
        "cliente_id": i,
        "nome": maybe_null(fake.name(), 0.05),
        "cpf": maybe_null(fake.cpf(), 0.1),
        "estado": dirty_text(["SP", "Sao Paulo", "São Paulo", "RJ", "MG"]),
        "cidade": maybe_null(fake.city(), 0.1),
        "data_cadastro": dirty_date()
    })

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv("./data/bronze/clientes.csv", index=False)

# =====================

contas = []

for i in range(1, NUM_CONTAS + 1):
    contas.append({
        "conta_id": i,
        "cliente_id": random.randint(1, NUM_CLIENTES + 5000),  # FK quebrada
        "tipo_conta": random.choice(["corrente", "poupanca", None]),
        "saldo_atual": round(random.uniform(-5000, 100_000), 2),
        "status": random.choice(["ativa", "encerrada", None]),
        "data_abertura": dirty_date()
    })

df_contas = pd.DataFrame(contas)
df_contas.to_csv("./data/bronze/contas.csv", index=False)

# =====================

transacoes = []

for i in range(1, NUM_TRANSACOES + 1):
    transacoes.append({
        "transacao_id": i if random.random() > 0.01 else random.randint(1, i),  # duplicata
        "conta_id": random.randint(1, NUM_CONTAS + 10_000),  # FK quebrada
        "data_transacao": dirty_date(),
        "tipo_transacao": random.choice(["credito", "debito", "pix", "ted", "doc", None]),
        "descricao": random.choice([
            "Pagamento boleto", "Compra cartão", "PIX", "TED", None
        ]),
        "valor": round(random.uniform(-2000, 50_000), 2)
    })

df_transacoes = pd.DataFrame(transacoes)
df_transacoes.to_csv("./data/bronze/transacoes.csv", index=False)

# ===================== 


emprestimos = []

for i in range(1, NUM_EMPRESTIMOS + 1):
    emprestimos.append({
        "emprestimo_id": i,
        "cliente_id": random.randint(1, NUM_CLIENTES + 2000),
        "valor_emprestimo": round(random.uniform(-5000, 200_000), 2),
        "parcelas": random.choice([12, 24, 36, 48, None]),
        "taxa_juros_mensal": round(random.uniform(0.1, 15), 2),
        "status": random.choice(["ativo", "quitado", "inadimplente", None]),
        "data_contratacao": dirty_date()
    })

df_emprestimos = pd.DataFrame(emprestimos)
df_emprestimos.to_csv("./data/bronze/emprestimos.csv", index=False)

print("Dados bancários FAKE e SUJOS gerados com sucesso.")
