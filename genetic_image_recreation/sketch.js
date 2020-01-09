let img;
let population;

function preload() {
  img = loadImage('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Mona_Lisa.jpg/507px-Mona_Lisa.jpg');
}

function setup() {
  createCanvas(img.width, img.height);
  pixelDensity(1);
  image(img, 0, 0);
  loadPixels();

  population = [];
  for (let i = 0; i < 10; i++){
    population.push(randomBall());
  }
}

function draw() {
  image(img, 0, 0);

  population.forEach(ball => {
    ball.climb();
  });

  population.forEach(ball => {
    ball.draw();
  });
}




// utilitary functions that are not being used

// function grid(cellSize) {
//   stroke(0);
//   for (let y = 0; y < height; y = y + cellSize) {
//     line(0, y, width, y);
//   }
//   for (let x = 0; x < width; x = x + cellSize) {
//     line(x, 0, x, height);
//   }
// }

// function getPixels() {
//   /*
//   Iterates the get() function on 
//   all the pixels on the image.
//   Returns a multi-dimensional array.
//   usage: imgPixels[y][x]
//   */
//   let p = [];
//   for (let y = 0; y < height; y++) {
//     let row = [];
//     for (let x = 0; x < width; x++) {
//       row.push(get(x, y));
//     }
//     p.push(row);
//   }
//   return p
// }
