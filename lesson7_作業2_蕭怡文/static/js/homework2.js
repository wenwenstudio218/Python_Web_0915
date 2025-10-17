document.addEventListener('DOMContentLoaded', function () {

    const toggleButton = document.querySelector('.toggle-button');
    const answerContent = document.querySelector('.answer-content');

    toggleButton.addEventListener('click', function () {
        answerContent.classList.toggle('visible');

        if (answerContent.classList.contains('visible')) {
            toggleButton.textContent = '關閉答案';
        } else {
            toggleButton.textContent = '顯示答案';
        }
    });

});