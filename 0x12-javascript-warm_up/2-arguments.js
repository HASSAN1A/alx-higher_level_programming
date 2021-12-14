#!/usr/bin/node
let argus;
if (process.argv.length < 3) {
  argus = 'No argument';
} else if (process.argv.length === 3) {
  argus = 'Argument found';
} else {
  argus = 'Arguments found';
}
console.log(argus);
