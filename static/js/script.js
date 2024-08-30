document.addEventListener("DOMContentLoaded", function () {
  const monthYearElem = document.getElementById('monthYear');
  const datesElem = document.getElementById('dates');
  const prevButton = document.getElementById('prev');
  const nextButton = document.getElementById('next');

  let currentYear = new Date().getFullYear();
  let currentMonth = new Date().getMonth();

  function renderCalendar(year, month) {
      datesElem.innerHTML = ''; // Vyprázdníme předchozí obsah
      const date = new Date(year, month, 1);
      const daysInMonth = new Date(year, month + 1, 0).getDate();
      const startDay = date.getDay(); // 0 = Neděle, 1 = Pondělí, ...

      monthYearElem.textContent = `${date.toLocaleString('cs-CZ', { month: 'long' })} ${year}`;

      // Dnešní datum
      const today = new Date();
      const todayYear = today.getFullYear();
      const todayMonth = today.getMonth();
      const todayDate = today.getDate();

      // Přidáme prázdné dny na začátek
      for (let i = 0; i < (startDay + 6) % 7; i++) {
          datesElem.appendChild(document.createElement('div'));
      }

      // Přidáme dny v měsíci
      for (let day = 1; day <= daysInMonth; day++) {
          const dayElem = document.createElement('div');
          dayElem.className = 'day';
          dayElem.textContent = day;

          // Zkontrolujeme, zda je den dnešní
          if (year === todayYear && month === todayMonth && day === todayDate) {
              dayElem.classList.add('today');
          }

          datesElem.appendChild(dayElem);
      }
  }

  prevButton.addEventListener('click', () => {
      currentMonth--;
      if (currentMonth < 0) {
          currentMonth = 11;
          currentYear--;
      }
      renderCalendar(currentYear, currentMonth);
  });

  nextButton.addEventListener('click', () => {
      currentMonth++;
      if (currentMonth > 11) {
          currentMonth = 0;
          currentYear++;
      }
      renderCalendar(currentYear, currentMonth);
  });

  renderCalendar(currentYear, currentMonth);
});
