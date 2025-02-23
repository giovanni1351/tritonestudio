AOS.init({
    duration: 1000,
    easing: 'ease-in-out',
    once: true
});

// Função para criar o iframe
function createIframe(container) {
    const iframeSrc = container.getAttribute('data-src');
    const iframe = document.createElement('iframe');
    iframe.setAttribute('src', iframeSrc);
    iframe.setAttribute('width', '100%');
    iframe.setAttribute('height', '800px');
    container.appendChild(iframe);
    container.iframe = iframe; // Armazena a referência do iframe
}

// Adiciona eventos aos containers
document.querySelectorAll('.iframe-containerNormal').forEach(container => {
    // Evento de clique no overlay para criar o iframe
    const overlay = container.querySelector('.play-overlay');
    overlay.addEventListener('click', function () {
        createIframe(container);
        overlay.remove();
    });

    // Evento de mouseleave para focar no iframe
    container.addEventListener('mouseleave', function () {
        if (container.iframe) {
            container.iframe.focus();
        }
    });
});