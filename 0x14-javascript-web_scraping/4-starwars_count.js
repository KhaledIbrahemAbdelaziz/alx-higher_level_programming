#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, bodoy) {
	if (!error) {
		const res = JSON.parse(body).results;
		console.log(res.reduce((count, movie) => {
			return movie.characters.find((character) => character.endsWith('/18/'))
				? count + 1
				: count;
		}, 0));
	}
});
