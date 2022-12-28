    let i = 1;
    let m = 1;
    const quotes = new Array ();
    quotes[0] = '“My children love this website and I love how the site makes learning fun for them!” review by member – N. Morgan';
    quotes[1] = '"Anagram Hunt is a challenging and fun game, it has improved my daughters spelling." review by member – A. Bailey';
    quotes[2] = '“We love this site, its a family favorite! Keep up the good work.”  review by member – W. Grey';
    quotes[3] = '“The Math Facts Practice games have improved my sons math scores a great deal. Awesome job on the game!” review by member – V. Saint';

    function runQuotes3() {
        if (i === 1) {
        let section = document.querySelector("p");
        section.innerText = quotes[1];
        i = i + 1;
        }
        else if (i === 2) {
        let section = document.querySelector("p");
        section.innerText = quotes[2];
        i = i + 1;
        }
        else if (i === 3) {
        let section = document.querySelector("p");
        section.innerText = quotes[3];
        i = i + 1;
        }
        else if (i > 3) {
        i = 1;
        let section = document.querySelector("p");
        section.innerText = quotes[0];
        }
    }
    function runQuotes2() {
        if (m === 1) {
        let sectionM = document.querySelector(".quotesectionSmall");
        sectionM.innerText = quotes[1];
        m = m + 1;
         }
        else if (m === 2) {
        let sectionM = document.querySelector(".quotesectionSmall");
        sectionM.innerText = quotes[2];
        m = m + 1;
         }
         else if (m === 3) {
        let sectionM = document.querySelector(".quotesectionSmall");
        sectionM.innerText = quotes[3];
        m = m + 1;
         }
         else if (m > 3) {
        m = 1;
        let sectionM = document.querySelector(".quotesectionSmall");
        sectionM.innerText = quotes[0];
         }
    }
    window.onload = function runQuotesau() {
        let sectionM = document.querySelector(".quotesectionSmall");
        sectionM.innerText = quotes[0];
        setInterval(runQuotes2, 10000);
        let section = document.querySelector("p");
        section.innerText = quotes[0];
        setInterval(runQuotes3, 10000);
    }
