# 🎱 GiftBall — Distributeur de balles surprise

Simulation d'un distributeur de balles surprise, implémentée en Python avec le design pattern **State**.

---

## 📦 Versions

### VERSION 1 — Implémentation simple
Une unique classe `GiftBall` avec un enum `State` pour gérer les états.

### VERSION 2 — Refactoring avec le pattern State
Chaque état devient une classe concrète implémentant l'interface `State`.
Les actions sont déléguées à l'état courant.

### VERSION 3 — Nouvel état double balle
20% de chance d'obtenir 2 balles lors d'un tour de manivelle.
Nouvel état `DispensingDoubleState` ajouté.

### VERSION 4 — Architecture microservices gRPC
Chaque état est exposé comme un service autonome appelable via **gRPC**.
`GiftBall` devient un client qui route les actions vers le bon service.

---

## 🏗️ Architecture
```bash

├──Systeme-Information-Eval
│     ├── src/
│     │   ├── state.py                  # Interface abstraite State
│     │   ├── no_token.py               # État : sans jeton
│     │   ├── one_token.py              # État : avec jeton
│     │   ├── dispensing.py             # État : distribution 1 balle
│     │   ├── dispensing_double.py      # État : distribution 2 balles (20%)
│     │   ├── giftball.py               # Contexte / client gRPC
│     │   ├── giftball.proto            # Définition des services gRPC
│     │   ├── generated/                # Stubs générés par protoc
│     │   └── servers/
│     │       ├── no_token_server.py
│     │       ├── one_token_server.py
│     │       ├── dispensing_server.py
│     │       └── dispensing_double_server.py
│     ├── test/
│     │   └── test_giftball.py
│     ├── database/
│     │   └── schema.sql
│     ├── main.py
│         └── README.md
```
---

## ⚙️ Installation

```bash
pip install grpcio grpcio-tools pytest
```

Générer les stubs gRPC :

```bash
python -m grpc_tools.protoc -I. --python_out=src/generated --grpc_python_out=src/generated src/giftball.proto
```

---

## 🚀 Lancement

### Démarrer tous les serveurs gRPC

```bash
python main.py
```

Les services écoutent sur les ports suivants :

| État                  | Port  |
|-----------------------|-------|
| `NO_TOKEN`            | 50051 |
| `ONE_TOKEN`           | 50052 |
| `DISPENSING`          | 50053 |
| `DISPENSING_DOUBLE`   | 50054 |

### Utiliser la machine

```python
from src.giftball import GiftBall

machine = GiftBall(stock=5)
machine.insert_token()
machine.turn_crank()
```

---

## 🧪 Tests

```bash
python -m pytest
```

---

## 🎨 Design Patterns utilisés

| Pattern   | Rôle |
|-----------|------|
| **State** | Chaque état encapsule son propre comportement, la machine délègue les actions à l'état courant |
| **Strategy** | Similaire au State — la différence étant que c'est ici la machine elle-même qui change d'état automatiquement |

---

## 👤 Auteur

Cyprien — [github.com/cyprien9694](https://github.com/cyprien9694)
bashgit add README.md
git commit -m "Add README"
