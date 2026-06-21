document.addEventListener('DOMContentLoaded', function () {
  const ratingWidget = document.querySelector('.star-rating-widget');
  if (ratingWidget) {
    const url = ratingWidget.dataset.url;
    const stars = ratingWidget.querySelectorAll('input[type="radio"]');
    stars.forEach(function (star) {
      star.addEventListener('change', function () {
        const ratingValue = this.value;
        fetch(url, {
          method: 'POST',
          headers: {
            'X-CSRFToken': getCookie('csrftoken'),
            'Content-Type': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json'
          },
          body: JSON.stringify({ puntuacion: ratingValue })
        })
        .then(resp => resp.json())
        .then(data => {
          if (data && data.success) {
            const avgNum = document.querySelector('.rating-avg-num');
            const countText = document.querySelector('.rating-count');
            if (avgNum) avgNum.textContent = data.promedio;
            if (countText) {
              countText.textContent = data.total === 1 ? '1 calificación' : `${data.total} calificaciones`;
            }
            const visualStars = document.getElementById('average-stars-display');
            if (visualStars) {
              const roundedAvg = Math.round(data.promedio);
              visualStars.innerHTML = '★'.repeat(roundedAvg) + '<span class="stars-row-empty">' + '★'.repeat(5 - roundedAvg) + '</span>';
            }
          }
        })
        .catch(err => console.error(err));
      });
    });
  }
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
