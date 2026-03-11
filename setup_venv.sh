#!/bin/bash

# Script para criar e ativar virtual environment
echo "Removendo ambiente antigo (se existir)..."
rm -rf .venv

if ! command -v python3.14 &> /dev/null
then
  echo "Python 3.14 não encontrado. Instale-o antes de rodar este script."
  exit 1
fi

echo "Criando virtual environment..."
python3.14 -m venv .venv

echo "Ativando virtual environment..."
source .venv/bin/activate

echo "Atualizando pip..."
pip install --upgrade pip

if [ -f "requirements.txt" ]; then
  echo "Instalando dependências do requirements.txt..."
  pip install -r requirements.txt
else
  echo "Arquivo requirements.txt não encontrado."
fi

echo "Setup concluído. Ambiente virtual ativo."
echo "Para desativar, use: deactivate"

git update-index --assume-unchanged run.sh .env.local run2.sh 
