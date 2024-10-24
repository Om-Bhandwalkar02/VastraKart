

// Navbar
document.addEventListener('DOMContentLoaded', function () {
    const darkModeButton = document.getElementById('dark-mode-button');
    const lightModeButton = document.getElementById('light-mode-button');

    darkModeButton.addEventListener('click', function () {
        document.documentElement.classList.add('dark');
        localStorage.setItem('theme', 'dark');
        darkModeButton.classList.add('hidden');
        lightModeButton.classList.remove('hidden');
    });

    lightModeButton.addEventListener('click', function () {
        document.documentElement.classList.remove('dark');
        localStorage.removeItem('theme');
        lightModeButton.classList.add('hidden');
        darkModeButton.classList.remove('hidden');
    });

    // Check and apply the current theme
    if (localStorage.getItem('theme') === 'dark') {
        document.documentElement.classList.add('dark');
        darkModeButton.classList.add('hidden');
        lightModeButton.classList.remove('hidden');
    } else {
        darkModeButton.classList.remove('hidden');
        lightModeButton.classList.add('hidden');
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const userMenuButton = document.getElementById('user-menu-button');

    if (mobileMenuButton) {
        mobileMenuButton.addEventListener('click', function() {
            const menu = document.getElementById('mobile-menu');
            if (menu) {
                menu.classList.toggle('hidden');
            }
        });
    }

    if (userMenuButton) {
        userMenuButton.addEventListener('click', function() {
            const userMenu = document.getElementById('user-menu');
            if (userMenu) {
                userMenu.classList.toggle('hidden');
            }
        });
    }

    window.addEventListener('click', function(e) {
        const userMenu = document.getElementById('user-menu');
        const userMenuButton = document.getElementById('user-menu-button');
        if (userMenu && userMenuButton && !userMenu.contains(e.target) && !userMenuButton.contains(e.target)) {
            userMenu.classList.add('hidden');
        }
    });
});
