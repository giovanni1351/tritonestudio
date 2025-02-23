// Animação das seções
const sections = document.querySelectorAll('section');
const observerOptions = { threshold: 0.2 };
const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible');
            obs.unobserve(entry.target);
        }
    });
}, observerOptions);
sections.forEach(section => observer.observe(section));

// Função para criar o iframe
function createIframe(container) {
    const iframeSrc = container.getAttribute('data-src');
    const iframe = document.createElement('iframe');
    iframe.setAttribute('src', iframeSrc);
    iframe.setAttribute('width', '100%');
    iframe.setAttribute('height', '100%');
    iframe.setAttribute('frameborder', '0');
    iframe.setAttribute('allowfullscreen', 'true');
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
function toggleMute(iframe, mute) {
    if (iframe) {
        iframe.muted = mute;
    }
}
document.querySelectorAll('.iframe-container').forEach(container => {
    const iframe = container.querySelector('.game-iframe');

    // Quando o mouse entra no container, desmuta o iframe
    container.addEventListener('mouseenter', () => {
        toggleMute(iframe, false);
    });

    // Quando o mouse sai do container, muta o iframe
    container.addEventListener('mouseleave', () => {
        toggleMute(iframe, true);
    });
});
document.addEventListener('DOMContentLoaded', function () {
    // Configuração do Observer para o fade do background
    const bgSections = document.querySelectorAll('#home, #detalhes-jogo2, #detalhes-jogo1');
    const bgObserverOptions = {
        threshold: 0.4 // Ajuste conforme necessário
    };

    const bgObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            entry.target.classList.toggle('active-bg', entry.isIntersecting);
        });
    }, bgObserverOptions);

    bgSections.forEach(section => {
        bgObserver.observe(section);
    });

    // Mantenha o observer existente para as animações das seções
    const sections = document.querySelectorAll('section');
    const observerOptions = { threshold: 0.2 };
    const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                obs.unobserve(entry.target);
            }
        });
    }, observerOptions);
    sections.forEach(section => observer.observe(section));
});
