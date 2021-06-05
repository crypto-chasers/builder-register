var sum = 0;

function math(num) {
	return Math.pow(num, 3) - Math.pow(num, 1 / 3);
}

for (var i=1;i<=100;i++) {
	sum += math(i);
}

console.log(sum); // 25502149.836096782