
const express = require('express');
const app = express();

app.use(express.json())

let genres = [{ id: 1, genre: "comedy" },
				{ id: 2, genre: "action"},
				{ id: 3, genre: "drama"}];

app.get('/api/genres', (req, res) => {
	res.send(genres)
	console.log("genres")
})

app.get('/api/genres/:id', (req, res) => {
	const genreId = req.params.id;
	const genre = genres.find((element) => element[id] === genreId)
	if (!genre){
		res.status(404).send("Genre not found");
		return
	}
	res.send(genre);
})

app.post('/api/genres', (req, res) => {
	console.log(req.body);
	if (!req.body.genre){
		res.status(400).send("Genre is not provided!");
		return
	}
	const obj = {
		id: genres.length + 1,
		genre: req.body.genre
	}

	genres.push(obj);
	res.send(obj);
})

app.listen(3000, () => console.log("Listening on 3000..."));