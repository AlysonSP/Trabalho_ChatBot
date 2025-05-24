# 🤖 Chatbot de Suporte Pinpoint: Otimizando o Atendimento Técnico 🚀

[![Status do Projeto](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)](https://github.com/SEU_USUARIO_GH/SEU_REPOSITORIO)
[![Linguagem](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/Flask-2.x-orange.svg)](https://flask.palletsprojects.com/)
[![Licença](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Otimizando a experiência de suporte técnico da Pinpoint Tecnologia através de um assistente virtual inteligente.**

---

## 📖 Sumário

*   [🎯 Sobre o Projeto](#sobre-o-projeto)
    *   [🏢 A Empresa Parceira: Pinpoint Tecnologia](#a-empresa-parceira-pinpoint-tecnologia)
    *   [❌ O Desafio](#o-desafio)
    *   [✅ Nossa Solução](#nossa-solu%C3%A7%C3%A3o)
*   [✨ Funcionalidades Chave](#funcionalidades-chave)
*   [👁️‍🗨️ Demonstração Visual (Preview)](#demonstra%C3%A7%C3%A3o-visual-preview)
*   [💬 Fluxo de Conversação](#fluxo-de-conversa%C3%A7%C3%A3o)
*   [🛠️ Tecnologias Utilizadas](#tecnologias-utilizadas)
*   [🚀 Começando](#come%C3%A7ando)
    *   [📋 Pré-requisitos](#pr%C3%A9-requisitos)
    *   [⚙️ Instalação e Execução](#instala%C3%A7%C3%A3o-e-execu%C3%A7%C3%A3o)
*   [🗺️ Roadmap do Projeto](#roadmap-do-projeto)
*   [🤝 Como Contribuir](#como-contribuir)
*   [👥 Equipe](#equipe)
*   [👨‍🏫 Orientação](#orienta%C3%A7%C3%A3o)
*   [📜 Licença](#licen%C3%A7a)
*   [🙏 Agradecimentos](#agradecimentos)

---

## 🎯 Sobre o Projeto

Este projeto acadêmico, desenvolvido no âmbito da disciplina "APLICAÇÕES DE CLOUD, IOT E INDUSTRIA 4.0 EM PYTHON" do curso de Análise e Desenvolvimento de Sistemas, visa criar um **chatbot inteligente** para a **Pinpoint Tecnologia e Pesquisa em Software LTDA**. O objetivo principal é otimizar o processo de abertura de chamados (tickets) de suporte técnico, melhorando a eficiência operacional da Pinpoint e a experiência de seus clientes.

### 🏢 A Empresa Parceira: Pinpoint Tecnologia

*   **Nome:** Pinpoint Tecnologia e Pesquisa em Software LTDA
*   **Localização:** Mooca – SP
*   **Setor:** Tecnologia
*   **Resumo:** Desde 2009, a Pinpoint é líder em soluções customizadas de monitoração e gerenciamento de infraestrutura de TI, redes, aplicações e sistemas, oferecendo suporte especializado 24/7 para grandes empresas no Brasil.

### ❌ O Desafio

A Pinpoint enfrenta desafios comuns na gestão de suporte:
*   **Coleta de Informações Incompleta:** Clientes frequentemente omitem detalhes cruciais ao abrir chamados.
*   **Atrasos na Resolução:** A falta de dados iniciais completos leva a demoras na análise e solução.
*   **Comunicação Fragmentada:** Múltiplas interações são necessárias para obter o panorama completo do problema.
*   **Impacto na Agilidade:** A eficiência do suporte é comprometida, afetando a satisfação do cliente.

### ✅ Nossa Solução

Propomos um **chatbot inteligente** que atuará como o primeiro ponto de contato para a abertura de chamados:
1.  **Coleta Estruturada:** Guiará o cliente por um fluxo conversacional dinâmico, assegurando que todas as informações relevantes (descrição do problema, criticidade, sistemas impactados, logs iniciais, etc.) sejam coletadas de forma padronizada.
2.  **Organização Imediata:** Os dados são organizados e formatados automaticamente.
3.  **Notificação Eficaz:** Um e-mail detalhado e completo é enviado instantaneamente para a equipe de suporte da Pinpoint, contendo todas as informações necessárias para uma análise inicial rápida.
4.  **Modernização:** Simplifica e moderniza o processo de suporte, oferecendo uma experiência mais fluida e ágil.

---

## ✨ Funcionalidades Chave

*   💬 **Interface Conversacional Intuitiva:** Interação amigável e guiada.
*   📝 **Coleta Detalhada de Dados:** Perguntas dinâmicas para capturar informações essenciais.
*   🗂️ **Menus Interativos e Respostas Condicionais:** Facilita a entrada de dados e personaliza o fluxo.
*   ✅ **Validação de Entradas:** Garante a qualidade dos dados fornecidos (ex: formato de e-mail, arquivos de log).
*   📧 **Notificação Automática por E-mail:** Envio de chamados completos para a equipe de suporte.
*   🧠 **Base de Conhecimento (FAQs):** Respostas automáticas para perguntas frequentes.
*   💾 **Persistência de Dados:** Armazenamento de interações e configurações em banco de dados SQLite.
*   🌐 **Interface Web Acessível:** Desenvolvida com Flask, HTML e CSS.

---

## 👁️‍🗨️ Demonstração Visual (Preview)

*(Aqui seria o local ideal para inserir um GIF animado mostrando a interação com o chatbot ou screenshots da interface.)*

---

## 💬 Fluxo de Conversação

O chatbot seguirá um fluxo lógico para coletar as informações necessárias:

1.  👋 **Saudação e Boas-vindas:** Início da interação.
2.  👤 **Identificação (Opcional):** Coleta de informações básicas do cliente.
3.  📄 **Descrição do Problema:** Campo aberto para o cliente detalhar a ocorrência.
4.  🚨 **Nível de Urgência:** Seleção através de menu (Baixa, Média, Alta, Crítica).
5.  💻 **Sistema/Serviço Afetado:** Identificação do componente com problema.
6.  📎 **Anexos (Opcional):** Possibilidade de anexar logs ou screenshots.
7.  📞 **Informações de Contato:** Confirmação ou coleta de e-mail/telefone.
8.  📋 **Resumo e Confirmação:** Apresentação dos dados coletados para validação do cliente.
9.  📨 **Submissão do Chamado:** Envio do e-mail para a equipe Pinpoint.
10. 🎉 **Confirmação e Próximos Passos:** Mensagem de sucesso e o que esperar.

*(Um diagrama de fluxo detalhado estará disponível na pasta `/docs` ou como anexo no relatório do projeto.)*

---

## 🛠️ Tecnologias Utilizadas

O projeto é construído com as seguintes tecnologias e conceitos:

*   **Linguagem de Programação:** ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
*   **Framework Web:** ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
*   **Frontend:** ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) (JavaScript opcional)
*   **Banco de Dados:** ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
*   **Ambiente de Desenvolvimento:** Jupyter Notebook (para prototipagem e testes iniciais)
*   **Conceitos Aplicados:**
    *   Desenvolvimento Orientado a Objetos
    *   APIs (para envio de e-mail e futuras integrações)
    *   Manipulação de Dados
    *   Arquitetura de Sistemas Distribuídos (básico)
    *   Testes Unitários e de Integração

---

## 🚀 Começando

Siga estas instruções para configurar e executar o projeto em seu ambiente local.

### 📋 Pré-requisitos

*   Python 3.9 ou superior
*   Pip (gerenciador de pacotes Python)
*   Git

### ⚙️ Instalação e Execução

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/SEU_USUARIO_GH/SEU_REPOSITORIO.git
    cd SEU_REPOSITORIO
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```bash
    python -m venv venv
    ```
    *   No Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   No macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Certifique-se de que o arquivo `requirements.txt` está atualizado com todas as bibliotecas necessárias.)*

4.  **Configure as variáveis de ambiente (se necessário):**
    Crie um arquivo `.env` na raiz do projeto se houver configurações sensíveis (ex: credenciais de e-mail). Exemplo:
    ```env
    EMAIL_HOST_USER="seu_email_de_envio@example.com"
    EMAIL_HOST_PASSWORD="sua_senha_de_aplicativo"
    PINPOINT_SUPPORT_EMAIL="suporte@pinpoint.com.br"
    ```
    *(Adicione `.env` ao seu `.gitignore`!)*

5.  **Execute a aplicação Flask:**
    ```bash
    flask run
    # Ou
    python app.py
    ```

6.  Acesse o chatbot em seu navegador: `http://127.0.0.1:5000/` (ou a porta configurada).

---

## 🗺️ Roadmap do Projeto

O desenvolvimento seguirá as entregas definidas no Estudo de Caso da disciplina:

| Entrega       | Data Prevista | Status        | Principais Marcos                                                                                             |
| :------------ | :------------ | :------------ | :------------------------------------------------------------------------------------------------------------ |
| **1ª Entrega** | 04/04/2025    | ⏳ Planejado   | Definição da empresa e escopo (Concluído), Requisitos Funcionais, Plano de Execução, Cronograma (Project Libre), 1ª Versão do Relatório. |
| **2ª Entrega** | 09/05/2025    | ⏳ Planejado   | Requisitos Não Funcionais, Diagrama de Fluxo de Mensagens, Código Inicial (Flask, ambiente), Funcionalidades básicas do chatbot, Plano de Testes, 2ª Versão do Relatório. |
| **3ª Entrega** | 06/06/2025    | ⏳ Planejado   | Código Final com todas as funcionalidades implementadas, Testes completos, Documentação final do projeto, Relatório Extensionista (assinado), Apresentação do Chatbot funcional. |

---

## 🤝 Como Contribuir

Este é um projeto acadêmico, mas contribuições que visem melhorar o código, a documentação ou sugerir novas funcionalidades são bem-vindas!

1.  Faça um Fork do projeto.
2.  Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`).
3.  Realize o Commit de suas mudanças (`git commit -m 'Add some AmazingFeature'`).
4.  Realize o Push para a Branch (`git push origin feature/AmazingFeature`).
5.  Abra um Pull Request.

Alternativamente, sinta-se à vontade para abrir uma *Issue* para relatar bugs ou sugerir melhorias.

---

## 👥 Equipe

*   **Gustavo Henrique Dias Fogo** - [GitHub](https://github.com/SEU_USUARIO_GH) - (Matrícula: 202403590832)
*   **Gustavo Arthur Dubiani Cruz** - [GitHub](https://github.com/SEU_USUARIO_GH) - (Matrícula: 202403481091)
*   **Ildefonso Gomes Cardoso Junior** - [GitHub](https://github.com/SEU_USUARIO_GH) - (Matrícula: 202402653903)
*   **Alyson Silva Prado** - [GitHub](https://github.com/AlysonSP) - (Matrícula: 202403760371)

---

## 👨‍🏫 Orientação

*   **Prof. Fabio da Roza Oliveira** - Professor Orientador da Disciplina.

---

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🙏 Agradecimentos

*   À **Pinpoint Tecnologia e Pesquisa em Software LTDA** pela oportunidade de desenvolver uma solução para um desafio real.
*   À **Universidade Estácio** e ao corpo docente do curso de Análise e Desenvolvimento de Sistemas.
*   A todos que direta ou indiretamente contribuíram com ideias e apoio.

---

**[⬆ Voltar ao topo](#-chatbot-de-suporte-pinpoint-otimizando-o-atendimento-técnico-)**
