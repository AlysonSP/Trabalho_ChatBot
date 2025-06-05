document.addEventListener('DOMContentLoaded', function() {
    const messagesContent = document.getElementById('messages-content');
    const messageInput = document.getElementById('message-input');
    const messageSubmit = document.getElementById('message-submit');
    const chatAvatar = document.querySelector('.chat-title .avatar img').src; // Pega o avatar do bot
    let sessionActive = true; // Controla se a sessão está ativa

    // Função para adicionar mensagem à UI
    function addMessageToUI(text, type = 'bot', avatarSrc = chatAvatar) {
        const msgContainer = document.createElement('div'); // Container para avatar e texto
        msgContainer.classList.add('message');
        if (type === 'user') {
            msgContainer.classList.add('message-personal');
        } else {
            // Adicionar avatar para mensagens do bot
            const avatarDiv = document.createElement('div');
            avatarDiv.classList.add('avatar');
            const img = document.createElement('img');
            img.src = avatarSrc;
            img.alt = (type === 'bot' ? "Bot" : "User") + " Avatar";
            avatarDiv.appendChild(img);
            msgContainer.appendChild(avatarDiv);
        }

        // Adiciona o texto da mensagem. Quebras de linha do bot são convertidas para <br>
        const textNode = document.createElement('span'); 
        textNode.innerHTML = text.replace(/\n/g, '<br>');
        msgContainer.appendChild(textNode);


        const timestamp = document.createElement('span');
        timestamp.classList.add('timestamp');
        timestamp.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
        // Adicionar timestamp dentro do textNode se for msg pessoal, ou após se for bot
        // Para melhor alinhamento com o CSS original, vamos adicionar sempre no final do msgContainer
        msgContainer.appendChild(timestamp);
        
        messagesContent.appendChild(msgContainer);
        // messagesContent.scrollTop = messagesContent.scrollHeight; // Auto-scroll
        // Scroll para a última mensagem
        msgContainer.scrollIntoView({ behavior: 'smooth', block: 'end' });
        
        // Adiciona a classe 'new' para animação e remove depois
        msgContainer.classList.add('new');
        setTimeout(() => {
            msgContainer.classList.remove('new');
        }, 500); // Duração da animação 'bounce'
    }

    // Função para mostrar mensagem de "digitando..."
    function showLoadingIndicator() {
        if (document.querySelector('.message.loading')) return; // Evita múltiplos loaders

        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('message', 'loading'); // Bot está digitando
        
        const avatarDiv = document.createElement('div');
        avatarDiv.classList.add('avatar');
        const img = document.createElement('img');
        img.src = chatAvatar; // Avatar do bot
        img.alt = "Bot Avatar";
        avatarDiv.appendChild(img);
        loadingDiv.appendChild(avatarDiv); // Adiciona avatar ao loading

        const spanDots = document.createElement('span'); // Para os pontinhos
        loadingDiv.appendChild(spanDots);

        messagesContent.appendChild(loadingDiv);
        // loadingDiv.scrollIntoView({ behavior: 'smooth', block: 'end' });
        messagesContent.scrollTop = messagesContent.scrollHeight;

    }

    function hideLoadingIndicator() {
        const loadingDiv = document.querySelector('.message.loading');
        if (loadingDiv) {
            loadingDiv.remove();
        }
    }

    // Função para enviar mensagem ao backend
    async function sendMessage(messageText) {
        if (!sessionActive && messageText.toLowerCase() !== 'iniciar') {
             addMessageToUI("A sessão anterior foi encerrada. Digite 'iniciar' para começar uma nova conversa.", 'bot');
             return;
        }
        // Permite enviar "iniciar" mesmo que vazio (após trim) se a sessão não estiver ativa
        if (messageText.trim() === '' && (sessionActive || messageText.toLowerCase() !== 'iniciar')) return;


        let endpoint = '/chat';
        let payload = { message: messageText };
        let methodType = 'POST';

        if (messageText.toLowerCase() === 'iniciar' && !sessionActive) {
            endpoint = '/start_chat'; 
            payload = {}; 
            methodType = 'GET';
            // Não adiciona "iniciar" como mensagem do usuário visualmente, apenas reinicia.
        } else {
             addMessageToUI(messageText, 'user');
        }
        
        const currentMessageValue = messageInput.value; // Salva antes de limpar
        messageInput.value = ''; 
        showLoadingIndicator();

        try {
            const fetchOptions = {
                method: methodType,
                headers: {
                    'Content-Type': 'application/json',
                }
            };
            if (methodType === 'POST') {
                fetchOptions.body = JSON.stringify(payload);
            }

            const response = await fetch(endpoint, fetchOptions);
            const data = await response.json();
            
            hideLoadingIndicator();

            if (data.responses && data.responses.length > 0) {
                data.responses.forEach((res, index) => {
                    setTimeout(() => { 
                        addMessageToUI(res, 'bot');
                    }, index * 400); // Pequeno delay entre mensagens do bot
                });
            }
            sessionActive = data.session_active;
            if (!sessionActive) {
                messageInput.placeholder = "Sessão encerrada. Digite 'iniciar' para recomeçar.";
                messageInput.disabled = false; 
            } else {
                messageInput.placeholder = "Digite sua opção ou mensagem...";
                messageInput.disabled = false;
            }

        } catch (error) {
            hideLoadingIndicator();
            addMessageToUI('Erro ao conectar com o servidor. Tente novamente.', 'bot');
            console.error('Error:', error);
            // Se houve erro, talvez o usuário queira reenviar a mensagem que não foi
            if (type !== 'user' && messageText.toLowerCase() !== 'iniciar') {
                 messageInput.value = currentMessageValue; // Restaura a mensagem não enviada
            }
            sessionActive = false; 
            messageInput.placeholder = "Erro. Digite 'iniciar' para tentar recomeçar.";
        }
    }

    // Event listeners
    messageSubmit.addEventListener('click', () => sendMessage(messageInput.value));
    messageInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) { 
            e.preventDefault(); 
            sendMessage(messageInput.value);
        }
    });

    // Iniciar a conversa quando a página carrega
    async function startConversation() {
        messageInput.disabled = true; // Desabilita input enquanto carrega
        showLoadingIndicator();
        try {
            const response = await fetch('/start_chat', { method: 'GET' });
            const data = await response.json();
            hideLoadingIndicator();
            if (data.responses && data.responses.length > 0) {
                 data.responses.forEach((res, index) => {
                    setTimeout(() => {
                        addMessageToUI(res, 'bot');
                    }, index * 300); // Delay inicial
                });
            }
            sessionActive = data.session_active;
             if (!sessionActive) { // Pouco provável ao iniciar, mas para consistência
                messageInput.placeholder = "Sessão encerrada. Digite 'iniciar' para recomeçar.";
            } else {
                messageInput.placeholder = "Digite sua opção ou mensagem...";
            }
            messageInput.disabled = false; 
        } catch (error) {
            hideLoadingIndicator();
            addMessageToUI('Não foi possível iniciar o chat. Verifique sua conexão ou tente mais tarde.', 'bot');
            console.error('Error starting chat:', error);
            messageInput.placeholder = "Erro ao carregar. Tente recarregar a página.";
            // messageInput.disabled = true; // Mantém desabilitado em caso de erro total no início
        }
    }

    startConversation(); 
});