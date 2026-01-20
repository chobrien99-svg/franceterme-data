// FranceTerme Interactive Display App

let termsData = [];
let currentIndex = 0;
let currentMode = 'card';

// Initialize the app
async function init() {
    try {
        const response = await fetch('terms_2024.json');
        termsData = await response.json();

        // Update stats
        document.getElementById('stat-total').textContent = '8,309';
        document.getElementById('stat-2024').textContent = termsData.length;

        // Count unique domains
        const uniqueDomains = new Set(termsData.map(t => t.domain));
        document.getElementById('stat-domains').textContent = uniqueDomains.size;

        // Shuffle terms for variety
        shuffleArray(termsData);

        // Setup mode buttons
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.mode-btn').forEach(b => b.classList.remove('active'));
                e.target.classList.add('active');
                currentMode = e.target.dataset.mode;
                renderMode(currentMode);
            });
        });

        // Render initial mode
        renderMode('card');
    } catch (error) {
        console.error('Error loading terms:', error);
        document.getElementById('display-area').innerHTML =
            '<p style="color: white; text-align: center; font-size: 1.5em;">Chargement des termes...</p>';
    }
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
}

function renderMode(mode) {
    const displayArea = document.getElementById('display-area');
    displayArea.innerHTML = '';

    switch(mode) {
        case 'card':
            renderCardMode(displayArea);
            break;
        case 'carousel':
            renderCarouselMode(displayArea);
            break;
        case 'cloud':
            renderCloudMode(displayArea);
            break;
        case 'timeline':
            renderTimelineMode(displayArea);
            break;
        case 'duel':
            renderDuelMode(displayArea);
            break;
    }
}

function renderCardMode(container) {
    const term = termsData[currentIndex];

    const html = `
        <div class="card-container">
            <div class="card" id="flip-card">
                <div class="card-front">
                    <div class="term-french">${term.term}</div>
                    <div class="term-domain">
                        ${getEmoji(term.domain)} ${term.domain}
                        ${term.subdomain ? ' → ' + term.subdomain : ''}
                    </div>
                    <div class="term-date">📅 ${term.date_str}</div>
                    <p style="text-align: center; margin-top: 40px; color: #888; font-style: italic;">
                        Cliquez pour voir la définition! 👆
                    </p>
                </div>
                <div class="card-back">
                    <div class="term-english">🌍 ${term.english || 'N/A'}</div>
                    <div class="term-definition">${term.definition || 'Pas de définition disponible.'}</div>
                    <div class="term-date">📅 ${term.date_str}</div>
                </div>
            </div>
            <div class="nav-buttons">
                <button class="nav-btn" id="prev-btn">⬅️ Précédent</button>
                <button class="nav-btn" id="next-btn">Suivant ➡️</button>
            </div>
        </div>
    `;

    container.innerHTML = html;

    // Add flip functionality
    document.getElementById('flip-card').addEventListener('click', function() {
        this.classList.toggle('flipped');
    });

    // Navigation
    document.getElementById('prev-btn').addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + termsData.length) % termsData.length;
        renderCardMode(container);
    });

    document.getElementById('next-btn').addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % termsData.length;
        renderCardMode(container);
    });
}

function renderCarouselMode(container) {
    const carouselHTML = `
        <div class="carousel">
            ${termsData.slice(0, 20).map(term => `
                <div class="carousel-item">
                    <div class="term-french" style="font-size: 1.8em;">${term.term}</div>
                    <div class="term-domain" style="font-size: 1em;">
                        ${getEmoji(term.domain)} ${term.domain}
                    </div>
                    <div class="term-english" style="font-size: 1.3em; margin: 15px 0;">
                        ${term.english || 'N/A'}
                    </div>
                    <div class="term-definition" style="font-size: 0.95em;">
                        ${truncate(term.definition, 150)}
                    </div>
                    <div class="term-date" style="font-size: 0.9em; margin-top: 15px;">
                        📅 ${term.date_str}
                    </div>
                </div>
            `).join('')}
        </div>
        <p style="text-align: center; color: white; margin-top: 20px; font-size: 1.2em;">
            ⬅️ Faites défiler pour découvrir plus de termes! ➡️
        </p>
    `;

    container.innerHTML = carouselHTML;
}

