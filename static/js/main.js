document.addEventListener('DOMContentLoaded', function() {
    // ScrollSpy custom logic (since native BS scrollspy needs specific structures that might conflict with our absolute header)
    const sections = document.querySelectorAll('.scroll-section');
    const navLinks = document.querySelectorAll('.nav-pill-custom');
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                // Adjust for fixed header (approx 120px offset)
                const offsetTop = targetSection.getBoundingClientRect().top + window.scrollY - 120;
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Custom Observer for Scrollspy
    const observerOptions = {
        root: null,
        rootMargin: '-130px 0px -50% 0px',
        threshold: 0
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                // Remove active from all
                navLinks.forEach(link => link.classList.remove('active'));
                // Add active to current
                const activeLink = document.querySelector(`.nav-pill-custom[href="#${id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                    // Ensure active link is visible in sticky tab container
                    const container = document.querySelector('.sticky-tabs-container');
                    const linkRect = activeLink.getBoundingClientRect();
                    const containerRect = container.getBoundingClientRect();
                    
                    if (linkRect.left < containerRect.left || linkRect.right > containerRect.right) {
                        container.scrollTo({
                            left: activeLink.offsetLeft - 20,
                            behavior: 'smooth'
                        });
                    }
                }
            }
        });
    }, observerOptions);

    sections.forEach(section => {
        observer.observe(section);
    });

    // --- Search functionality ---
    const searchToggle = document.getElementById('searchToggle');
    const searchInput  = document.getElementById('searchInput');

    if (searchToggle && searchInput) {

        // Mostrar/ocultar el input al hacer clic en el ícono
        searchToggle.addEventListener('click', () => {
            const isHidden = searchInput.classList.toggle('d-none');
            if (!isHidden) {
                searchInput.focus();
            } else {
                searchInput.value = '';
                filterProducts('');
            }
        });

        // Cerrar búsqueda con Escape
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                searchInput.value = '';
                searchInput.classList.add('d-none');
                filterProducts('');
            }
        });

        // Filtrar en tiempo real mientras se escribe
        searchInput.addEventListener('input', (e) => {
            filterProducts(e.target.value.trim().toLowerCase());
        });
    }

    function filterProducts(term) {
        const sections = document.querySelectorAll('.scroll-section');

        sections.forEach(section => {
            const cards = section.querySelectorAll('.product-card');
            const individualRows = section.querySelectorAll('.product-individual-row');
            let visibleCount = 0;

            cards.forEach(card => {
                const text = card.innerText.toLowerCase();
                const match = term === '' || text.includes(term);
                card.style.display = match ? '' : 'none';
                if (match) visibleCount++;
            });

            individualRows.forEach(row => {
                const text = row.innerText.toLowerCase();
                const match = term === '' || text.includes(term);
                row.style.display = match ? '' : 'none';
                if (match) visibleCount++;
            });

            // Ocultar la sección entera si ningún producto coincide
            section.style.display = (term === '' || visibleCount > 0) ? '' : 'none';
        });
    }
});
