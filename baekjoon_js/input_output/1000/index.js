import { createInterface } from 'readline';

var rl = createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line',function(answer) {
   var input = answer.split(' '),
      a = parseInt(input[0]),
      b = parseInt(input[1]);

   console.log(a+b);
   rl.close();
});