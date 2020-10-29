var shiftWindow = function() { scrollBy(0, -140) };
if (location.hash) shiftWindow();
window.addEventListener("hashchange", shiftWindow);