const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost/mongo-exercises')
	.then(() => console.log(`Connected...`))
	.catch(err => console.error(`Connection failed...`));


const genreSchema = new mongoose.Schema({
	name: String,
	author: String,
	tags: [String],
	date: Date,
	isPublished: Boolean,
	price: Number
});

const Course = mongoose.model('Course', genreSchema);


async function getCourse(){
	return await Course.find().sort({name: 1}).select({name: 1, author: 1})
};

getCourse()
	.then(result => {
		console.log(result)
	})