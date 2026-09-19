console.log("UI loaded");

function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    sidebar.classList.toggle("open");
}

function toggleSection(id) {
    const el = document.getElementById(id);
    el.classList.toggle("hidden");
}
