//const gameOver = new Audio(); gameOver.autoplay = true;

//function unlockAudio() {
//   gameOver.src = '/static/audio/silence.wav';
//}
window.addEventListener('load', function() {
   const gameOver = new Audio(); gameOver.autoplay = true;
   function unlockAudio() {
      gameOver.src = '/static/audio/silence.wav';
   }
   addScore = sessionStorage.getItem("addScore");
   addScoreM = sessionStorage.getItem("addScoreM");
   op = sessionStorage.getItem("op");
   unlockAudio();
   document.body.addEventListener('touchstart', function() {
      unlockAudio();
   });


   if (isNaN(addScore)) {
      gameOver.src = '/static/audio/gameover.wav';
      let score = 0;
      score.innerText = addScore;
      let op = sessionStorage.getItem("op");
      let opFin = document.getElementById('op');
      opFin.innerText = op;
   } else {
         gameOver.src = '/static/audio/gameover.wav';
         let score = document.getElementById('score');
         score.innerText = addScore;
         let op = sessionStorage.getItem("op");
         let opFin = document.getElementById('op');
         opFin.innerText = op;
      }

   if (isNaN(addScoreM)) {
      gameOver.src = '/static/audio/gameover.wav';
      let scoreM = 0;
      scoreM.innerText = addScoreM;
      opM = sessionStorage.getItem("opM");
      let opFinM = document.getElementById('opM');
      opFinM.innerText = op;
   } else {
         gameOver.src = '/static/audio/gameover.wav';
         let scoreM = document.getElementById('scoreM');
         scoreM.innerText = addScoreM;
         opM = sessionStorage.getItem("opM");
         let opFinM = document.getElementById('opM');
         opFinM.innerText = op;
      }

   });