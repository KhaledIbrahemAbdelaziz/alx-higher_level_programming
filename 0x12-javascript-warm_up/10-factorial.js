#!/usr/bin/node
function fact(i) {
	if (i === 0 || isNaN(i))
		return (1);
	if (i < 0)
		return (-1);
	return (i * fact(i - 1));
}
console.log(fact(Number(process.argv[2])));
