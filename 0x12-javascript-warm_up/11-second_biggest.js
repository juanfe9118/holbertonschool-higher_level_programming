#!/usr/bin/node
args = process.argv;
if (args.length <= 3){
    console.log(0);
} else {
  let arr = []
  for (let i = 2; i < args.length; i++){
    arr.push(args[i]);
  }
  arr.sort(function(a, b){return b - a});
  console.log(arr[1]);
}