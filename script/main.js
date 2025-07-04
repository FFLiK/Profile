window.onload = function(){
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            setAnimation();
            setIconAnimation();
            setBackgroundIconAnimation();
            openclose();
            initThemeToggle();
        });
    });
}

function setAnimation() {
    let elements = document.querySelectorAll('.animate');

    let i = 0;
    let n = elements.length;
    for (i; i < n; i++) {
        elements[i].style.opacity = "1.0";
        elements[i].style.transitionDelay = 0.05 * i + "s";
    }
}

function setIconAnimation() {
    let observer = new IntersectionObserver((element) => {
            element[0].target.style.transform = "scale(1.0)";
        }
    )

    let element = document.querySelector('#icon');
    if (element) observer.observe(element);
}

function setBackgroundIconAnimation() {
    let observer = new IntersectionObserver((element) => {
            element[0].target.style.opacity = "0.05";
            element[0].target.style.bottom = "-20%";
        }
    )

    let element = document.querySelector('#background-icon');
    if (element) observer.observe(element);
}

function openclose() {
    const allOpenclose = document.querySelectorAll('.openclose');
    console.log(allOpenclose);
    allOpenclose.forEach(function(openclose) {
        openclose.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href");

            const target = document.querySelector('.' + targetId);
            const targetDisplay = target.style.display;
            if (targetDisplay === 'inline') {
                target.style.display = 'none';
                this.innerHTML = "<small class='clr-tiny' style='text-decoration: underline'>자세히 보기</small>"
            } else {
                target.style.display = 'inline';
                this.innerHTML = "<small class='clr-tiny' style='text-decoration: underline'>접기</small>"
            }
        });
    });
}

function initThemeToggle() {
    // Check for saved theme preference or default to 'dark'
    const savedTheme = localStorage.getItem('theme') || 'dark';
    
    // Apply the saved theme
    applyTheme(savedTheme);
    
    // Create theme toggle button if it doesn't exist
    let themeToggle = document.getElementById('theme-toggle');
    if (!themeToggle) {
        themeToggle = document.createElement('button');
        themeToggle.id = 'theme-toggle';
        themeToggle.className = 'theme-toggle';
        themeToggle.setAttribute('aria-label', 'Toggle theme');
        document.body.appendChild(themeToggle);
    }
    
    // Update button icon
    updateThemeToggleIcon(savedTheme);
    
    // Add click event listener
    themeToggle.addEventListener('click', toggleTheme);
}

function toggleTheme() {
    const currentTheme = document.body.classList.contains('light-theme') ? 'light' : 'dark';
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
    
    applyTheme(newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeToggleIcon(newTheme);
}

function applyTheme(theme) {
    if (theme === 'light') {
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
    }
}

function updateThemeToggleIcon(theme) {
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.innerHTML = theme === 'light' ? '🌙' : '☀️';
    }
}