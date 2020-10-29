var shiftWindow = function() { scrollBy(0, -120) };
if (location.hash) shiftWindow();
window.addEventListener("hashchange", shiftWindow);