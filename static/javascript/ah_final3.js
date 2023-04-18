const gameOver = new Audio(); gameOver.autoplay = true; gameOver.volume = .2;

function unlockAudio() {
   gameOver.src = '/static/audio/silence.wav';
}
window.addEventListener('load', function() {
   addScore = sessionStorage.getItem("addScore");
   addScoreM = sessionStorage.getItem("addScoreM");

   if (isNaN(addScore) && isNaN(addScoreM)) {
      gameOver.src = '/static/audio/gameover.wav';
      score.innerText = 0;

   } else if(isNaN(addScore) && addScoreM > 0){
      gameOver.src = '/static/audio/gameover.wav';
      let score = document.getElementById('score');
         score.innerText = addScoreM;

   } else {
      gameOver.src = '/static/audio/gameover.wav';
      let score = document.getElementById('score');
         score.innerText = addScore;
   }

   if (isNaN(addScoreM)) {
      gameOver.src = '/static/audio/gameover.wav';
      scoreM.innerText = 0;

   } else {
      gameOver.src = '/static/audio/gameover.wav';
      let scoreM = document.getElementById('scoreM');
      scoreM.innerText = addScoreM;
   }

});