const gameOver = new Audio(); gameOver.autoplay = true; gameOver.volume = .5;

function unlockAudio() {
   gameOver.src = '/static/audio/silence.wav';
}
window.addEventListener('load', function() {
   addScore = sessionStorage.getItem("addScore");
   addScoreM = sessionStorage.getItem("addScoreM");
   lastAnagram = sessionStorage.getItem("lastAnagram");

   let anagramPlace = document.getElementById('anagramPlace');
   anagramPlace.innerText = lastAnagram;
   let anagramPlace2 = document.getElementById('anagramPlace2');
   anagramPlace2.innerText = lastAnagram;


   if (isNaN(addScore) && isNaN(addScoreM)) {
      gameOver.src = '/static/audio/progress.wav';
      score.innerText = 0;

   } else if(isNaN(addScore) && addScoreM > 0){
      gameOver.src = '/static/audio/progress.wav';
      let score = document.getElementById('score');
         score.innerText = addScoreM;

   } else {
      gameOver.src = '/static/audio/progress.wav';
      let score = document.getElementById('score');
         score.innerText = addScore;
   }

   if (isNaN(addScoreM)) {
      gameOver.src = '/static/audio/progress.wav';
      scoreM.innerText = 0;

   } else {
      gameOver.src = '/static/audio/progress.wav';
      let scoreM = document.getElementById('scoreM');
      scoreM.innerText = addScoreM;
   }

});