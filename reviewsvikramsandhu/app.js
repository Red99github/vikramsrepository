// local reviews data
const reviews = [
  {
    id: 1,
    name: 'lucas felske',
    job: 'painter',
    img: 'https://cdn.discordapp.com/attachments/621833619526254595/1102630960555622491/IMG_1185.jpg?ex=65b7d09a&is=65a55b9a&hm=1d1ab248fc1c27720d6af7df6dfeed6a225b66828cc9d8ca6fdb43276f4c3ce7&',
    text: "Lives in L.A now!",
  },
  {
    id: 2,
    name: 'isaiah hussain',
    job: 'carpenter',
    img: 'https://cdn.discordapp.com/attachments/891566461695447083/1176203937368522782/IMG_3074.jpg?ex=65b7d847&is=65a56347&hm=ba17449a1a3b6458a811b431644116aaea32f19548fda6d4e4a3c746e2053a3a&',
    text: 'Definitely got a 100% in computer programming last year!',
  },
  {
    id: 3,
    name: 'nikita yatsyk',
    job: 'surgeon',
    img: 'https://cdn.discordapp.com/attachments/623680704475168780/1023776864059277353/IMG_20220924_195942_488.jpg?ex=65b70781&is=65a49281&hm=ad9c7dde9001d865ef66d7d8d80434149a9c5ed912dc9d97a31ea027c1589abb&',
    text: 'Best friend since grade 5!',
  },
  {
    id: 4,
    name: 'me!!!',
    job: 'truck and trailer parts retailer',
    img: 'https://cdn.discordapp.com/attachments/1118036557593595956/1196613685624455188/IMG_3549.png?ex=65b84456&is=65a5cf56&hm=b5fa371c461e7ab22c2b723795b88b83b272a5daaf9e234d36498f3f7cdd8ef6&',
    text: 'i just need a b- man thats all i need please i know i didnt complete the modifications on the other one but I TRIED MAN',
  },
];
// select items
const img = document.getElementById('person-img');
const author = document.getElementById('author');
const job = document.getElementById('job');
const info = document.getElementById('info');

const prevBtn = document.querySelector('.prev-btn');
const nextBtn = document.querySelector('.next-btn');
const firstBtn = document.querySelector('.first-btn');
const lastBtn = document.querySelector('.last-btn');
const randomBtn = document.querySelector('.random-btn');

// set starting item
let currentItem = 0;

// load initial item
window.addEventListener('DOMContentLoaded', function () {
  showPerson(currentItem);
});

// show person based on item
function showPerson(person) {
  const item = reviews[person];
  img.src = item.img;
  author.textContent = item.name;
  job.textContent = item.job;
  info.textContent = item.text;
}
// show next person
nextBtn.addEventListener('click', function () {
  currentItem++;
  if (currentItem > reviews.length - 1) {
    currentItem = 0;
  }
  showPerson(currentItem);
});
// show prev person
prevBtn.addEventListener('click', function () {
  currentItem--;
  if (currentItem < 0) {
    currentItem = reviews.length - 1;
  }
  showPerson(currentItem);
});

// show first person
firstBtn.addEventListener('click', function () {
  currentItem += reviews.length;
  if (currentItem > reviews.length) {
    currentItem = reviews.length - 4;
  }
  showPerson(currentItem);
});
// show last person
lastBtn.addEventListener('click', function () {
  currentItem += reviews.length;
  if (currentItem > reviews.length) {
    currentItem = 3;
  }
  showPerson(currentItem);
});

// show random person
randomBtn.addEventListener('click', function () {
  console.log('bleegh');

  currentItem = Math.floor(Math.random() * reviews.length);
  showPerson(currentItem);
});