function renderCloudMode(container) {
    const selectedTerms = termsData.slice(0, 15);

    const cloudHTML = `
        <div class="word-cloud">
            ${selectedTerms.map((term, idx) => `
                <div class="cloud-word" data-index="${idx}">
                    ${term.term}
                </div>
            `).join('')}
        </div>
        <div class="cloud-details hidden" id="cloud-details">
            <div class="term-french" style="font-size: 2em;" id="cloud-term"></div>
            <div class="term-domain" id="cloud-domain"></div>
            <div class="term-english" style="font-size: 1.5em;" id="cloud-english"></div>
            <div class="term-definition" id="cloud-definition"></div>
            <div class="term-date" id="cloud-date"></div>
        </div>
    `;

    container.innerHTML = cloudHTML;

    // Add click handlers
    document.querySelectorAll('.cloud-word').forEach(word => {
        word.addEventListener('click', function() {
            const idx = parseInt(this.dataset.index);
            const term = selectedTerms[idx];

            document.getElementById('cloud-details').classList.remove('hidden');
            document.getElementById('cloud-term').textContent = term.term;
            document.getElementById('cloud-domain').innerHTML = `${getEmoji(term.domain)} ${term.domain}` +
                (term.subdomain ? ` → ${term.subdomain}` : '');
            document.getElementById('cloud-english').textContent = `🌍 ${term.english || 'N/A'}`;
            document.getElementById('cloud-definition').textContent = term.definition || 'Pas de définition disponible.';
            document.getElementById('cloud-date').textContent = `📅 ${term.date_str}`;

            // Scroll to details
            document.getElementById('cloud-details').scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        });
    });
}

function renderTimelineMode(container) {
    // Group by date
    const grouped = {};
    termsData.slice(0, 30).forEach(term => {
        if (!grouped[term.date_str]) {
            grouped[term.date_str] = [];
        }
        grouped[term.date_str].push(term);
    });

    const dates = Object.keys(grouped).sort((a, b) => {
        const dateA = new Date(a.split('/').reverse().join('-'));
        const dateB = new Date(b.split('/').reverse().join('-'));
        return dateB - dateA;
    });

    const timelineHTML = `
        <div class="timeline">
            ${dates.map((date, idx) => `
                <div class="timeline-item">
                    <div class="timeline-dot"></div>
                    <div class="timeline-content">
                        <h3 style="color: #667eea; margin-bottom: 15px;">📅 ${date}</h3>
                        ${grouped[date].map(term => `
                            <div style="margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px solid #eee;">
                                <div class="term-french" style="font-size: 1.5em;">${term.term}</div>
                                <div style="color: #764ba2; font-style: italic; margin: 5px 0;">
                                    ${term.english || 'N/A'}
                                </div>
                                <div style="font-size: 0.9em; color: #666; margin-top: 5px;">
                                    ${getEmoji(term.domain)} ${term.domain}
                                </div>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `).join('')}
        </div>
    `;

    container.innerHTML = timelineHTML;
}

function renderDuelMode(container) {
    const term = termsData[currentIndex];

    const duelHTML = `
        <div class="duel-container">
            <h2 style="text-align: center; color: #667eea; margin-bottom: 20px;">
                ${getEmoji(term.domain)} ${term.domain}
            </h2>
            <div class="duel-sides">
                <div class="duel-side duel-french">
                    <div class="duel-flag">🇫🇷</div>
                    <div class="duel-word">${term.term}</div>
                    <div style="font-size: 1.1em; margin-top: 10px;">Français</div>
                </div>
                <div class="duel-vs">VS</div>
                <div class="duel-side duel-english">
                    <div class="duel-flag">🇬🇧</div>
                    <div class="duel-word">${term.english || 'N/A'}</div>
                    <div style="font-size: 1.1em; margin-top: 10px;">English</div>
                </div>
            </div>
            <div style="margin-top: 40px; padding: 25px; background: #f5f5f5; border-radius: 15px;">
                <h3 style="color: #667eea; margin-bottom: 15px;">📖 Définition</h3>
                <p style="font-size: 1.1em; line-height: 1.6; color: #555;">
                    ${term.definition || 'Pas de définition disponible.'}
                </p>
                <p style="margin-top: 15px; color: #888; text-align: right;">
                    📅 Publié le ${term.date_str}
                </p>
            </div>
            <div class="nav-buttons">
                <button class="nav-btn" id="duel-prev">⬅️ Précédent</button>
                <button class="nav-btn" id="duel-next">Suivant ➡️</button>
            </div>
        </div>
    `;

    container.innerHTML = duelHTML;

    document.getElementById('duel-prev').addEventListener('click', () => {
        currentIndex = (currentIndex - 1 + termsData.length) % termsData.length;
        renderDuelMode(container);
    });

    document.getElementById('duel-next').addEventListener('click', () => {
        currentIndex = (currentIndex + 1) % termsData.length;
        renderDuelMode(container);
    });
}

function getEmoji(domain) {
    const emojiMap = {
        'Biologie': '🧬',
        'Chimie': '⚗️',
        'Spatiologie': '🚀',
        'Économie et gestion d\'entreprise': '💼',
        'Nucléaire': '⚛️',
        'Sports': '⚽',
        'Informatique': '💻',
        'Finance': '💰',
        'Télécommunications': '📡',
        'Défense': '🛡️',
        'Automobile': '🚗',
        'Énergie': '⚡',
        'Environnement': '🌍',
        'Santé': '⚕️',
        'Agriculture': '🌾',
        'Transports': '🚆'
    };

    return emojiMap[domain] || '📚';
}

function truncate(str, length) {
    if (!str) return '';
    if (str.length <= length) return str;
    return str.substring(0, length) + '...';
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
} else {
    init();
}
