document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('.fav-form').forEach(function (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      const url = form.action;
      const btn = form.querySelector('.fav-btn');
      fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': getCookie('csrftoken'),
          'X-Requested-With': 'XMLHttpRequest',
          'Accept': 'application/json'
        },
      }).then(resp => resp.json()).then(data => {
        if (data && typeof data.favorited !== 'undefined') {
          btn.classList.toggle('is-fav', data.favorited);
        }
      }).catch(() => {});
    });
  });
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
