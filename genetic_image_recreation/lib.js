class Ball {
  constructor(x, y, radius, color) {
    this.x = x;
    this.y = y;
    this.radius = radius;
    this.color = color;
    this.alpha = alpha(color);
  }

  draw() {
    noStroke();
    fill(this.color);
    circle(this.x, this.y, this.radius * 2, this.color);
  }
  
  getCovered() {
    /*
    computes euclidian distance for all
    points of a radius x radius square,
    if it is smaller than the radius, 
    it knows the point is inside the circle
    */
    let l = [];
    let minX = this.x - this.radius;
    let maxX = this.x + this.radius;
    let minY = this.y - this.radius;
    let maxY = this.y + this.radius;

    for (let x = minX; x < maxX; x++) {
      for (let y = minY; y < maxY; y++) {
        let euc_distance = Math.sqrt((x - this.x) ** 2 + (y - this.y) ** 2);
        if (euc_distance < this.radius) {
          l.push([x, y]);
        }
      }
    }

    return l
  }

  score() {
    /*
    calculates the error (color difference)
    of each covered pixel, sums and multiplies by
    alpha.
    */
    let coveredCoords = this.getCovered();

    let errors = [];

    for (let coord of coveredCoords) {
      let [x, y] = coord;
      let diff = this.colorDiff(this.color, get(x, y));
      let error = diff.reduce((r, n) => r + n);
      errors.push(error);
    }
    return (errors.reduce((r, n) => r + n) / errors.length) * this.alpha / 255;
  }

  colorDiff(c1, c2) {
    let c1Values = (typeof(c1.levels) != "undefined") ? c1.levels.slice(0, 3) : c1.slice(0, 3);
    let c2Values = (typeof(c2.levels) != "undefined") ? c2.levels.slice(0, 3) : c2.slice(0, 3);
    return c1Values.map((c, i) => Math.abs(c - c2Values[i]));
  }
  
  copy(){
    return new Ball(this.x, this.y, this.radius, this.color);
  }

  // climb(){
  //   let xCap = width / 10;
  //   let yCap = height / 10;
  //   let rCap = 10;
  //   let cCap = 15;
  //   let cArray = this.color.levels;

  //   let next = this.copy();

  //   function handleColor(colorValue){
  //     let upLim = (colorValue + cCap > 255)? 255: colorValue + cCap; 
  //     let loLim = (colorValue - cCap < 0)? 0: colorValue - cCap;
  //     return int(random(loLim,upLim));
  //   }

  //   // cases: x, y, radius, R, G, B, A
  //   switch (int(random(0,7))){
  //     case 0:
  //       next.x = int(random(next.x - xCap, next.x + xCap));
  //       break;

  //     case 1:
  //       next.y = int(random(next.y - yCap, next.y + yCap));
  //       break;

  //     case 2:
  //       next.radius = int(random(next.radius - rCap, next.radius + rCap));
  //       break;

  //     case 3:
  //       cArray[0] = handleColor(cArray[0]);
  //       break;

  //     case 4: 
  //       cArray[1] = handleColor(cArray[1]);
  //       break;

  //     case 5:
  //       cArray[2] = handleColor(cArray[2]);
  //       break;

  //     case 6:
  //       cArray[3] = handleColor(cArray[3]);
  //       break;
  //   }
  //   next.color = color(...cArray);
  //   if (next.score() > this.score()){
  //     this.x = next.x;
  //     this.y = next.y;
  //     this.radius = next.radius;
  //     this.color = next.color;
  //   }
  }
}

function randomBall(){
  let x = int(random(width));
  let y = int(random(height));
  let radius = int(random(100));
  let color_ = color(
    int(random(255)),
    int(random(255)),
    int(random(255)),
    int(random(255))
  );
  return new Ball(x, y, radius, color_)
}
