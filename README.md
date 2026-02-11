# 🎮 GameVault - E-commerce de Jogos Digitais

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Django](https://img.shields.io/badge/Django-4.0%2B-green)
![TailwindCSS](https://img.shields.io/badge/Tailwind-CSS-blueviolet)
![Stripe](https://img.shields.io/badge/Stripe-Payment-635bff)

**GameVault** é uma plataforma Fullstack de venda e distribuição de jogos digitais. O projeto simula o fluxo completo de um e-commerce moderno: desde a vitrine e busca de produtos, passando por um carrinho de compras dinâmico via AJAX, até o checkout seguro com Stripe e a liberação imediata do acesso ao produto na biblioteca do usuário.

---

## 📸 Screenshots

<div style="display: flex; gap: 10px;">
    <img src="static/images/screenshot_home.png" alt="Home Page" width="400">
    <img src="static/images/screenshot_library.png" alt="Minha Biblioteca" width="400">
</div>

---

## 🚀 Funcionalidades

- **🛒 Carrinho Dinâmico (AJAX):** Adição e remoção de itens instantaneamente sem recarregar a página, calculando totais em tempo real.
- **💳 Pagamentos Reais:** Integração com **Stripe Checkout** para processamento seguro de cartões de crédito.
- **🔐 Autenticação:** Sistema completo de Login, Cadastro e Logout.
- **📦 Entrega Digital:** Sistema de liberação automática. O jogo só aparece na "Biblioteca" do usuário após a confirmação do pagamento.
- **🎨 UI Moderna:** Interface responsiva construída com **Tailwind CSS**, incluindo suporte a **Dark Mode**.
- **🔍 Busca:** Sistema de filtragem de produtos por nome.

---

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python, Django Framework.
- **Frontend:** HTML5, Tailwind CSS, JavaScript (Fetch API).
- **Banco de Dados:** SQLite (Dev).
- **Pagamentos:** Stripe API (SDK Python).
- **Segurança:** Variáveis de ambiente com `python-decouple`.

---

## 📦 Como Rodar o Projeto

Pré-requisitos: Python instalado.

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/SEU-USUARIO/GameVault.git](https://github.com/SEU-USUARIO/GameVault.git)
   cd GameVault