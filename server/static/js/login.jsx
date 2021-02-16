'use strict';
function Login() {

	// function will go here
	return (
		<div>
			<h1>Log In</h1>
			<Form.Group controlId="formBasicEmail">
				<Form.Label>Email address</Form.Label>
				<Form.Control type="email" placeholder="Enter email" />
				<Form.Text className="text-muted">
				We'll never share your email with anyone else.
				</Form.Text>
			</Form.Group>

			<Form.Group controlId="formBasicPassword">
				<Form.Label>Password</Form.Label>
				<Form.Control type="password" placeholder="Password" />
			</Form.Group>

			<Button variant="primary">Log In</Button>
			
		</div>
	)
}

// class Login extends React.Component  {
// 	constructor(props) {
// 		super(props);
// 	}
// 	render(){
// 		return (
// 			<div>
// 				<h1>Log In</h1>
// 				<Form.Group controlId="formBasicEmail">
// 					<Form.Label>Email address</Form.Label>
// 					<Form.Control type="email" placeholder="Enter email" />
// 					<Form.Text className="text-muted">
// 					We'll never share your email with anyone else.
// 					</Form.Text>
// 				</Form.Group>
	
// 				<Form.Group controlId="formBasicPassword">
// 					<Form.Label>Password</Form.Label>
// 					<Form.Control type="password" placeholder="Password" />
// 				</Form.Group>
	
// 				<Button variant="primary">Log In</Button>
				
// 			</div>
// 		)
// 	}


// 	// function will go here
	
// }


// ReactDOM.render(<Map />, document.getElementById('map'));

