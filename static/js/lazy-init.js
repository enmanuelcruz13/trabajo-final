// Small helper to apply lazy background-image swapping for elements with data-bg
document.addEventListener('lazyloaded', function(e){
  // lazysizes will fire lazyloaded for images; for elements using data-bg we swap background now
  var el = e.target;
  if(el.dataset && el.dataset.bg){
    el.style.backgroundImage = "url('" + el.dataset.bg + "')";
  }
}, {passive:true});

// For elements that are not images but have data-bg attribute, trigger load when in viewport
document.addEventListener('DOMContentLoaded', function(){
  if(!('IntersectionObserver' in window)) return;
  var els = document.querySelectorAll('[data-bg]');
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        var el = entry.target;
        el.style.backgroundImage = "url('" + el.dataset.bg + "')";
        io.unobserve(el);
      }
    });
  });
  els.forEach(function(el){ io.observe(el); });
});
