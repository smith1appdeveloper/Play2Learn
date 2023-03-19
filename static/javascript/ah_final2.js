window.addEventListener('load', function() {
   addScore = sessionStorage.getItem("addScore");
   addScoreM = sessionStorage.getItem("addScoreM");
   lastAnagram = sessionStorage.getItem("lastAnagram");

   let anagramPlace = document.getElementById('anagramPlace');
   anagramPlace.innerText = lastAnagram;
   let anagramPlace2 = document.getElementById('anagramPlace2');
   anagramPlace2.innerText = lastAnagram;


   if (isNaN(addScore) && isNaN(addScoreM)) {
      score.innerText = 0;

   } else if(isNaN(addScore) && addScoreM > 0){
      let score = document.getElementById('score');
         score.innerText = addScoreM;

   } else {
      let score = document.getElementById('score');
         score.innerText = addScore;
   }

   if (isNaN(addScoreM)) {
      scoreM.innerText = 0;

   } else {
      let scoreM = document.getElementById('scoreM');
      scoreM.innerText = addScoreM;
   }

});