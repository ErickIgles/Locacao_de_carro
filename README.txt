# 🚗 Projeto AlugaFacil


## 📌 Sobre

AlugaFacil é uma plataforma responsiva para aluguel de carros, permitindo que usuários realizem cadastros, façam login e pesquisem por veículos disponíveis. O sistema inclui:

- 🔹 Barra de pesquisa e filtragem por marcas.
- 🔹 Página de detalhes do veículo com informações completas.
- 🔹 Processo de locação e cancelamento de aluguel.
- 🔹 Perfil do usuário com opções de configuração.
- 🔹 Apenas usuários cadastrados podem acessar as funcionalidades de locação.

## 🛠 Tecnologias Utilizadas

 Tecnologia  
 🐍 Python ->   Linguagem principal      
 🌐 Django ->   Framework web            
 🎨 HTML ->    Marcação de conteúdo     
 🎨 CSS  ->     Estilização responsiva   
 🗄 SQLite ->  Banco de dados           



## 📥 Instalação

git clone https://github.com/ErickIgles/Locacao_de_carro.git
cd AlugaFacil
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
