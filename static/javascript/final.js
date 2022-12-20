window.addEventListener('load', function() {
   addScore = sessionStorage.getItem("addScore");
   addScoreM = sessionStorage.getItem("addScoreM");
   op = sessionStorage.getItem("op");


   if (isNaN(addScore)) {
      let score = 0;
      score.innerText = addScore;
      let op = sessionStorage.getItem("op");
      let opFin = document.getElementById('op');
      opFin.innerText = op;
   } else {
         let score = document.getElementById('score');
         score.innerText = addScore;
         let op = sessionStorage.getItem("op");
         let opFin = document.getElementById('op');
         opFin.innerText = op;
      }

   if (isNaN(addScoreM)) {
      let scoreM = 0;
      scoreM.innerText = addScoreM;
      opM = sessionStorage.getItem("opM");
      let opFinM = document.getElementById('opM');
      opFinM.innerText = op;
   } else {
         let scoreM = document.getElementById('scoreM');
         scoreM.innerText = addScoreM;
         opM = sessionStorage.getItem("opM");
         let opFinM = document.getElementById('opM');
         opFinM.innerText = op;
      }

   });