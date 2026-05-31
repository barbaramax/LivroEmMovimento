# Livro em Movimento

Projeto extensionista desenvolvido na disciplina de Desenvolvimento Web 3.
Site desenvolvido para a ONG Livro em Movimento, com o objetivo de facilitar o acesso às informações da organização e permitir que pessoas doem livros, se cadastrem como voluntárias e entrem em contato com a equipe.

---

## Equipe de Desenvolvimento

**Backend**
- Barbara Max
- Lucas Laiun

Responsáveis pelo desenvolvimento da API, modelagem do banco de dados e integração entre os serviços da aplicação.

**Frontend**
- Ana Sara Mousinho
- Vitória Monteiro

Responsáveis pelo desenvolvimento da interface do sistema, componentes visuais e experiência do usuário.

---

## Sobre o Projeto

A ONG Livro em Movimento atua na promoção da leitura, da educação e da cultura por meio de projetos e ações sociais. O site foi criado para divulgar as atividades da organização e centralizar as formas de participação da comunidade.

---

## Funcionalidades

- Formulário de doação de livros (nome, e-mail, telefone, quantidade)
- Formulário de cadastro de voluntários com seleção de área de interesse
- Página de contato com redirecionamento para WhatsApp e e-mail
- Listagem de notícias e eventos cadastrados
- Painel administrativo Django para gerenciar conteúdo do site

---

## Tecnologias Utilizadas

**Backend**
- Django 5.2 — framework web Python, responsável pela API, banco de dados e painel admin
- django-cors-headers — controle de CORS entre frontend e backend
- dj-database-url — configuração do banco via variável de ambiente
- Cloudinary + django-cloudinary-storage — armazenamento de mídia em nuvem
- SQLite — sistema gerenciador de banco de dados

**Frontend**
- React — biblioteca para construção da interface
- Vite — ferramenta de build e servidor de desenvolvimento
- Tailwind CSS — estilização via classes utilitárias
- django-vite — integração entre o build do Vite e o Django

**Deploy**
- Vercel — plataforma utilizada para hospedagem da aplicação.
---

