(() => {
    const root = document.documentElement;
    const buttons = document.querySelectorAll('[data-theme-toggle]');

    function updateButtons(isLight) {
        buttons.forEach((button) => {
            const label = isLight ? 'Switch to dark mode' : 'Switch to light mode';
            button.setAttribute('aria-label', label);
            button.setAttribute('aria-pressed', String(isLight));
            button.title = label;
            const icon = button.querySelector('[data-theme-icon]');
            if (icon) icon.className = `fas ${isLight ? 'fa-moon' : 'fa-sun'}`;
        });
    }

    updateButtons(root.classList.contains('theme-light'));
    buttons.forEach((button) => {
        button.addEventListener('click', () => {
            const isLight = !root.classList.contains('theme-light');
            root.classList.toggle('theme-light', isLight);
            root.classList.toggle('theme-dark', !isLight);
            localStorage.setItem('portfolio-theme', isLight ? 'light' : 'dark');
            updateButtons(isLight);
        });
    });
})();
