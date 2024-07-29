document.addEventListener("DOMContentLoaded", function() {
    // Fade-in animation for new items
    document.querySelectorAll('.list-group-item').forEach(function(item) {
        item.classList.add('fade-in');
        setTimeout(() => item.classList.add('show'), 100);
    });

    // Fade-out animation for removing items
    document.querySelectorAll('.btn-danger').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const item = this.closest('.list-group-item');
            item.classList.add('fade-out');
            setTimeout(() => {
                item.remove();
            }, 300); // Match with CSS transition duration
        });
    });

    // Mark as completed animation
    document.querySelectorAll('.btn-success').forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            const item = this.closest('.list-group-item').querySelector('span');
            item.classList.toggle('text-decoration-line-through');
        });
    });
});
