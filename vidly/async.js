console.log('Before');
getUser(11, logUser);
console.log('After');

function logUser(user){
	console.log(user);
	getCourses(user, logCourses)
}

function logCourses(courses){
	console.log(courses);
}

function getUser(id, callback) {
	setTimeout(() => {
		console.log('Imitation of request to the database...')
		callback({id: id, name: "Elzhan"});
	}, 1000)
}


function getCourses(user, callback){
	console.log('Calling the registrar API...')
	setTimeout(() => {
		callback(['course1', 'course2', 'course3']);	
	}, 1500)
	
}